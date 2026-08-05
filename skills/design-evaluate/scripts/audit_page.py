#!/usr/bin/env python3
"""
audit_page.py — static UX & accessibility audit of HTML/CSS files. Pure stdlib.

Checks (each finding: severity critical|important|polish, rule id, message, line):
  structure   missing <title>, lang attr, meta viewport, h1 count, heading level skips
  images      <img> without alt
  forms       inputs without an associated <label>/aria-label/placeholder-only labels
  links       vague link text ("click here", "read more"), empty links/buttons,
              target=_blank without rel=noopener
  a11y        positive tabindex, missing skip link on long pages, autoplay media,
              <div onclick> without role/tabindex
  css         color/background pairs failing WCAG contrast, font-family overload (>3),
              px font sizes below 12px, !important overload, missing :focus styles
              when :hover is styled

Usage:
  python audit_page.py index.html                 # audits file + linked local css
  python audit_page.py ./site --json out.json     # audits every .html in folder
Output: JSON report to stdout (and --json file if given).
"""

import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser

VAGUE_LINK_TEXT = {"click here", "here", "read more", "learn more", "more", "link", "this"}


# ---------------------------------------------------------------- color math
def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def parse_css_color(val):
    val = val.strip().lower()
    m = re.match(r"#([0-9a-f]{3}|[0-9a-f]{6})\b", val)
    if m:
        return hex_to_rgb(m.group(0))
    m = re.match(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", val)
    if m:
        return tuple(int(m.group(i)) for i in (1, 2, 3))
    named = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0),
             "gray": (128, 128, 128), "grey": (128, 128, 128)}
    return named.get(val)


