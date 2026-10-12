+++
kind = "proof"
of = "lem-weil-pbc-constructible-closed-generic-criterion"
uses = ["def-constructible-stratification", "prop-constructible-open-closed", "prop-constructible-pullback"]
+++
Induct on closed subsets C of X, with the strengthened claim for every closed immersion i:Z -> X whose range is contained in C. Closed subsets satisfy the well-founded descending condition. Z is Noetherian since it is a closed subscheme of X; in Lean use LocallyOfFiniteType.isLocallyNoetherian and QuasiCompact.compactSpace_of_compactSpace, both applied to i, then construct IsNoetherian Z. (`AlgebraicGeometry.IsNoetherian.noetherianSpace, TopologicalSpace.instWellFoundedLTClosedsOfNoetherianSpace, WellFounded.has_min` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Noetherian.lean))).

For empty Z its sheaf is zero and therefore constructible. Otherwise choose the dense open U supplied by the hypothesis; it is nonempty. The reduced closed complement i′:Z′ -> Z has range Z minus U. Its image C′ in X is a proper closed subset of C: a point of U maps to C but cannot lie in that image because i is injective. Apply the induction hypothesis to i′ composed with i. (`AlgebraicGeometry.Scheme.IdealSheafData.subschemeι` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/IdealSheaf/Subscheme.lean))).

Pullback composition transports the constructibility just obtained to the restriction of i^*F to Z′. On U the finite locally constant sheaf is constructible by the trivial one-stratum stratification and pullback stability. Apply the existing open-closed constructibility equivalence to glue these two restrictions. Finally take C=X and i=id, and use the identity pullback isomorphism. ([prop-constructible-pullback], [prop-constructible-open-closed], [def-constructible-stratification]).
