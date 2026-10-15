+++
id = "sk-def-pe-site"
kind = "definition"
title = "The small pro-étale site"
order = 703
uses = ["sk-def-pe-morphisms", "sk-lem-pe-weakly-etale-stability"]
tags = ["sketch"]
+++
The objects of $X_{\mathrm{proét}}$ are weakly étale $X$-schemes [sk-def-pe-morphisms],
with all $X$-morphisms as arrows (these are weakly étale by
[sk-lem-pe-weakly-etale-stability]). A family $\{U_i\to U\}_{i\in I}$ is a covering if it
is an fpqc covering. Explicitly, for every affine open $W\subset U$ there must be finitely
many indices $i_1,\ldots,i_m$ and affine opens $V_j\subset U_{i_j}\times_UW$ with

$$
W=\bigcup_{j=1}^m\operatorname{image}(V_j\to W).
$$

The indices may depend on $W$; no finiteness of $I$ is required. Equivalently one may use
finitely many quasi-compact opens above each $W$. See Stacks, Tags 0989 and 098A.

The finite refinement condition is part of the topology; a jointly surjective family
without it is not a covering. For an affine target every cover refines to a finite affine
cover, whose disjoint union is affine and faithfully flat over the target. Ordinary étale
and Zariski covers are pro-étale covers: flat maps locally of finite presentation are open,
so quasi-compactness gives the required finite refinements (Stacks, Tag 098B).
