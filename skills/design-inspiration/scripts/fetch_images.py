#!/usr/bin/env python3
"""
fetch_images.py — image search & download for design inspiration and mockup assets.

Sources (no API key needed):
  web        Bing Images (general web image search — same index breadth as Google Images)
  pinterest  Bing Images with pinterest keyword + pinterest-hosted results ranked first
  dribbble   Bing Images biased toward dribbble (UI shots)
  behance    Bing Images biased toward behance (design portfolios)
  openverse  Openverse API (openly-licensed images — safe to embed in real projects)
  wikimedia  Wikimedia Commons API (free-license images)

Sources (API key via env var):
  pexels     PEXELS_API_KEY   (free stock photos, safe for production use)
  unsplash   UNSPLASH_ACCESS_KEY (free stock photos, safe for production use)

Usage:
  python fetch_images.py "modern saas dashboard dark" --source web --count 8
  python fetch_images.py "coffee shop website" --source pinterest --count 10 --download --out ./inspiration
  python fetch_images.py "mountain landscape" --source openverse --download --out ./assets
  python fetch_images.py "office team" --source pexels --count 5 --download

Output: JSON to stdout: [{"title", "image_url", "thumbnail", "source_page", "width", "height", "license"}]
With --download, files are saved and each record gains a "local_path".

NOTE ON USE: search results (ddg/pinterest/dribbble/behance) are for INSPIRATION and
placeholder mockups only — the images are third-party copyrighted work. For images
shipped in a real product, use openverse / wikimedia / pexels / unsplash and respect
the license field returned.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

_opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor())  # DDG requires cookies from the first hit


def http_get(url, headers=None, timeout=20):
    base = {"User-Agent": UA, "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9"}
    req = urllib.request.Request(url, headers={**base, **(headers or {})})
    with _opener.open(req, timeout=timeout) as r:
        return r.read()


# --------------------------------------------------- Web search (ddgs/Bing)
def web_images(query, count, site=None):
    """General web image search. Primary engine: the `ddgs` library
    (DuckDuckGo — reliable, supports site: filters). Fallback: Bing HTML
    scrape (flaky under bot detection). Install the primary engine with:
        pip install ddgs
    """
    q = f"{query} site:{site}" if site else query
    try:
        from ddgs import DDGS
    except ImportError:
        return _bing_images(q, count)
    try:
        return [{
            "title": r.get("title", ""),
            "image_url": r.get("image"),
            "thumbnail": r.get("thumbnail"),
            "source_page": r.get("url"),
            "width": r.get("width"),
            "height": r.get("height"),
            "license": "unknown (third-party; inspiration/mockup use only)",
        } for r in DDGS().images(q, max_results=count)]
    except Exception:
        return _bing_images(q, count)


def _bing_images(q, count):
    import html as htmod
    results, first = [], 1
    while len(results) < count and first < 200:
        url = "https://www.bing.com/images/search?" + urllib.parse.urlencode(
            {"q": q, "first": first, "count": 35})
        page = http_get(url).decode("utf-8", "replace")
        blobs = re.findall(r'\bm="(\{[^"]*?murl[^"]*?\})"', page)
        if not blobs:
            break
        for blob in blobs:
            try:
                d = json.loads(htmod.unescape(blob))
            except json.JSONDecodeError:
                continue
            results.append({
                "title": d.get("t", ""),
                "image_url": d.get("murl"),
                "thumbnail": d.get("turl"),
                "source_page": d.get("purl"),
                "width": None,
                "height": None,
                "license": "unknown (third-party; inspiration/mockup use only)",
            })
        first += 35
        time.sleep(0.4)
    # dedupe by image_url, keep order
    seen, deduped = set(), []
    for r in results:
        if r["image_url"] and r["image_url"] not in seen:
            seen.add(r["image_url"])
            deduped.append(r)
    return deduped[:count]


# ----------------------------------------------------------------- Openverse
def openverse_images(query, count):
    url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
        {"q": query, "page_size": min(count, 50)})
    data = json.loads(http_get(url))
    return [{
        "title": it.get("title", ""),
        "image_url": it.get("url"),
        "thumbnail": it.get("thumbnail"),
        "source_page": it.get("foreign_landing_url"),
        "width": it.get("width"),
        "height": it.get("height"),
        "license": f"{it.get('license')} {it.get('license_version') or ''}".strip(),
    } for it in data.get("results", [])[:count]]


# ------------------------------------------------------------------ Wikimedia
def wikimedia_images(query, count):
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"filetype:bitmap {query}", "gsrlimit": count, "gsrnamespace": 6,
        "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 1024})
    data = json.loads(http_get(url))
    out = []
    for page in (data.get("query", {}).get("pages", {}) or {}).values():
        for ii in page.get("imageinfo", []):
            meta = ii.get("extmetadata", {})
            out.append({
                "title": page.get("title", ""),
                "image_url": ii.get("url"),
                "thumbnail": ii.get("thumburl"),
                "source_page": ii.get("descriptionurl"),
                "width": ii.get("width"),
                "height": ii.get("height"),
                "license": (meta.get("LicenseShortName", {}) or {}).get("value", "see source_page"),
            })
    return out[:count]


# -------------------------------------------------------------------- Pexels
def pexels_images(query, count):
    key = os.environ.get("PEXELS_API_KEY")
    if not key:
        raise RuntimeError("Set PEXELS_API_KEY (free at https://www.pexels.com/api/)")
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "per_page": min(count, 80)})
    data = json.loads(http_get(url, headers={"Authorization": key}))
    return [{
        "title": it.get("alt", ""),
        "image_url": it["src"]["large2x"],
        "thumbnail": it["src"]["medium"],
        "source_page": it.get("url"),
        "width": it.get("width"),
        "height": it.get("height"),
        "license": "Pexels License (free to use)",
    } for it in data.get("photos", [])[:count]]


# ------------------------------------------------------------------ Unsplash
def unsplash_images(query, count):
    key = os.environ.get("UNSPLASH_ACCESS_KEY")
    if not key:
        raise RuntimeError("Set UNSPLASH_ACCESS_KEY (free at https://unsplash.com/developers)")
    url = "https://api.unsplash.com/search/photos?" + urllib.parse.urlencode(
        {"query": query, "per_page": min(count, 30)})
    data = json.loads(http_get(url, headers={"Authorization": f"Client-ID {key}"}))
    return [{
        "title": it.get("alt_description") or it.get("description") or "",
        "image_url": it["urls"]["regular"],
        "thumbnail": it["urls"]["small"],
        "source_page": it["links"]["html"],
        "width": it.get("width"),
        "height": it.get("height"),
        "license": "Unsplash License (free to use)",
    } for it in data.get("results", [])[:count]]


SOURCES = {
    "web": lambda q, n: web_images(q, n),
    "pinterest": lambda q, n: web_images(q, n, site="pinterest.com"),
    "dribbble": lambda q, n: web_images(q, n, site="dribbble.com"),
    "behance": lambda q, n: web_images(q, n, site="behance.net"),
    "openverse": openverse_images,
    "wikimedia": wikimedia_images,
    "pexels": pexels_images,
    "unsplash": unsplash_images,
}


def safe_name(s, i):
    base = re.sub(r"[^\w\- ]+", "", s or "")[:50].strip().replace(" ", "_") or "image"
    return f"{i:02d}_{base}"


def download(results, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for i, r in enumerate(results, 1):
        url = r.get("image_url") or r.get("thumbnail")
        if not url:
            continue
        ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif"):
            ext = ".jpg"
        path = os.path.join(out_dir, safe_name(r.get("title", ""), i) + ext)
        try:
            with open(path, "wb") as f:
                f.write(http_get(url, headers={"Referer": r.get("source_page") or url}))
            r["local_path"] = path
        except Exception as e:
            r["download_error"] = str(e)
        time.sleep(0.3)
    return results


def main():
    ap = argparse.ArgumentParser(description="Search/download images for design work")
    ap.add_argument("query")
    ap.add_argument("--source", default="web", choices=sorted(SOURCES))
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--download", action="store_true")
    ap.add_argument("--out", default="./design-inspiration")
    args = ap.parse_args()

    try:
        results = SOURCES[args.source](args.query, args.count)
    except Exception as e:
        print(json.dumps({"error": str(e), "source": args.source}), file=sys.stderr)
        sys.exit(1)
    if args.download:
        results = download(results, args.out)
    json.dump(results, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
