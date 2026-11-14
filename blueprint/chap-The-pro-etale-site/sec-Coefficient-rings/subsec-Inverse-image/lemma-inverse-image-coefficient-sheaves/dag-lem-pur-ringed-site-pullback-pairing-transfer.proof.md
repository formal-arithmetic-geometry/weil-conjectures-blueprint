+++
kind = "proof"
of = "dag-lem-pur-ringed-site-pullback-pairing-transfer"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-ringed-site-pullback-localization-universes", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
1. By the independent-universe localization comparison, a map from (FL)|U(V) to S|U(V) is equivalent to a map L|V → U_V*(S|U(V)). Apply this to the functional b(p), followed by the coefficient ring map. This defines the lift of each local functional, with the required evaluation on global unit sections. (uses [dag-lem-pur-ringed-site-pullback-localization-universes])
2. Uniqueness in this localized adjunction proves additivity, scalar linearity and compatibility with restriction of those lifts. They therefore give a module morphism P → U_* Hom(FL,S). Take its adjunct to obtain d. The two adjunction unit equations give the stated evaluation. For uniqueness, global adjunction reduces to equality of local Hom sections, and the localized Hom equivalence detects that equality on all restricted unit sections. (uses [dag-lem-pur-ringed-site-pullback-localization-universes], [dag-lem-pur-ringed-site-module-pullback-exists-universes])
