+++
kind = "proof"
of = "lem-pbc-h2-integral-open-extension-comparison"
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image"]
+++
Replace upperStar on both coefficient categories by upperStarIsoOpenImmersionRestriction. Restriction is precomposition, so it commutes with the coefficient functor sectionwise. ([def-weil-pbc-inverse-image]).

Unfold extension by zero as left Kan extension followed by sheafification. E preserves limits and colimits. The existing Mathlib Functor.lanCompIsoOfPreserves and sheafComposeNatIso commute E with these operations. Compose their isomorphisms and the restriction comparisons to obtain the displayed isomorphism. ([def-weil-pbc-extension-by-zero], `CategoryTheory.presheafToSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheafification.lean))).
