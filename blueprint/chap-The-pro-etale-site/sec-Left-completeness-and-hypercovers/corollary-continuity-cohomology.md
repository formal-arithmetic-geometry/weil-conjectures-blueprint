+++
id = "corollary-continuity-cohomology"
kind = "corollary"
title = "Continuity of cohomology"
order = 106
lean = ["AlgebraicGeometry.Scheme.ProEt.H_map_isColimit_of_isFiltered_small", "AlgebraicGeometry.ProEtale.preservesColimitsOfShape_rightDerived_lowerStar"]
+++
Suppose $U$ is quasi-compact and quasi-separated and
$(K_i^\bullet)$ is a filtered diagram of complexes of $\mathcal R$-modules
vanishing below one fixed degree $a$. Then for every $q$,

$$
\varinjlim_i H^q(U,K_i^\bullet)
\simeq H^q(U,\varinjlim_iK_i^\bullet).
$$

If $f:X\to Y$ is quasi-compact and quasi-separated, the analogous map
$\varinjlim_iR^qf_*K_i^\bullet\to
R^qf_*(\varinjlim_iK_i^\bullet)$ is an isomorphism.
