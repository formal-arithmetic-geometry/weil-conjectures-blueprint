+++
id = "sk-def-sfb-open-base-change"
kind = "definition"
title = "Base change for extension by zero on $D_{\\mathrm{cons}}$"
order = 1695
uses = ["sk-def-sfb-base-change-morphism"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriekBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriekBaseChangeIso"]
tags = ["sketch"]
+++
Work in the setting of [sk-def-sfb-dc-setting], and let $\Lambda$ be any commutative condensed
ring. Only the restricted functors $Lf^*$ and $j_!$ of [sk-def-sfb-dc-restricted-functors] enter,
and these exist for every $\Lambda$. Fix a commutative square of schemes and morphisms of the
setting

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle j'}\downarrow & & \downarrow{\scriptstyle j}\\
Z' & \xrightarrow{\;g\;} & Z
\end{array}
\qquad j\circ g'=g\circ j',
$$

with $j$ and $j'$ open immersions. The *extension-by-zero exchange morphism*

$$
\mathrm{Ex}^{j}_{sq}\colon j'_!\circ Lg'^*\longrightarrow Lg^*\circ j_!
$$

of functors $D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Z',\Lambda)$ is built, like the
base change morphism of [sk-def-sfb-base-change-morphism], from a unit, a square transport and
a counit:

$$
j'_!Lg'^*\xrightarrow{\ \eta\ }j'_!Lg'^*Lj^*j_!\xrightarrow[\ \sim\ ]{\ \theta\ }j'_!Lj'^*Lg^*j_!\xrightarrow{\ \varepsilon'\ }Lg^*j_!,
$$

with $\eta$ the unit of $j_!\dashv Lj^*$, $\theta\colon Lg'^*Lj^*\cong Lj'^*Lg^*$ the pullback
comparison of the square (read with its two diagonals exchanged), and $\varepsilon'$ the counit of
$j'_!\dashv Lj'^*$.

If the square is **cartesian**, then $\mathrm{Ex}^{j}_{sq}$ is an isomorphism. Its inverse is the
*extension-by-zero base change isomorphism*

$$
Lg^*\circ j_!\xrightarrow{\ \sim\ }j'_!\circ Lg'^*.
$$
