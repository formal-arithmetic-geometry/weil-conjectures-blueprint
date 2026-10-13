+++
id = "sk-def-sfb-shriek-base-change-morphism"
kind = "definition"
title = "Compact-support base change morphism $\\mathrm{Ex}_!^c$"
order = 1807
uses = ["sk-def-nagata-sketch-data", "sk-def-sfb-dc-lower-shriek", "sk-def-sfb-open-base-change", "sk-prop-nagata-sketch-comp-category"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange"]
tags = ["sketch"]
+++
Work in the setting of [sk-def-sfb-dc-setting], with $\Lambda$ as in [sk-def-sfb-dc-lower-shriek].
Fix a **cartesian** square of schemes and morphisms of the setting

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$

and a compactification $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$ of $f$
([sk-def-nagata-sketch-data]). Its *base change*
([sk-prop-nagata-sketch-comp-category]) is the compactification

$$
c'=\bigl(X'\xrightarrow{\ i'\ }Z':=Z\times_YY'\xrightarrow{\ p'\ }Y'\bigr)
$$

of $f'$. Here $p'$ is the second projection, and $i'$ is induced by $i\circ g'$ and $f'$. Writing
$\bar g\colon Z'\to Z$ for the first projection, both squares

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle i'}\downarrow & & \downarrow{\scriptstyle i}\\
Z' & \xrightarrow{\;\bar g\;} & Z
\end{array}
\qquad\qquad
\begin{array}{ccc}
Z' & \xrightarrow{\;\bar g\;} & Z\\
{\scriptstyle p'}\downarrow & & \downarrow{\scriptstyle p}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$

are cartesian. The *compact-support base change morphism*

$$
\mathrm{Ex}_!^c\colon Lg^*\circ Rf_!^c\longrightarrow Rf'^{\,c'}_!\circ Lg'^*
$$

of functors $D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$, with $Rf_!^c=Rp_*\circ i_!$
and $Rf'^{\,c'}_!=Rp'_*\circ i'_!$ as in [sk-def-sfb-dc-lower-shriek], is the composite

$$
Lg^*Rp_*i_!\xrightarrow{\ \mathrm{BC}\ }Rp'_*L\bar g^*i_!\xrightarrow[\ \sim\ ]{\ (\mathrm{Ex}^{j})^{-1}\ }Rp'_*i'_!Lg'^*.
$$

The first map is the base change morphism of [sk-def-sfb-base-change-morphism] for the proper
square, whiskered by $i_!$. The second applies $Rp'_*$ to the extension-by-zero base change
isomorphism of [sk-def-sfb-open-base-change] for the cartesian open square. All statements are
relative to the explicit compactification $c$. Independence of $c$ is not asserted.
