---
description: Generate a WCAG-validated design-token system from a brand color
argument-hint: <brand-hex e.g. #4f46e5>
---
Generate design tokens for brand color $ARGUMENTS:

```
python "${CLAUDE_PLUGIN_ROOT}/skills/design-systems/scripts/design_tokens.py" "$ARGUMENTS" --format css
python "${CLAUDE_PLUGIN_ROOT}/skills/design-systems/scripts/design_tokens.py" "$ARGUMENTS"
```

Present the CSS variables, explain the accessibility pairings report (which steps pass AA on white/dark, button recommendation), and offer to write the tokens into the project's stylesheet per the design-systems skill.
