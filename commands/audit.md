---
description: Run a full UX & accessibility audit on HTML/CSS files (measured findings + principle-based review)
argument-hint: [file-or-folder]
---
Run the static auditor on $ARGUMENTS (default: the current project's HTML files — find them first):

```
python "${CLAUDE_PLUGIN_ROOT}/skills/design-evaluate/scripts/audit_page.py" <target>
```

Then follow the design-evaluate skill: merge the measured findings (quote ratios and line numbers) with a principle-based review per the nng-heuristics reference, and report Critical / Important / Polish with concrete fixes.
