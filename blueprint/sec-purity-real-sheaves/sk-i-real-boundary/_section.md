+++
id = "sk-i-real-boundary"
kind = "proposition"
title = "Boundary stalks and restriction to an open"
order = 2980
uses = ["sk-d-real-boundary", "sk-d-real-setup", "sk-d-real-weil"]
lean = ["AlgebraicGeometry.Scheme.isConstructibleSheaf_lowerStar", "AlgebraicGeometry.Scheme.isIso_unit_upperStarLowerStarAdjunction"]
tags = ["sketch"]
+++
In the situation of [sk-d-real-boundary]: for a finite ring $\Lambda$
and a finite locally constant sheaf $\mathcal F$ of $\Lambda$-modules on
$U_0$, the direct image $j_*\mathcal F$ is constructible (for this it
suffices that $C_0$ is a curve and $C_0\setminus U_0$ is finite); likewise,
for $\mathcal F$ lisse Weil, the sheaf $J=j_*\mathcal F$ is constructible,
and $J_{\bar s}=V_s^{I_s}$ equivariantly for Frobenius.
If $C_0$ is smooth, $U_0$ is dense, and $\mathcal G$ is a finite locally
constant sheaf of $\Lambda$-modules on $C_0$, then the adjunction unit
$\mathcal G\to j_*j^*\mathcal G$ is an isomorphism; likewise, if
$\mathcal G$ is lisse on all of $C_0$, then
$\mathcal G\simeq j_*(\mathcal G|_{U_0})$. The map
$\pi_1(U)\to\pi_1(C)$ is surjective, and hence so is the Weil-group map
of [sk-d-real-weil].
