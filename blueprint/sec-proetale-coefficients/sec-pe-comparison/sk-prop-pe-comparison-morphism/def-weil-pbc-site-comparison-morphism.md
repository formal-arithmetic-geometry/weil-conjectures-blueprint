+++
id = "def-weil-pbc-site-comparison-morphism"
kind = "definition"
title = "The comparison morphism of sites"
order = 1004
lean = ["AlgebraicGeometry.Scheme.toProEt", "AlgebraicGeometry.ProEtale.comparisonLowerStar", "AlgebraicGeometry.ProEtale.comparisonUpperStar", "AlgebraicGeometry.ProEtale.comparisonAdjunction"]
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-proetale-site"]
+++
For a scheme $T$, the inclusion of etale $T$-schemes into weakly etale
$T$-schemes is continuous and preserves finite limits. It defines a geometric
morphism

$$
 \nu_T:T_{\Proet}\longrightarrow T_{\Et},
 \qquad
 \nu_T^*:\Sh(T_{\Et})\rightleftarrows
 \Sh(T_{\Proet}):\nu_{T,*}.
$$

Here $\nu_{T,*}$ is restriction to the etale subsite, $(\nu_{T,*}G)(V)=G(V)$
for $V$ etale over $T$, and $\nu_T^*$ is its left adjoint: the left Kan
extension of presheaves along the inclusion, followed by sheafification. For
any ring $\Lambda$, the same construction gives an adjunction
$\nu_T^*\dashv\nu_{T,*}$ between sheaves of $\Lambda$-modules on the two sites.
