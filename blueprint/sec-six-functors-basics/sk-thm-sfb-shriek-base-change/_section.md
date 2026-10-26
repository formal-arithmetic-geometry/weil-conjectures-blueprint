+++
id = "sk-thm-sfb-shriek-base-change"
kind = "theorem"
title = "Base change for the lower shriek on $D_{\\mathrm{cons}}$"
order = 2578
uses = ["sk-def-sfb-shriek-base-change-morphism"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicAlgCl"]
tags = ["sketch"]
+++
Let $\Lambda$ be $\underline E$ for a finite extension $E$ of $\mathbf Q_\ell$
([det-def-sfb-condensed-ring]) or $\Lambda=\underline{\Qlb}$ ([det-def-sfb-qlbar-condensed]). For
every cartesian square

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$

of the setting and every compactification $c$ of $f$, the compact-support base change morphism
of [sk-def-sfb-shriek-base-change-morphism],

$$
\mathrm{Ex}_!^c\colon Lg^*\circ Rf_!^c\xrightarrow{\ \sim\ }Rf'^{\,c'}_!\circ Lg'^*,
$$

is an isomorphism of functors $D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$, with
$c'$ the base-changed compactification. No properness of $f$ is assumed.
