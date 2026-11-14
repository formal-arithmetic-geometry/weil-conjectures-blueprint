+++
id = "dag-det-pe-wlocal-strict-contractible"
kind = "dag-definition"
title = "w-strictly local and w-contractible rings"
name_showing = false
order = 43502
tags = ["sheaf-dag"]
split_from = "definition-w-local-w-strictly-local--2"
dag_id = "det-pe-wlocal-strict-contractible"
dag_kind = "definition"
dag_status = "imported"
serial = false
dag_lean = ["IsWLocalRing", "IsWStrictlyLocalRing", "IsWContractibleRing", "WLocalSpace.closedPointsHomeomorph"]
uses = ["dag-def-weil-pbc-w-local"]
+++
Let $R$ be a ring and $T=\operatorname{Spec}R$, a spectral space with set $T^c$ of closed
points (the maximal ideals of $R$).

1. $R$ is *w-local* if $T^c$ is closed in $T$ and every prime of $R$ is contained in exactly
   one maximal ideal. By `det-pe-wlocal-components` this agrees with
   [dag-def-weil-pbc-w-local]: $T^c$ closed and every connected component of $T$ has exactly
   one closed point.
2. $R$ is *w-strictly local* if it is w-local and, for every maximal ideal $\mathfrak m$,
   the local ring $R_{\mathfrak m}$ is strictly henselian
   `def-weil-pbc-henselian-terminology`.
3. $R$ is *w-contractible* if it is w-strictly local and the profinite space
   $\pi_0(T)$ of connected components (with the quotient topology from $T$) is
   extremally disconnected: the closure of every open subset of $\pi_0(T)$ is open.
   Equivalently, by `det-pe-wlocal-components`, the compact Hausdorff space $T^c$ (with
   the subspace topology) is extremally disconnected.

(SHEAF DAG node `det-pe-wlocal-strict-contractible`; machine-alignment layer.) Split from [definition-w-local-w-strictly-local--2]. DAG kind: definition. DAG status: imported.
