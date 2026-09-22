+++
id = "lem-cbc-extension-zero-composition"
kind = "lemma"
title = "Composition of open immersions"
order = 6606
lean = ["AlgebraicGeometry.Etale.extensionByZero_comp"]
uses = ["def-cbc-extension-by-zero"]
+++
For composable open immersions $U\hookrightarrow V\hookrightarrow X$, the
canonical comparison
$$
 (j_2)_!(j_1)_!F\xrightarrow{\ \sim\ }(j_2j_1)_!F
$$
is an isomorphism, natural in $F$ and compatible with the identity open
immersion and the two ways of composing three open immersions.

## Proof

All three functors are left adjoint to the corresponding inverse image
functors, and the two candidates are the left adjoints of the same functor
($(j_2j_1)^{-1}=(j_1)^{-1}(j_2)^{-1}$), so they are canonically isomorphic
(the comparison being the mate of the identification of inverse images);
naturality and the coherence equations follow from the adjunction calculus, as
in [def-cbc-extension-by-zero].

Unresolved dependencies: def:weil-pbc-scheme-conventions
