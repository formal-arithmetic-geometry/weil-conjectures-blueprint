+++
id = "sk-thm-wft-curve-middle-upper"
kind = "theorem"
title = "The weight bound on a curve"
order = 760
lean = ["AlgebraicGeometry.hasWeightsAtMostOver_compactlySupportedCohomology_directImage_of_isCurve"]
uses = ["sk-i-real-boundary", "sk-p-real-semi", "sk-prop-sf-open-closed-triangle", "sk-thm-wft-affine-curve-upper"]
tags = ["sketch"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open in a smooth curve over $k_0$,
and let $F$ be a pure lisse Weil sheaf of weight $w$ on $U_0$. Then for every $r\in\mathbf Z$ the group $H_c^r(C,j_*F)$ has weights
at most $w+r$. In particular, for $U_0=C_0$, the group $H_c^r(C,F)$ has
weights at most $w+r$.
