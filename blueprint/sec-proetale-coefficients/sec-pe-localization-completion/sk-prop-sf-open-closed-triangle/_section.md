+++
id = "sk-prop-sf-open-closed-triangle"
kind = "proposition"
title = "Extension by zero and restriction to a closed subscheme"
order = 119
lean = ["AlgebraicGeometry.ProEtale.isIso_upperStarLowerStarAdjunction_counit", "AlgebraicGeometry.ProEtale.preservesFiniteColimits_lowerStar_of_isCompl", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_and_preservesFiniteColimits_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.isIso_of_isIso_upperStar_of_isCompl", "AlgebraicGeometry.ProEtale.isIso_openImmersionLowerShriekBaseChangeMap"]
tags = ["sketch"]
+++
Let $X$ be quasi-compact and quasi-separated, $j:U\hookrightarrow X$
a quasi-compact open immersion, and $i:Z\hookrightarrow X$ its
closed complement. For a sheaf of rings $\mathcal R$ on $X_{\mathrm{pro}\acute{e}t}$, we use its
inverse images as the coefficient rings on $U$ and $Z$. Thus
$i^*$ goes from $\mathcal R$-module sheaves on $X_{\mathrm{pro}\acute{e}t}$ to $i^*\mathcal R$-module
sheaves on $Z_{\mathrm{pro}\acute{e}t}$, $i_*$ goes back, and $j^*$, $j_!$ relate
$\mathcal R$-module sheaves on $X_{\mathrm{pro}\acute{e}t}$ and $j^*\mathcal R$-module sheaves on
$U_{\mathrm{pro}\acute{e}t}$.
Then $i^*$ is exact and preserves all small limits and colimits;
$i_*$ is exact and fully faithful. The functors $j^*$ and $j_!$ are
exact, and every $\mathcal R$-module sheaf $M$ has the exact sequence

$$
0\longrightarrow j_!j^*M\longrightarrow M
\longrightarrow i_*i^*M\longrightarrow0.
$$

Moreover $j_!$ preserves products and derived inverse limits of
module complexes. These functors commute with base change along any
morphism $X'\to X$, with $U$ and $Z$ replaced by their inverse images.
