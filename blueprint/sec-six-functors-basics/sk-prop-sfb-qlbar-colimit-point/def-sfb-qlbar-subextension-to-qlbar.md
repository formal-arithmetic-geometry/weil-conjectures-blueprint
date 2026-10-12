+++
id = "def-sfb-qlbar-subextension-to-qlbar"
kind = "definition"
title = "The inclusions $\\underline E\\to\\underline{\\overline{\\mathbf Q}}_\\ell$"
order = 1528
uses = ["def-sfb-padic-subfield-condensed-ring", "def-sfb-qlbar-subextension-map", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-ring-object"]
lean = ["Profinite.padicSubfieldRingObjToPadicAlgCl"]
+++
For a finite subextension $E$ of $\Qlb/\mathbf Q_\ell$, let
$j_E\colon\underline E\to\underline{\Qlb}$ be the morphism of condensed rings
([def-sfb-padic-subfield-condensed-ring], [sk-def-sfb-qlbar-condensed]) given by

$$
C(S,E)\ni a\longmapsto\bigl(S\xrightarrow{a}E\subseteq\Qlb\bigr)\in\underline{\Qlb}(S),
$$

viewed as a morphism of the underlying ring objects ([sk-def-sfb-ring-object]). For
$E\subseteq F$, these maps satisfy $j_F\circ\iota_{E,F}=j_E$, with $\iota_{E,F}$ as in
[def-sfb-qlbar-subextension-map].
