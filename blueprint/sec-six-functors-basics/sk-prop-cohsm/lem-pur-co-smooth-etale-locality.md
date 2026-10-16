+++
id = "lem-pur-co-smooth-etale-locality"
kind = "lemma"
title = "Source-etale locality, without derived descent"
lean = ["AlgebraicGeometry.Etale.nonempty_dualizingComplex_iso_constantComplex_of_etale", "AlgebraicGeometry.Etale.isCohomologicallySmooth_of_etale", "AlgebraicGeometry.Etale.IsCohomologicallySmooth.of_comp_of_surjective", "AlgebraicGeometry.Etale.isIso_dualizingComplexTensorMap_of_comp", "AlgebraicGeometry.Etale.isInvertible_of_isInvertible_leftDerivedUpperStar_of_etale", "AlgebraicGeometry.Etale.isInvertible_dualizingComplex_of_comp"]
order = 2338
uses = ["def-pur-co-smoothness", "def-pur-conventions", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-exceptional-inverse-image", "def-weil-scheme-morphism-properties", "lem-pur-etale-iso-descent"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $u:U\to X$ be a surjective etale morphism of separated
finite-type schemes. If $fu:U\to Y$ is cohomologically smooth, then
$f:X\to Y$ is cohomologically smooth. Every etale map $u$ is
cohomologically smooth, with $\omega_u\simeq\Lambda$.
