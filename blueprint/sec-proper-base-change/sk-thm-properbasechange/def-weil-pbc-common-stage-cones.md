+++
id = "def-weil-pbc-common-stage-cones"
kind = "definition"
title = "Common-stage cones and distinguished triangles"
order = 1370
uses = ["def-weil-pbc-finite-stage-pair-category", "prop-weil-pbc-common-stage-calculus"]
+++
Let $f=[M,u]:(E,K)\to(F,L)$ be a morphism of the finite-stage pair category
[def-weil-pbc-finite-stage-pair-category], represented over the finite field
$M$. Choose in $\mathcal C_M(T)$ a distinguished cone triangle
$$
 T_{M/E}K\xrightarrow{u}T_{M/F}L
 \xrightarrow{i_u}C(u)\xrightarrow{p_u}(T_{M/E}K)[1].
$$
Its image in $\mathcal P_T$ is the triangle with cone object $(M,C(u))$,
second arrow represented by $i_u$, and third arrow represented by
$$
 \sigma_{M/E,K}^{-1}\circ p_u:
 C(u)\longrightarrow T_{M/E}(K[1]).
$$
A triangle in $\mathcal P_T$ is distinguished if it is isomorphic to such a
common-stage cone triangle.
