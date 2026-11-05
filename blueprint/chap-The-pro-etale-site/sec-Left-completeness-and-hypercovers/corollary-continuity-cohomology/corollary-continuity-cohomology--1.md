+++
id = "corollary-continuity-cohomology--1"
kind = "corollary"
title = "Continuity of cohomology (1)"
name_showing = false
order = 106001
aliases = ["bp-r029-1"]
lean = ["AlgebraicGeometry.Scheme.ProEt.H_map_isColimit_of_isFiltered_small"]
uses = ["definition-small-pro-etale-site"]
+++
Suppose $U$ is a quasi-compact and quasi-separated scheme and
$(F_i)_{i\in I}$ is a small filtered diagram of abelian sheaves on
$U_{\mathrm{pro}\acute{e}t}$. Then for every $q\in\N$, the canonical map

$$
\varinjlim_i H^q(U,F_i)
\longrightarrow H^q(U,\varinjlim_iF_i)
$$

is an isomorphism. More explicitly, every class on the right comes from
$H^q(U,F_i)$ for some $i$, and a class in $H^q(U,F_i)$ whose image is zero
becomes zero after some arrow $i\to j$ in $I$.

For $U$ in a universe $u$, the groups of sections and the objects and
arrows of $I$ are taken in universe $u+1$.