def rel_lum(rgb):
    def ch(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(c1, c2):
    l1, l2 = sorted((rel_lum(c1), rel_lum(c2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


# ------------------------------------------------------------------- parser
class Auditor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.findings = []
        self.headings = []
        self.h1_count = 0
        self.has_title = False
        self.has_viewport = False
        self.lang = None
        self.labels_for = set()
        self.inputs = []          # (line, attrs)
        self.link_stack = None    # (line, attrs, text)
        self.button_stack = None
        self.text_len = 0
        self.has_skip_link = False
        self.css_links = []

    def add(self, sev, rule, msg, line=None):
        self.findings.append({"severity": sev, "rule": rule, "message": msg,
                              "line": line if line is not None else self.getpos()[0]})

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self.has_title = True
        elif tag == "meta" and a.get("name", "").lower() == "viewport":
            self.has_viewport = True
        elif tag == "link" and a.get("rel", "").lower() == "stylesheet" and a.get("href"):
            self.css_links.append(a["href"])
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            lvl = int(tag[1])
            if lvl == 1:
                self.h1_count += 1
            if self.headings and lvl > self.headings[-1] + 1:
                self.add("important", "heading-skip",
                         f"Heading level jumps from h{self.headings[-1]} to h{lvl} "
                         "(screen-reader users lose document structure)", line)
            self.headings.append(lvl)
        elif tag == "img":
            if "alt" not in a:
                self.add("critical", "img-alt",
                         f"<img src=\"{(a.get('src') or '')[:40]}\"> has no alt attribute", line)
        elif tag in ("input", "textarea", "select"):
            if a.get("type") in ("hidden", "submit", "button"):
                return
            self.inputs.append((line, a))
        elif tag == "label" and a.get("for"):
            self.labels_for.add(a["for"])
        elif tag == "a":
            self.link_stack = [line, a, ""]
            href = a.get("href", "")
            if a.get("target") == "_blank" and "noopener" not in (a.get("rel") or ""):
                self.add("polish", "blank-noopener",
                         "target=_blank without rel=\"noopener\"", line)
            if href.startswith("#") and "skip" in (href + str(a.get("class", ""))).lower():
                self.has_skip_link = True
        elif tag == "button":
            self.button_stack = [line, a, ""]
        if "tabindex" in a:
            try:
                if int(a["tabindex"]) > 0:
                    self.add("important", "positive-tabindex",
                             f"tabindex={a['tabindex']} overrides natural focus order", line)
            except ValueError:
                pass
        if tag == "div" and "onclick" in a and "role" not in a:
            self.add("critical", "div-onclick",
                     "<div onclick> without role/tabindex — invisible to keyboard "
                     "and screen-reader users; use <button>", line)
        if tag in ("video", "audio") and "autoplay" in a:
            self.add("important", "autoplay", f"<{tag} autoplay> — WCAG 1.4.2", line)

    def handle_data(self, data):
        self.text_len += len(data.strip())
        if self.link_stack is not None:
            self.link_stack[2] += data
        if self.button_stack is not None:
            self.button_stack[2] += data

    def handle_endtag(self, tag):
        if tag == "a" and self.link_stack:
            line, a, text = self.link_stack
            t = " ".join(text.split()).lower()
            if not t and not a.get("aria-label") and not a.get("title"):
                self.add("critical", "empty-link", "Link with no accessible text", line)
            elif t in VAGUE_LINK_TEXT:
                self.add("important", "vague-link",
                         f'Link text "{t}" is meaningless out of context '
                         "(screen readers navigate by link list)", line)
            self.link_stack = None
        elif tag == "button" and self.button_stack:
            line, a, text = self.button_stack
            if not text.strip() and not a.get("aria-label"):
                self.add("critical", "empty-button", "Button with no accessible text", line)
            self.button_stack = None

    def finalize(self, path):
        if not self.has_title:
            self.add("important", "no-title", "Missing <title>", 1)
        if not self.lang:
            self.add("important", "no-lang", "<html> missing lang attribute", 1)
        if not self.has_viewport:
            self.add("critical", "no-viewport",
                     "Missing viewport meta — page will not be usable on mobile", 1)
        if self.h1_count == 0:
            self.add("important", "no-h1", "No <h1> on the page", 1)
        elif self.h1_count > 1:
            self.add("polish", "multi-h1", f"{self.h1_count} <h1> elements (prefer one)", 1)
        for line, a in self.inputs:
            iid = a.get("id")
            if not ((iid and iid in self.labels_for) or a.get("aria-label")
                    or a.get("aria-labelledby")):
                what = a.get("name") or a.get("placeholder") or a.get("type") or "input"
                self.add("critical", "unlabeled-input",
                         f"Form field '{what}' has no <label>/aria-label "
                         "(placeholder alone disappears on input)", line)
        if self.text_len > 4000 and not self.has_skip_link:
            self.add("polish", "no-skip-link",
                     "Long page without a skip-to-content link", 1)


# ---------------------------------------------------------------- CSS audit
def audit_css(css_text, findings, fname):
    def add(sev, rule, msg, line):
        findings.append({"severity": sev, "rule": rule, "message": f"[{fname}] {msg}",
                         "line": line})

    fams = set(re.findall(r"font-family\s*:\s*([^;}]+)", css_text, re.I))
    primary = {f.split(",")[0].strip().strip("'\"").lower() for f in fams}
    primary -= {"inherit", "sans-serif", "serif", "monospace", "system-ui"}
    if len(primary) > 3:
        add("polish", "font-overload",
            f"{len(primary)} font families ({', '.join(sorted(primary))}) — 2 is usually enough", 1)

    for m in re.finditer(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", css_text, re.I):
        if float(m.group(1)) < 12:
            add("important", "tiny-text",
                f"font-size {m.group(1)}px is below the 12px readability floor",
                css_text.count("\n", 0, m.start()) + 1)

    n_imp = css_text.count("!important")
    if n_imp > 5:
        add("polish", "important-overload",
            f"{n_imp} uses of !important — sign of specificity battles", 1)

    if ":hover" in css_text and ":focus" not in css_text:
        add("critical", "no-focus-styles",
            "Styles :hover but never :focus — keyboard users get no visual feedback", 1)

    # contrast: rules that declare both color and background(-color)
    for m in re.finditer(r"([^{}]+)\{([^}]*)\}", css_text):
        body = m.group(2)
        col = re.search(r"(?<![\w-])color\s*:\s*([^;]+)", body, re.I)
        bg = re.search(r"background(?:-color)?\s*:\s*([^;]+)", body, re.I)
        if col and bg:
            c1, c2 = parse_css_color(col.group(1)), parse_css_color(bg.group(1))
            if c1 and c2:
                r = contrast(c1, c2)
                if r < 3.0:
                    line = css_text.count("\n", 0, m.start()) + 1
                    add("critical", "low-contrast",
                        f"'{m.group(1).strip()[:40]}' pairs {col.group(1).strip()} on "
                        f"{bg.group(1).strip()} — ratio {r:.2f}:1 (WCAG needs 4.5:1)", line)
                elif r < 4.5:
                    line = css_text.count("\n", 0, m.start()) + 1
                    add("important", "borderline-contrast",
                        f"'{m.group(1).strip()[:40]}' ratio {r:.2f}:1 — OK for large "
                        "text only", line)


# ------------------------------------------------------------------- runner
def audit_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        html = f.read()
    a = Auditor()
    a.feed(html)
    a.finalize(path)
    findings = a.findings
    base = os.path.dirname(os.path.abspath(path))
    # inline <style> blocks
    for m in re.finditer(r"<style[^>]*>(.*?)</style>", html, re.S | re.I):
        audit_css(m.group(1), findings, "inline <style>")
    # linked local css
    for href in a.css_links:
        if href.startswith(("http:", "https:", "//")):
            continue
        p = os.path.normpath(os.path.join(base, href.split("?")[0]))
        if os.path.isfile(p):
            with open(p, encoding="utf-8", errors="replace") as f:
                audit_css(f.read(), findings, os.path.basename(p))
    order = {"critical": 0, "important": 1, "polish": 2}
    findings.sort(key=lambda x: (order[x["severity"]], x["rule"]))
    return findings


def main():
    ap = argparse.ArgumentParser(description="Static UX/a11y audit for HTML/CSS")
    ap.add_argument("path", help="an .html file or a folder of .html files")
    ap.add_argument("--json", help="also write report to this file")
    args = ap.parse_args()

    targets = []
    if os.path.isdir(args.path):
        for root, _, files in os.walk(args.path):
            targets += [os.path.join(root, f) for f in files if f.lower().endswith(".html")]
    else:
        targets = [args.path]

    report = {}
    for t in targets:
        report[t] = audit_file(t)
    summary = {"files": len(targets),
               "critical": sum(1 for v in report.values() for f in v if f["severity"] == "critical"),
               "important": sum(1 for v in report.values() for f in v if f["severity"] == "important"),
               "polish": sum(1 for v in report.values() for f in v if f["severity"] == "polish")}
    out = {"summary": summary, "findings": report}
    text = json.dumps(out, indent=2)
    print(text)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
