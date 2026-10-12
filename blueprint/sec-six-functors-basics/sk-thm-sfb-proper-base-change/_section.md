+++
id = "sk-thm-sfb-proper-base-change"
kind = "theorem"
title = "Proper base change on $D_{\\mathrm{cons}}$"
order = 1798
uses = ["sk-def-sfb-base-change-morphism"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl"]
tags = ["sketch"]
+++
Let $\Lambda$ be $\underline E$ for a finite extension $E$ of $\mathbf Q_\ell$
([sk-def-sfb-condensed-ring]) or $\Lambda=\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed]).
Consider a **cartesian** square of schemes and morphisms of the setting

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$

with $f$ **proper**. No hypothesis is imposed on $g$. Then the base change morphism of
[sk-def-sfb-base-change-morphism],

$$
\mathrm{BC}_{sq}\colon Lg^*\circ Rf_*\xrightarrow{\ \sim\ }Rf'_*\circ Lg'^*,
$$

is an isomorphism of functors $D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$.
