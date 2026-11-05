+++
id = "theorem-finite-etale-covers-proper-henselian--2"
kind = "remark"
title = "Lifting finite covers"
order = 357001
aliases = ["bp-r108-2"]
lean = ["AlgebraicGeometry.Scheme.isEquivalence_pullback_finiteEtale_of_henselianRing"]
+++
*Lifting finite étale covers over a proper henselian pair.*
Let $(B,J)$ be a henselian pair, let $Y$ be proper over $B$, and let
$i:Y_0\to Y$ be the closed fibre
$Y_0=Y\times_{\operatorname{Spec}B}\operatorname{Spec}(B/J)$.
Base change along $i$ is an equivalence between the categories of finite
étale schemes over $Y$ and over $Y_0$,

$$
\textit{F\'Et}_Y\xrightarrow{\sim}
\textit{F\'Et}_{Y_0}.
$$

This is [Stacks, [0GS2](https://stacks.math.columbia.edu/tag/0GS2)], proved by algebraization, approximation, and
descent of finite presentation.
