+++
id = "def-pc-euler-characteristic"
kind = "definition"
title = "The Euler characteristic"
order = 4253
lean = ["AlgebraicGeometry.eulerCharacteristic"]
uses = ["def-pc-scheme", "def-pc-derived-direct-image", "def-pc-morphism-conventions", "lem-pc-euler-characteristic-well-defined"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$ and $\mathcal{F}$ a
coherent $\mathcal{O}_X$-module. The *Euler characteristic* of
$\mathcal{F}$ is
$$
\chi(X,\mathcal{F}):=\sum_i(-1)^i\dim_kH^i(X,\mathcal{F})\in\Z ,
$$
where $H^i(X,\mathcal{F})$ are the higher direct images
[def-pc-derived-direct-image] of $\mathcal{F}$ for the structure morphism.
That the sum is finite — the cohomology being finite-dimensional and
vanishing above the dimension — is
[lem-pc-euler-characteristic-well-defined], as
[rem-ptr-pc-euler-characteristic-13] records.

*Import note.* The source's sentence breaks off at a semicolon and the
definition then closes; it is completed with the cross-reference the
pointer remark supplies, and nothing else is added.
