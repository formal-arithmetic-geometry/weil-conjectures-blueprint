+++
id = "lemma-nagata-affine-blowup-complement"
kind = "lemma"
title = "Affine complement-of-center isomorphism"
order = 239
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isIso_blowupMap_restrict_of_ideal_eq_top"]
uses = ["def-nagata-affine-blowup", "lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-affine-blowup-top", "prop-nagata-affine-blowup-restrict"]
+++
For $Z=V(I)\subseteq\operatorname{Spec}(A)$, the affine blow-up morphism
restricts to an isomorphism over $\operatorname{Spec}(A)\setminus Z$.

## Proof

The complement is covered by the basic opens $D(a)$, $a\in I$. On $D(a)$
the localized ideal is the unit ideal, so
[prop-nagata-affine-blowup-restrict] and
[lemma-nagata-affine-blowup-top] identify the blow-up with $D(a)$.
The identifications agree on overlaps by
[lemma-nagata-affine-blowup-restrict-cocycle], and hence glue.
