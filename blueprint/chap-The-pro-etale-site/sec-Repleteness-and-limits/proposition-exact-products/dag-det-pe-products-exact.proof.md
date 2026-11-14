+++
kind = "proof"
of = "dag-det-pe-products-exact"
tags = ["sheaf-dag"]
uses = ["dag-det-pe-sections-limits-colimits", "dag-det-pe-sections-conservative", "dag-sk-def-pe-weak-contractible"]
+++
1. Let L be the discrete-I limit functor on module sheaves. It is additive because it preserves binary products. To prove that L preserves finite colimits it suffices, by Mathlib Functor.exact_tfae, to prove that it preserves exact short complexes. Fix an exact short complex S of I-indexed module-sheaf diagrams and an affine weakly contractible W. By det-pe-sections-limits-colimits, evaluation E at W preserves finite limits and finite colimits. Whiskering diagrams with E is therefore exact, so S remains exact after evaluation. Mathlib ModuleCat.AB supplies exact products of modules; transport its instance from ULift I to I along the discrete equivalence to account for the coefficient and index universes. Applying the module limit functor gives an exact short complex. (uses [dag-det-pe-sections-limits-colimits])
2. The natural isomorphism preservesLimitNatIso E identifies the evaluated sheaf-limit short complex with the module-limit short complex just shown exact. Transport exactness along the induced short-complex isomorphism. Apply the first clause of det-pe-sections-conservative to conclude exactness of S.map L. Functor.exact_tfae now gives finite-colimit preservation by L, which is HasExactLimitsOfShape (Discrete I). This also proves endpoint exactness: preservation of all exact short complexes implies preservation of short exact complexes, by applying exactness to zero-endpoint complexes as in Mathlib exact_tfae. The argument includes empty I. (uses [dag-det-pe-sections-conservative])

Proof dependencies not drawn: `sk-def-pbc-conventions`.
