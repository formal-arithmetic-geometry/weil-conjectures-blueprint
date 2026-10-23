+++
id = "def-weil-pbc-proetale-operations"
kind = "definition"
title = "Derived operations on ringed pro-etale topoi"
order = 1043
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.lowerStar", "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction"]
uses = ["def-sp-kinjective-bridge", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site"]
+++
Let $\Lambda$ be a commutative condensed ring, and for a scheme $T$ let
$\Lambda_T$ be its pullback to the small pro-etale site of $T$ along the
canonical morphism from $T_{\Proet}$ to the point. Let $u:U\to V$ be a
morphism; the canonical coefficient morphism
$\alpha_u:u^{-1}\Lambda_V\to\Lambda_U$ is an isomorphism of ring sheaves. The
module inverse image is

$$
 u^*F=\Lambda_U\otimes_{u^{-1}\Lambda_V}u^{-1}F,
$$

the module direct image $u_*G$ is the sheaf direct image with $\Lambda_V$ acting
through the mate $\Lambda_V\to u_*\Lambda_U$ of $\alpha_u$, and
$u^*\dashv u_*$ on module sheaves. Their total derived functors, computed
on K-flat and on K-injective resolutions [def-sp-kinjective-bridge],
are triangulated functors

$$
 Lu^*:D(V_{\Proet},\Lambda_V)\longrightarrow D(U_{\Proet},\Lambda_U),
 \qquad
 Ru_*:D(U_{\Proet},\Lambda_U)\longrightarrow D(V_{\Proet},\Lambda_V),
$$

with $Lu^*\dashv Ru_*$. For a finite discrete ring $\Lambda$, $\Lambda_T$ is the
constant coefficient sheaf of [def-weil-pbc-proetale-modules].
