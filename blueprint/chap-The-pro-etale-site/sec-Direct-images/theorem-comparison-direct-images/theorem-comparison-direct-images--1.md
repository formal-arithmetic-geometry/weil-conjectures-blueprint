+++
id = "theorem-comparison-direct-images--1"
kind = "theorem"
title = "Underived comparison and acyclicity"
name_showing = false
order = 133001
aliases = ["bp-r038-1"]
lean = ["AlgebraicGeometry.ProEtale.lowerStarComparisonUpperStarBaseChange", "AlgebraicGeometry.ProEtale.isIso_lowerStarComparisonUpperStarBaseChange", "AlgebraicGeometry.ProEtale.rightAcyclic_lowerStar_comparisonUpperStar_obj_of_injective"]
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and let
$g:X\to Y$ be a morphism of schemes. There is a canonical natural
transformation on sheaves with values in $\mathcal A$

$$
c_g^0:\nu_Y^*g_{\acute{e}t,*}\longrightarrow
g_{\mathrm{pro}\acute{e}t,*}\nu_X^*.
$$

If $g$ is quasi-compact and quasi-separated, $c_g^0$ is an
isomorphism. Moreover, for every injective sheaf $I$ with values in
$\mathcal A$ on $X_{\acute{e}t}$, the sheaf $\nu_X^*I$ is acyclic for
$g_{\mathrm{pro}\acute{e}t,*}$:

$$
R^qg_{\mathrm{pro}\acute{e}t,*}\nu_X^*I=0\qquad(q>0).
$$
