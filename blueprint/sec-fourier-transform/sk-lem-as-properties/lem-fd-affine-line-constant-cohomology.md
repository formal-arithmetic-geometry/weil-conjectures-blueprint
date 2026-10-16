+++
id = "lem-fd-affine-line-constant-cohomology"
kind = "lemma"
title = "Constant cohomology of the affine line"
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant_affineLine", "AlgebraicGeometry.Etale.cohomology_affineLine_unit"]
order = 3028
uses = ["def-fd-additive-character", "def-weil-pbc-qbar-category", "lem-sc-pic-affine", "sbc-thm-cohomological-dimension-of-an-affine-curve", "thm-sc-affine-cohomology"]
+++
For $k$ finite or algebraically closed,

$$
H^q(\mathbf A^1_{\bar k},\overline{\mathbf Q}_\ell)=\begin{cases}\overline{\mathbf Q}_\ell,&q=0,\\0,&q>0.\end{cases}
$$
