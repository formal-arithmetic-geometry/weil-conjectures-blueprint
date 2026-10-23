+++
id = "lem-pur-co-smooth-composition"
kind = "lemma"
title = "Composition"
lean = ["AlgebraicGeometry.Etale.IsCohomologicallySmooth.nonempty_iso_dualizingComplex_comp", "AlgebraicGeometry.Etale.IsCohomologicallySmooth.isInvertible_dualizingComplex_comp", "AlgebraicGeometry.Etale.IsCohomologicallySmooth.comp", "AlgebraicGeometry.Etale.isIso_dualizingComplexTensorMap_comp"]
order = 2368
uses = ["def-pur-co-smoothness", "def-pur-conventions", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-exceptional-inverse-image"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
if $f:X\to Y$ and $g:Y\to Z$ are cohomologically smooth, then
$gf:X\to Z$ is cohomologically smooth, and moreover

$$
\omega_{gf}\;\cong\;\omega_f\otimes^L_{\Lambda_X}Lf^*\omega_g.
$$
