+++
id = "det-pe-wlocal-strict-contractible"
kind = "definition"
title = "w-strictly local and w-contractible rings"
lean = ["IsWLocalRing", "IsWStrictlyLocalRing", "IsWContractibleRing", "IsStrictlyHenselianLocalRing", "ExtremallyDisconnected"]
order = 893
uses = ["def-weil-pbc-w-local", "def-weil-pbc-henselian-terminology", "det-pe-wlocal-components"]
+++
Let $R$ be a ring and $T=\operatorname{Spec}R$, a spectral space with set $T^c$ of closed
points (the maximal ideals of $R$).

1. $R$ is *w-local* if $T$ is w-local [def-weil-pbc-w-local]: $T^c$ is closed in $T$ and
   every prime of $R$ is contained in exactly one maximal ideal.
2. $R$ is *w-strictly local* if it is w-local and, for every maximal ideal $\mathfrak m$,
   the local ring $R_{\mathfrak m}$ is strictly henselian
   [def-weil-pbc-henselian-terminology].
3. $R$ is *w-contractible* if it is w-strictly local and the profinite space
   $\pi_0(T)$ of connected components (with the quotient topology from $T$) is
   extremally disconnected: the closure of every open subset of $\pi_0(T)$ is open.
   Equivalently, by [det-pe-wlocal-components], the compact Hausdorff space $T^c$ (with
   the subspace topology) is extremally disconnected.
