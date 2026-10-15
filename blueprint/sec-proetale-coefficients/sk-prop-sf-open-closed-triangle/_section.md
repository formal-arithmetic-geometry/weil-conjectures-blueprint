+++
id = "sk-prop-sf-open-closed-triangle"
kind = "proposition"
title = "Open–closed operations on module sheaves"
order = 738
uses = ["sk-def-sf-setting"]
lean = ["AlgebraicGeometry.Etale.openClosedShortComplex", "AlgebraicGeometry.Etale.shortExact_openClosedShortComplex"]
tags = ["sketch"]
+++
Let $X$ be quasi-compact and quasi-separated, $j:U\hookrightarrow X$ a
quasi-compact open immersion, and $i:Z\hookrightarrow X$ its closed
complement. For a sheaf of rings $B$ on $X_{\mathrm{proét}}$, use its inverse
images as the coefficient rings on $U$ and $Z$. Thus $i^*$ goes from
$B$-module sheaves on $X_{\mathrm{proét}}$ to $i^*B$-module sheaves on
$Z_{\mathrm{proét}}$, $i_*$ goes back, and $j^*$, $j_!$ relate $B$-module sheaves
on $X_{\mathrm{proét}}$ and $j^*B$-module sheaves on $U_{\mathrm{proét}}$.

Then $i^*$ is exact and preserves all small limits and colimits; $i_*$ is
exact and fully faithful. The functors $j^*$ and $j_!$ are exact, and every
$B$-module sheaf $M$ has the exact sequence

$$
0\longrightarrow j_!j^*M\longrightarrow M\longrightarrow i_*i^*M\longrightarrow0.
$$

Moreover $j_!$ preserves products and derived inverse limits of module
complexes. These operations commute with base change in their usual
open–closed squares.
