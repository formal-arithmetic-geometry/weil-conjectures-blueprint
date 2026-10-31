+++
id = "sk-def-pe-wlocal"
kind = "definition"
title = "w-local, w-strictly local and w-contractible rings"
order = 38
lean = ["WLocalSpace", "IsWLocalRing", "IsWStrictlyLocalRing", "IsWContractibleRing", "WLocalSpace.isHomeomorph_connectedComponents_closedPoints"]
tags = ["sketch"]
+++
A spectral space $T$ is *w-local* if its set $T^c$ of closed
points is closed and every point specializes to exactly one closed
point. A ring $R$ is w-local if $\operatorname{Spec}(R)$ is w-local.
It is *w-strictly local* if it is w-local and
$R_{\mathfrak m}$ is strictly henselian for every maximal ideal
$\mathfrak m$. It is *w-contractible* if it is w-strictly local
and the profinite space $\pi_0(\operatorname{Spec}(R))$ is
extremally disconnected.
