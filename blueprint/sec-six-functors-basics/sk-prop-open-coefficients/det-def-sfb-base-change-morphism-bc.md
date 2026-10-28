+++
id = "det-def-sfb-base-change-morphism-bc"
kind = "definition"
title = "The base change morphism $\\mathrm{BC}_{sq}$ on $D_{\\mathrm{cons}}$"
order = 2734
uses = ["det-def-sfb-base-change-morphism-comparison", "def-sfb-dc-upper-lower-adjunction", "def-sfb-dc-lower-star"]
+++
In the situation of [det-def-sfb-base-change-morphism-comparison], assume moreover that the
derived pushforwards restrict to bounded constructible complexes ([def-sfb-dc-lower-star]; e.g.
$\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$), and let
$\eta'\colon\mathrm{Id}\Rightarrow Rf'_*Lf'^*$ be the unit of $Lf'^*\dashv Rf'_*$ and
$\varepsilon\colon Lf^*Rf_*\Rightarrow\mathrm{Id}$ the counit of $Lf^*\dashv Rf_*$
([def-sfb-dc-upper-lower-adjunction]). The *base change morphism* of the square is the natural
transformation of functors $D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$
$$
\mathrm{BC}_{sq}\colon Lg^*Rf_*\xrightarrow{\ \eta'_{Lg^*Rf_*}\ }Rf'_*Lf'^*Lg^*Rf_*\xrightarrow{\ Rf'_*(\theta_{sq})_{Rf_*}\ }Rf'_*Lg'^*Lf^*Rf_*\xrightarrow{\ Rf'_*Lg'^*\varepsilon\ }Rf'_*Lg'^* .
$$
No hypothesis that the square is cartesian is made.
