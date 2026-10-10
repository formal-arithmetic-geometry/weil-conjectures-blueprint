+++
id = "lem-zl-affine-curve-range"
kind = "lemma"
title = "Cohomological range of an affine curve"
order = 2735
uses = ["def-compact-support-direct-image-detailed", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-qbar-category", "lem-sc-cohomological-dimension", "lem-sc-compactification", "lem-weil-pbc-mittag-leffler", "prop-weil-pbc-direct-image-limits", "sbc-thm-finiteness-finite-type"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.subsingleton_compactlySupportedCohomology_of_isAffine"]
+++
If $C_0$ is a smooth affine curve over $k_0$ (affine and smooth of
relative dimension one) and $\mathcal F$ is a constructible Weil sheaf on
$C_0$ in the coefficients of [def-weil-pbc-qbar-category], then
$H_c^i(C,\mathcal F)=0$ for $i\notin\{0,1,2\}$.
