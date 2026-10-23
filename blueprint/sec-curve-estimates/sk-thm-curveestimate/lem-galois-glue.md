+++
id = "lem-galois-glue"
kind = "lemma"
title = "Glueing of schemes along open immersions"
order = 1424
lean = ["AlgebraicGeometry.Scheme.GlueData", "AlgebraicGeometry.Scheme.GlueData.glued", "AlgebraicGeometry.Scheme.GlueData.vPullbackConeIsLimit", "AlgebraicGeometry.Scheme.Cover.glueMorphisms"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $Y$ be a scheme, let $\{Y_i\to Y\}$ be a Zariski cover, and for
each $i$ let $P_i\to Y_i$ be a scheme. Suppose given isomorphisms
$\varphi_{ij}:P_i\times_YY_j\to P_j\times_YY_i$ over $Y_i\times_YY_j$
with $\varphi_{ii}=\operatorname{id}$ and
$\varphi_{jk}\varphi_{ij}=\varphi_{ik}$ over the triple intersections.
Then there is a $Y$-scheme $P$ with isomorphisms
$P\times_YY_i\cong P_i$ over $Y_i$ compatible with the
$\varphi_{ij}$, unique up to unique isomorphism.
