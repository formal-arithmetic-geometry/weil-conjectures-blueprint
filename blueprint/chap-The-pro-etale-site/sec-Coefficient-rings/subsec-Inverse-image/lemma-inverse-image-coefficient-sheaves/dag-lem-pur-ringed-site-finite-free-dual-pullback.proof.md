+++
kind = "proof"
of = "dag-lem-pur-ringed-site-finite-free-dual-pullback"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-ringed-site-module-pullback-exists-universes", "dag-lem-pur-ringed-site-pullback-pairing-transfer", "dag-lem-pur-ringed-site-pullback-dual-free-chart"]
+++
1. Construct the module left adjoint by lem-pur-ringed-site-module-pullback-exists-universes. Apply lem-pur-ringed-site-pullback-pairing-transfer to the identity on each internal dual. Its unique pairing extensions give the family delta and its evaluation equation. The family is uniquely determined componentwise by this same uniqueness. (uses [dag-lem-pur-ringed-site-module-pullback-exists-universes], [dag-lem-pur-ringed-site-pullback-pairing-transfer])
2. For b:L → M apply the same pairing-transfer uniqueness to precomposition by b. Adjunction-unit naturality shows that both naturality composites evaluate on (phi,m) as a(phi(b(m))); hence both equal the unique transfer. This is the explicit Lean naturality proof. (uses [dag-lem-pur-ringed-site-pullback-pairing-transfer])
3. Map the given covering sieve through U. Finite-limit preservation makes U(1_C) terminal. The pushed-forward sieve is contained in the sieve of objects U(V_i), so these objects cover D. Each restricted delta is invertible by lem-pur-ringed-site-pullback-dual-free-chart, applied to the supplied source trivialization. The chart theorem handles internal-Hom restriction and finite biproducts internally; no separate dual trivialization is needed. Apply Mathlib Sheaf.isIso_of_coversTop to the underlying additive sheaf map, and reflect the isomorphism along SheafOfModules.toSheaf. (uses [dag-lem-pur-ringed-site-pullback-dual-free-chart])
