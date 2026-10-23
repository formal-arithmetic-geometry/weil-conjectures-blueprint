+++
id = "prop-nagata-proj-standard-open"
kind = "theorem"
title = "Standard affine opens of Proj"
order = 154
lean = ["AlgebraicGeometry.Proj.basicOpenIsoSpec", "AlgebraicGeometry.Proj.iSup_basicOpen_eq_top"]
tags = ["latex:proposition"]
uses = ["def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "lemma-nagata-proj-chart-ring-cocycle"]
+++
Each homogeneous $f$ of positive degree determines an open subscheme
$D_+(f)\subseteq\operatorname{Proj}(R)$ and a canonical isomorphism

$$
D_+(f)\cong\operatorname{Spec}(R_{(f),0}).
$$

If a family $(f_i)$ of elements of $R$ generates an ideal containing the
irrelevant ideal $R_+$, the $D_+(f_i)$ (the loci of homogeneous primes not
containing $f_i$) cover $\operatorname{Proj}(R)$.
