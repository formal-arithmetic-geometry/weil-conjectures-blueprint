+++
id = "def-nagata-global-blowup-map"
kind = "definition"
title = "Global blow-up morphism"
order = 232
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupMap"]
uses = ["def-nagata-global-blowup", "def-nagata-global-blowup-local-model", "lemma-nagata-global-blowup-local-maps-agree"]
+++
Define

$$
b_{X,\mathcal I}\colon\operatorname{Bl}_{\mathcal I}(X)\longrightarrow X
$$

by gluing the local structure maps
$\mathsf B_{V_i}(\mathcal I)\to V_i\to X$. Their overlap equality is
[lemma-nagata-global-blowup-local-maps-agree], so the morphism-gluing
interface applies.
