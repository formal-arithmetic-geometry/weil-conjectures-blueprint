+++
id = "def-sfb-qlbar-subextension-to-qlbar"
kind = "definition"
title = "The inclusions $\\underline E\\to\\underline{\\overline{\\mathbf Q}}_\\ell$"
order = 1242
uses = ["def-sfb-padic-subfield-condensed-ring", "def-sfb-qlbar-subextension-map", "det-def-sfb-qlbar-condensed", "det-def-sfb-ring-object"]
lean = ["Profinite.padicSubfieldCondensedRingToPadicAlgCl", "Profinite.padicSubfieldRingObjToPadicAlgCl", "Profinite.padicSubfieldRingObjMap_comp_toPadicAlgCl"]
+++
For a finite subextension $E$ of $\Qlb/\mathbf Q_\ell$, let
$j_E\colon\underline E\to\underline{\Qlb}$ be the morphism of condensed rings
([def-sfb-padic-subfield-condensed-ring], [det-def-sfb-qlbar-condensed]) given by

$$
C(S,E)\ni a\longmapsto\bigl(S\xrightarrow{a}E\subseteq\Qlb\bigr)\in\underline{\Qlb}(S),
$$

viewed as a morphism of the underlying ring objects ([det-def-sfb-ring-object]). For
$E\subseteq F$, these maps satisfy $j_F\circ\iota_{E,F}=j_E$, with $\iota_{E,F}$ as in
[def-sfb-qlbar-subextension-map].
