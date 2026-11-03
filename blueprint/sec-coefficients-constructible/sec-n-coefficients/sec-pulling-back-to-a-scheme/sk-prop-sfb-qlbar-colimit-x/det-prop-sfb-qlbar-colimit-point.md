+++
id = "det-prop-sfb-qlbar-colimit-point"
kind = "proposition"
title = "$\\underline{\\overline{\\mathbf Q}}_\\ell=\\operatorname{colim}_E\\underline E$ on the point"
order = 1243
uses = ["det-def-sfb-qlbar-condensed", "det-def-sfb-condensed-ring", "def-sfb-qlbar-subextension-map", "def-sfb-qlbar-subextension-to-qlbar"]
lean = ["Profinite.padicSubfieldRingObjMap", "Profinite.padicSubfieldRingObjToPadicAlgCl", "Profinite.padicSubfieldRingObjFunctor", "Profinite.padicAlgClRingObjCocone", "Profinite.isColimitPadicAlgClRingObjCocone"]
+++
Let $\mathcal E$ be the filtered poset of finite subextensions $E$ of $\Qlb/\mathbf Q_\ell$
([det-def-sfb-qlbar-condensed]). Give each $E$ the topology restricted from $\Qlb$, and let
$\underline E=C(-,E)$ be its condensed ring ([det-def-sfb-condensed-ring]). For
$E\subseteq F$, postcomposition with the inclusion gives a morphism of ring objects
$\underline E\to\underline F$. This makes $E\mapsto\underline E$ a functor
$\mathcal E\to\Sh(*_{\mathrm{proét}},\Ab)$. Postcomposition with $E\subseteq\Qlb$ gives
morphisms of ring objects $\underline E\to\underline{\Qlb}$, and these are compatible
with the maps $\underline E\to\underline F$.

The resulting cocone is a colimit in $\Sh(*_{\mathrm{proét}},\Ab)$:

$$
\colim_{E\in\mathcal E}\underline E\xrightarrow{\ \sim\ }\underline{\Qlb}.
$$

This identity is a theorem; $\underline{\Qlb}$ itself is defined by its sections.
