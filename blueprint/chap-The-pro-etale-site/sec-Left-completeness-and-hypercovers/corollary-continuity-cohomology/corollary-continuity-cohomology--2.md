+++
id = "corollary-continuity-cohomology--2"
kind = "corollary"
title = "Continuity of cohomology (2)"
name_showing = false
order = 106002
aliases = ["bp-r029-2"]
lean = ["AlgebraicGeometry.ProEtale.preservesColimitsOfShape_rightDerived_lowerStar"]
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality"]
+++
Let $f:X\to Y$ be a quasi-compact and quasi-separated morphism of schemes,
and let $(F_i)_{i\in I}$ be a filtered diagram of abelian sheaves on
$X_{\mathrm{pro}\acute{e}t}$. For every $q\in\N$, the canonical map

$$
\varinjlim_i R^qf_*F_i\longrightarrow R^qf_*(\varinjlim_iF_i)
$$

is an isomorphism of abelian sheaves on $Y_{\mathrm{pro}\acute{e}t}$.

For $X$ and $Y$ in a universe $u$, the groups of sections are taken in
universe $u+1$, and $I$ is required to be equivalent to a category whose
objects and arrows lie in universe $u+1$.
