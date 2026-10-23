+++
id = "sk-p-real-rankin"
kind = "proposition"
title = "The determinant upper bound"
order = 3877
uses = ["sk-cor-walg-curve-calculus", "sk-d-real-detweights", "sk-def-wrp-real-definition", "sk-i-restriction", "sk-lem-wrp-hc2", "sk-lem-wrp-positive-euler", "sk-p-linear-filtration", "sk-p-tensor", "sk-thm-trace-transport"]
lean = ["AlgebraicGeometry.WeilGroup.hasWeightsAtMost_of_isReal"]
tags = ["sketch"]
+++
Let $U_0/\mathbf F_q$ be a smooth geometrically connected affine curve
and let $\mathcal G\ne0$ be a lisse $\iota$-real Weil sheaf
([sk-def-wrp-real-definition]). If $\beta$ is the largest determinant weight
([sk-d-real-detweights]) of its irreducible Weil constituents, then

$$
 |\iota(\alpha)|^2\le q_x^\beta
 \quad(x\in|U_0|,\ \alpha\text{ an eigenvalue on }\mathcal G_{\bar x}).
$$
