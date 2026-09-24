+++
id = "lemma-nagata-rees-generators-cover-proj"
kind = "lemma"
title = "Degree-one generators cover Proj"
order = 281
lean = ["AlgebraicGeometry.Proj.iSup_basicOpen_eq_top"]
uses = ["def-nagata-affine-proj", "prop-nagata-rees-finite-generation"]
+++
If $I=(f_0,\ldots,f_r)$, then the standard opens
$D_+(f_it)$ cover $\operatorname{Proj}(\mathcal R_A(I))$.

## Proof

The elements $f_it$ generate the irrelevant ideal by
[prop-nagata-rees-finite-generation]. Apply
`AlgebraicGeometry.Proj.iSup_basicOpen_eq_top` to obtain the
asserted cover; equivalently, a homogeneous prime cannot contain all
generators.
