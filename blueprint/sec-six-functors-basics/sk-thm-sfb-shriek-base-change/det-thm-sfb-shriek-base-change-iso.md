+++
id = "det-thm-sfb-shriek-base-change-iso"
kind = "theorem"
title = "$\\mathrm{Ex}_!^c$ is an isomorphism"
order = 2580
uses = ["det-thm-sfb-shriek-base-change-proper-step", "det-def-sfb-shriek-base-change-morphism-definition"]
+++
Let $\Lambda=\underline E$ for a finite extension $E$ of $\mathbf Q_\ell$ ([det-def-sfb-condensed-ring]),
or $\Lambda=\underline{\Qlb}$ ([det-def-sfb-qlbar-condensed]). For every cartesian square
$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$
of the setting and every compactification $c$ of $f$, with base-changed compactification $c'$ of
$f'$, the compact-support base change morphism
$$
\mathrm{Ex}_!^c\colon Lg^*\circ Rf_!^c\longrightarrow Rf'^{\,c'}_!\circ Lg'^*
$$
of [det-def-sfb-shriek-base-change-morphism-definition] is an isomorphism of functors
$D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$. No properness of $f$ is assumed.
