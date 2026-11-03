+++
id = "sk-p-real-rankin"
kind = "proposition"
title = "A bound by the largest determinant weight"
order = 688
lean = ["AlgebraicGeometry.WeilGroup.hasWeightsAtMost_of_isReal"]
uses = ["sk-d-real-detweights", "sk-def-wrp-real-definition", "sk-i-restriction", "sk-lem-wrp-hc2", "sk-lem-wrp-positive-euler", "sk-p-linear-filtration", "sk-prop-walg-determinant-weights", "sk-thm-trace-transport", "sk-r-linear-library"]
tags = ["sketch"]
+++
Let $U_0/\mathbf F_q$ be a smooth geometrically connected affine curve
and let $\mathcal G\ne0$ be a lisse $\iota$-real Weil sheaf. If $\beta$
is the largest determinant weight of its irreducible Weil constituents,
then

$$
|\iota(\alpha)|^2\le q_x^\beta
\quad(x\in|U_0|,\ \alpha\text{ an eigenvalue on }\mathcal G_{\bar x}).
$$
