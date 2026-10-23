+++
id = "sk-def-sfb-base-change-morphism"
kind = "definition"
title = "The base change morphism on $D_{\\mathrm{cons}}$"
order = 2586
uses = ["sk-def-sfb-dc-restricted-functors"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructiblePullbackSquareComparison", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleBaseChangeUnitStep", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleBaseChangeSquareStep", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleBaseChangeCounitStep", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleBaseChange"]
tags = ["sketch"]
+++
Work in the setting of [sk-def-sfb-dc-setting]. Let $\Lambda$ be a commutative condensed ring for
which the derived pushforwards restrict to bounded constructible complexes
([sk-def-sfb-dc-restricted-functors]; for instance $\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$).
Fix a commutative square of schemes and morphisms of the setting

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
\qquad f\circ g'=g\circ f'.
$$

All functors below are the restricted functors on $D_{\mathrm{cons}}(-,\Lambda)$ of
[sk-def-sfb-dc-restricted-functors].

The *pullback comparison* of the square is the natural isomorphism

$$
\theta_{sq}\colon Lf'^*\circ Lg^*\cong L(g\circ f')^*=L(f\circ g')^*\cong Lg'^*\circ Lf^*,
$$

built from the two composition isomorphisms and the commutativity of the square.

The *base change morphism* $\mathrm{BC}_{sq}\colon Lg^*\circ Rf_*\to Rf'_*\circ Lg'^*$ of functors
$D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$ is the composite of three steps:

$$
Lg^*Rf_*\xrightarrow{\ \eta'\ }Rf'_*Lf'^*Lg^*Rf_*\xrightarrow[\ \sim\ ]{\ \theta_{sq}\ }Rf'_*Lg'^*Lf^*Rf_*\xrightarrow{\ \varepsilon\ }Rf'_*Lg'^*.
$$

The first step inserts the unit $\eta'$ of $Lf'^*\dashv Rf'_*$. The second transports along
$\theta_{sq}$. The third contracts the counit $\varepsilon$ of $Lf^*\dashv Rf_*$. No hypothesis on
the square (such as being cartesian) or on $\Lambda$ beyond the above enters the definition.
