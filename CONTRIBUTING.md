# Contributing

Contributions welcome — especially new reference files and skills.

- **References** (`skills/*/references/*.md`): every claim must cite an authoritative source (NN/g, Baymard, W3C, Material, Apple HIG, or a named book). No unattributed opinion. End each file with a Sources section.
- **Skills** (`skills/<name>/SKILL.md`): frontmatter `description` must contain concrete trigger phrases AND disambiguation against sibling skills. Keep the body a decision procedure; put depth in references/.
- **Scripts** (`skills/*/scripts/*.py`): stdlib-only where possible (Pillow/ddgs acceptable); JSON output; must pass `python -m py_compile` (CI enforces).
- Run the CI checks locally before opening a PR.
