+++
id = "sbc-lem-identity-and-base-change-composition"
kind = "lemma"
title = "Identity and base-change composition"
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id"]
order = 2093
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "lem-weil-pbc-exchange-identity-pasting"]
+++
For a cartesian square of
the proper-base-change chapter with $g=\operatorname{id}_Y$, the derived exchange
morphism of [def-weil-pbc-derived-exchange] is the identity. If
$Y''\xrightarrow{h}Y'\xrightarrow{g}Y$, then, after the canonical
associativity identifications, the derived exchange morphism for the
composite base change $g\circ h$ is

$$
Lh^*Lg^{-1}Rf_*\xrightarrow{Lh^*\operatorname{BC}_{f,g}}
Lh^*Rf'_*Lv^{-1}\xrightarrow{\operatorname{BC}_{f',h}}
Rf''_*L(v\circ v')^{-1},
$$

where $v:X'\to X$, $v':X''\to X'$ are the top morphisms of the two
squares.
