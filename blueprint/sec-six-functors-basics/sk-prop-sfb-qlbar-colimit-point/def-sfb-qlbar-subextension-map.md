+++
id = "def-sfb-qlbar-subextension-map"
kind = "definition"
title = "The inclusions $\\underline E\\to\\underline F$"
order = 1476
uses = ["def-sfb-continuous-map-condensed-ring-map", "def-sfb-padic-subfield-condensed-ring", "sk-def-sfb-qlbar-condensed"]
lean = ["Profinite.padicSubfieldRingObjMap"]
+++
Let $E\subseteq F$ be finite subextensions of $\Qlb/\mathbf Q_\ell$
([sk-def-sfb-qlbar-condensed]), with the topologies restricted from $\Qlb$, and let
$\underline E$, $\underline F$ be their condensed rings
([def-sfb-padic-subfield-condensed-ring]). The morphism
$\iota_{E,F}\colon\underline E\to\underline F$ is postcomposition with the inclusion
$E\subseteq F$ ([def-sfb-continuous-map-condensed-ring-map]), viewed as a morphism of the
underlying ring objects of $\Sh(*_{\mathrm{proét}},\Ab)$. It is strictly functorial:
$\iota_{E,E}=\mathrm{id}$, and $\iota_{F,H}\circ\iota_{E,F}=\iota_{E,H}$ for
$E\subseteq F\subseteq H$.
