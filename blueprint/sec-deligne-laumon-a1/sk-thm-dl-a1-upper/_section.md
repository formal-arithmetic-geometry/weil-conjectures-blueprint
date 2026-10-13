+++
id = "sk-thm-dl-a1-upper"
kind = "theorem"
title = "Deligne–Laumon affine-line estimate"
order = 3129
uses = ["sk-c-dl-a1-hc1", "sk-d-dl-a1-setup", "sk-l-dl-a1-endpoints", "sk-p-dl-a1-exact", "sk-p-linear-filtration"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.hasWeightsAtMost_compactlySupportedCohomology_directImage", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.subsingleton_compactlySupportedCohomology_directImage_zero", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.isPureOfWeightOver_compactlySupportedCohomology_directImage_two"]
tags = ["sketch"]
+++
Let $j:U_0\hookrightarrow A_0$ be a dense open immersion and let $F$
be a lisse Weil sheaf, punctually $\iota$-pure of weight $w$ and
unramified at infinity. For every integer $r$,

$$
H_c^r(A,j_*F)\quad\text{has weights at most }w+r.
$$

More precisely, degree zero vanishes, degree two is pure of weight
$w+2$, and only the degree-one upper bound requires the Fourier argument.
