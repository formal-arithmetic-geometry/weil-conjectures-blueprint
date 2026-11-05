+++
id = "corollary-continuity-cohomology--1"
kind = "corollary"
title = "Continuity of cohomology (1)"
name_showing = false
order = 106001
aliases = ["bp-r029-1"]
lean = ["AlgebraicGeometry.Scheme.ProEt.H_map_isColimit_of_isFiltered_small"]
uses = ["definition-small-pro-etale-site--1"]
+++
Suppose $U$ is quasi-compact and quasi-separated and
$(K_i^\bullet)$ is a filtered diagram of complexes of $\mathcal R$-modules
vanishing below one fixed degree $a$. Then for every $q$,

$$
\varinjlim_i H^q(U,K_i^\bullet)
\simeq H^q(U,\varinjlim_iK_i^\bullet).
$$
