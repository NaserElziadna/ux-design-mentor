# E-commerce Conversion & Checkout UX

Grounded in Baymard Institute's large-scale checkout usability research and cart-abandonment meta-analysis. The average documented cart abandonment rate is ~70% (Baymard, meta-analysis of 49 studies), and a large share of that loss is caused by fixable UX problems, not by shoppers "just browsing." Use this file when reviewing carts, checkouts, or product pages.

## Why carts are abandoned

Baymard's tracked "reasons for abandonment during checkout" (US shoppers who abandoned after starting checkout):

- **Extra costs too high (shipping, tax, fees)** — the #1 reason, cited by ~48% (Baymard).
- **Site required account creation** — a top-3 reason (~1 in 4 abandonments).
- **Checkout too long / too complicated** — roughly 1 in 5.
- Also tracked: couldn't see total order cost up-front, didn't trust the site with card details, slow delivery, errors/crashes, too-strict returns policy, insufficient payment methods, card declined.
- "Just browsing" abandonment (~42-48% of all cart abandons) is largely unrecoverable — optimize for the rest.

Rule: every one of the fixable reasons maps to a concrete pattern below. Audit against the list, not against taste.

- [ ] Total cost (incl. shipping estimate + tax) visible before checkout starts
- [ ] No forced account creation
- [ ] Checkout completable with minimal fields and steps

## Guest checkout is a requirement, not an option

- Offer **guest checkout as a prominent, first-class path** — Baymard treats forced account creation as a direct abandonment cause.
- Order the options: guest first or equal to sign-in; never preselect "create account."
- Offer optional account creation **after** order completion ("save your details — just add a password"), when the user has all fields already filled.
- Don't disguise account creation: an "optional password" field inside guest checkout reads as forced registration. If you ask for a password, it is not guest checkout.

- [ ] Guest path visible without scrolling on the checkout entry step
- [ ] Account offer deferred to the confirmation page

## Checkout flow structure

- **Field count beats step count.** Baymard: the average checkout shows ~11.3 form fields, yet most sites can complete a guest order with ~8. Cutting fields improves completion more than merging steps.
- Multi-step (accordion or paged) vs one-page is a wash in Baymard's testing when both are well built. One-page checkouts risk overwhelming users and slow validation; multi-step risks perceived length. Either way: **show the true number of steps honestly** — a "3 steps" indicator that hides sub-steps destroys trust.
- Provide a **progress indicator** with step labels (e.g., Shipping → Payment → Review). Allow backward navigation without data loss.
- Practical field cuts: single "Full name" field; hide "Address line 2" and "Company" behind links; default "Billing = shipping address" checked; derive city/state from ZIP where possible; never ask for the same data twice.

- [ ] ≤ ~8 required fields for a typical guest order
- [ ] Progress indicator with honest step count and labels
- [ ] Back navigation preserves entered data

## Trust signals & payment

- Users judge "is this page safe?" by **visual proximity**: place security badges/SSL reassurance directly adjacent to the card fields, and visually encapsulate the payment section (border/background) — Baymard found perceived security depends on the fields *looking* secure, not on actual TLS.
- Use recognized marks (Norton, McAfee, card-network logos) over generic padlock icons where possible.
- **Payment method coverage**: offer the locally expected mix — cards + PayPal + Apple Pay/Google Pay at minimum; insufficient payment options is a tracked abandonment reason. Show accepted methods early (cart page), not only at the payment step.
- Format card fields to match the physical card: number spacing, inline card-brand detection, `autocomplete="cc-number"` etc., numeric keyboard on mobile (`inputmode="numeric"`).

- [ ] Security badge within the payment field group
- [ ] Express wallets (Apple Pay / Google Pay / PayPal) offered
- [ ] Accepted payment methods shown before checkout

## Shipping cost transparency

- Show shipping costs **before** checkout: on the product page (estimate or "free over X") and in the cart via a shipping calculator or flat statement. Hidden costs discovered at the last step are the single biggest fixable abandonment cause (48%, Baymard).
- Show an **order total that updates live** as shipping method changes.
- **Free-shipping thresholds** work: display a progress message in the cart ("Add $12 for free shipping") — it raises average order value and removes the #1 abandonment trigger; keep the threshold realistic relative to average order value.
- Show **delivery speed as a date** ("Arrives Thu, Aug 13"), not "3-5 business days" — users must translate ranges; dates convert better and reduce support contacts.

- [ ] Shipping cost or estimator visible in the cart
- [ ] Delivery estimates shown as concrete dates

## Error recovery in checkout

