# Reducing Anxiety & Building Confidence: Full Pattern Catalog

Non-technical admin users are frequently anxious about breaking something they can't explain or fix later. Every pattern here targets that anxiety directly, not just task efficiency.

## Wizards vs. Forms

"Novices and infrequent users like wizards; frequent and power users prefer forms." ([UXmatters — Wizards versus Forms](https://www.uxmatters.com/mt/archives/2011/09/wizards-versus-forms.php)) A stepped wizard with a visible progress indicator reduces anxiety through the endowed-progress effect (see the Goal-Gradient Effect in `../../ux-design-principles/references/laws-of-ux.md`) and limits how much a nervous user has to hold in mind at any one step.

**Apply this by task frequency, not by task complexity alone:** an admin user issuing a refund once a month, or onboarding a new employee a few times a year, is exactly the infrequent-user profile — default to a stepped flow even if the underlying task isn't objectively "complex." Reserve dense single-page forms for actions the same user repeats often enough to have built real fluency (e.g., a daily order-status update).

## Plain Language Over System Terminology

Rename internal/database vocabulary into words that match the user's actual job: "Node" → "Article," "Taxonomy" → "Category," "View Mode" → "Layout," "Entity" → whatever the entity actually represents to this user (a customer, an order, a class). Technical vocabulary is a primary, well-documented source of confusion in CMS-style tools for non-technical staff. ([evolvingweb — Content Editor UX](https://evolvingweb.com/blog/content-editor-ux-why-cms-usability-tough))

**Test:** if a term wouldn't appear in this user's own job description or in a conversation with their manager, it doesn't belong in the interface as-is — either rename it or explain it inline.

## Guardrails, Not Open Canvases

Curated component libraries, intelligent defaults, predefined and pre-validated color/style choices, and options limited by content type all reduce the number of decisions a non-technical user has to get right unassisted. An open-ended, maximally flexible interface (arbitrary custom CSS, unrestricted layout freedom, exposed raw configuration) is a burden for this audience, not a feature — constraint is the kindness here, not a limitation to apologize for.

## Inline Help Over Separate Documentation

A contextual tooltip or short inline help text positioned next to the specific control it explains beats a help center article the user has to leave the task to find and read. If a control genuinely needs an explanation, that explanation should be reachable without navigating away from the task in progress.

## Empty States as Onboarding

A blank screen with no explanation reads as either broken or unfinished to a non-technical user. An effective empty state should:
- Explain *why* it's empty in plain language (not "No data" — say what would need to happen to populate it)
- Offer exactly one obvious next action — don't showcase every possible feature to a first-timer
- Recommended ratio: roughly two parts instruction to one part delight/personality — this is functional copy first, not a branding opportunity

Reveal complexity gradually as the user actually needs it, rather than front-loading the full feature set into the first empty state they see. ([NN/g — Empty State Interface Design](https://www.nngroup.com/articles/empty-state-interface-design/))

## Audit Trails as a Trust Mechanism

A searchable, filterable "who did what, when" log serves two purposes at once: it lets a manager verify what happened, and — just as important for this audience — it lets the anxious user themselves confirm that an action is traceable and therefore recoverable. Knowing that "if I make a mistake, there's a record of exactly what I did and when" measurably reduces the fear of silently breaking something they can't later explain or undo. Surface a simple, filterable activity log as a first-class screen, not a hidden admin-only feature — the person doing the work benefits from seeing it too.

## Explicit Permission Clarity

Role/permission systems frequently confuse users because special roles behave differently without the interface ever saying so. State plainly, next to the action itself (not buried three settings screens away), who is allowed to do this and, if the current user can't, briefly why. Where feasible, apply the principle of least privilege *visually*, not just functionally — a non-technical user should only *see* the controls their role can act on, rather than seeing a greyed-out button they don't understand and can't use, which reads as a bug rather than a permission boundary.
