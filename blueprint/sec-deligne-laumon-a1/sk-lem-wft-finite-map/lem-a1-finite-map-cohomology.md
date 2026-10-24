+++
id = "lem-a1-finite-map-cohomology"
kind = "lemma"
title = "Cohomology under a finite curve map"
lean = ["AlgebraicGeometry.WeilSheaf.nonempty_equiv_compactlySupportedCohomology_lowerStar_of_isFinite"]
order = 4030
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-finite-direct-image-exact", "prop-functor-package"]
+++
For a finite map $g:C_0\to\mathbf A^1_{k_0}$ of separated finite-type
$k_0$-schemes and a lisse Weil sheaf $\mathcal F$ on $C_0$,

$$
H_c^i(C,\mathcal F)\simeq H_c^i(\mathbf A^1,g_*\mathcal F)
$$

for every $i$.