- Validate inline, on field blur — not only on submit. Never clear the form after a failed submit (a documented rage-quit trigger, especially for card declines).
- Error messages: adjacent to the field, specific ("Card number is 15-16 digits" not "Invalid input"), and preserved values.
- On payment failure, keep the user on the payment step with everything else intact and suggest an alternative payment method.
- Be lenient with input formats: accept spaces in card numbers, any phone format, uppercase/lowercase emails — normalize server-side instead of rejecting.

- [ ] Failed submit preserves all entered data
- [ ] Error text names the field and the fix

## Coupon-code field dangers

- A prominent, empty promo-code box tells users without a code that they're overpaying; many leave the checkout to hunt for codes (and often don't come back). Baymard recommendation: **hide the field behind a plain "Have a promo code?" link**, collapsed by default.
- Auto-apply codes from marketing links so those users never need the field.
- Never place a large promo box next to the order total on the payment step.

- [ ] Promo code collapsed behind a text link
- [ ] Campaign links auto-apply their discount

## Mobile checkout specifics

- Correct keyboards per field: `inputmode="numeric"` for card/ZIP/phone, `type="email"` for email; `autocomplete` tokens on every field so autofill works — the single biggest mobile speed win.
- Tap targets ≥ 44-48px, fields full-width, labels above fields (not placeholder-only labels, which vanish on focus).
- Sticky primary CTA at the bottom of the viewport on long steps.
- Express checkout (Apple Pay / Shop Pay / Google Pay) offered before the form — it bypasses typing entirely, the main mobile pain.

- [ ] Every field has correct `autocomplete` + `inputmode`
- [ ] Express wallet button above the manual form on mobile

## Product page conversion elements

- **Images**: multiple large images (Baymard testing supports 5+ covering "in scale," "in context," and feature close-ups), zoomable, with consistent quality. Image quality/quantity is a leading cause of product-page abandonment in Baymard's testing.
- **Reviews**: show average rating + count near the title with an anchor link jumping to full reviews; include rating distribution and user images. No reviews at all suppresses trust more than a few negative ones.
- **Above the fold**: price, availability ("In stock"), and a delivery estimate should be visible near the buy button — users hesitate to add-to-cart without knowing when it arrives.
- **Sticky add-to-cart on mobile**: keep price + CTA pinned once the original button scrolls away, since mobile product pages are long.

- [ ] ≥ 5 images incl. in-context and scale shots
- [ ] Rating summary near title, linked to reviews
- [ ] Stock status and delivery estimate above the fold

## Urgency & scarcity: the ethical line

- **Real** signals are legitimate and effective: actual low stock ("2 left"), true sale end times, genuine demand data.
- **Fabricated** urgency is a dark pattern: fake countdowns that reset on reload, invented "X people viewing," false low-stock claims. These are documented deceptive patterns (see deceptive.design's "fake urgency"/"fake scarcity") and are increasingly regulated (e.g., FTC actions, EU consumer law).
- Test yourself: if the number or timer is generated rather than measured, don't ship it. Short-term conversion lift, long-term trust destruction and legal exposure.

- [ ] Every urgency/scarcity claim traceable to real data

## Post-add-to-cart behavior

- Never do nothing: silent add-to-cart makes users click again or hunt for the cart. Always give clear confirmation.
- **Slide-in drawer / mini-cart** is the default best pattern: confirms the add, shows cart contents + subtotal, offers "Checkout" and "Continue shopping" without leaving the page. Good for multi-item shops.
- **Full redirect to cart** suits single-item purchase flows (high-ticket, one product per order) but interrupts browsing otherwise.
- Modal confirmations that must be dismissed are the weakest option — interruption without the drawer's utility.
- Update the cart icon badge in all cases.

- [ ] Add-to-cart gives immediate, dismissible confirmation with a path to checkout

## Sources

- https://baymard.com/lists/cart-abandonment-rate — abandonment rate meta-analysis and reasons-for-abandonment survey
- https://baymard.com/blog/checkout-flow-average-form-fields — average vs necessary form fields
- https://baymard.com/blog/checkout-optimization-from-16-fields-to-8 — field-reduction techniques
- https://baymard.com/blog/holistic-view-on-checkout-usability — checkout structure findings
- https://baymard.com/blog/perceived-security-of-payment-form — trust signals near payment fields
- https://baymard.com/blog/how-users-perceive-security-during-checkout
- https://www.deceptive.design/types — fake urgency/scarcity dark patterns
- https://www.nngroup.com/articles/ecommerce-product-pages/ — product page essentials
