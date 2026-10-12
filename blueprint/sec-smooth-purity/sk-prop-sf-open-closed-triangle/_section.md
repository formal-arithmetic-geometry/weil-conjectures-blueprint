+++
id = "sk-prop-sf-open-closed-triangle"
kind = "proposition"
title = "The open–closed triangle"
order = 2171
uses = ["sk-def-sf-setting"]
lean = ["AlgebraicGeometry.Etale.openClosedShortComplex", "AlgebraicGeometry.Etale.shortExact_openClosedShortComplex"]
tags = ["sketch"]
+++
Let $j:U\hookrightarrow X$ be an open immersion and $i:Z\hookrightarrow X$ a
closed immersion of schemes whose image is the complement of the image of
$j$. Let $\mathcal A$ be a Grothendieck abelian category of coefficients
which is concrete compatibly with filtered colimits and sheafification (for
instance $\Lambda$-modules, with the operations of
[sk-def-sf-operations]). For every sheaf $F$ on $X_{\Et}$ with values in
$\mathcal A$, the sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F\longrightarrow i_*i^*F
\longrightarrow0,
$$

whose first map is the counit of $j_!\dashv j^*$ and whose second map is
the unit of $i^*\dashv i_*$, is a complex, natural in $F$, and it is short
exact.
