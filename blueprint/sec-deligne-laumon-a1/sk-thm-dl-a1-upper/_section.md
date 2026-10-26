+++
id = "sk-thm-dl-a1-upper"
kind = "theorem"
title = "The weight bound on the affine line"
order = 4024
uses = ["sk-c-dl-a1-hc1", "sk-l-dl-a1-endpoints", "sk-lem-wft-character-integral", "sk-p-dl-a1-exact", "sk-p-dl-a1-middle", "sk-p-linear-filtration"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.hasWeightsAtMost_compactlySupportedCohomology_directImage", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.subsingleton_compactlySupportedCohomology_directImage_zero", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isPureOfWeightOver_compactlySupportedCohomology_directImage_two"]
tags = ["sketch"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open, and let
$F$ be a lisse sheaf on $U_0$, pure of weight $w$ and unramified at
infinity. Then

$$
 \operatorname{wt}H_c^r(\mathbf A^1,j_*F)\le w+r
 \qquad(r\in\mathbf Z).
$$

Degree zero vanishes, degree two is pure of weight $w+2$, and
there is no cohomology outside degrees $0,1,2$.
