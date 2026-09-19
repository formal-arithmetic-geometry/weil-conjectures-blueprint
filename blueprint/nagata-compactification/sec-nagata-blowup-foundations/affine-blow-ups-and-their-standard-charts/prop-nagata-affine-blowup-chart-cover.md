+++
id = "prop-nagata-affine-blowup-chart-cover"
kind = "theorem"
title = "Finite affine chart cover"
order = 207
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.iSup_opensRange_blowupι_eq_top"]
tags = ["latex:proposition"]
uses = ["lemma-nagata-rees-generators-cover-proj", "prop-nagata-affine-blowup-chart"]
+++
If $I=(f_0,\ldots,f_r)$, the affine opens

$$
\operatorname{Spec}(A[I/f_i])
$$

form a finite open cover of
$\operatorname{Bl}_I(\operatorname{Spec}A)$.

## Proof

The opens $D_+(f_it)$ cover by
[lemma-nagata-rees-generators-cover-proj]. Replace each one by the
affine spectrum supplied by [prop-nagata-affine-blowup-chart]. The
compatibility of the open embeddings with the structure map is part of that
chart isomorphism.
