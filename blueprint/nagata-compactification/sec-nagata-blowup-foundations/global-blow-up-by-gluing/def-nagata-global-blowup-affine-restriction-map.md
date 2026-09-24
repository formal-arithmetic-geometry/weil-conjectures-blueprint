+++
id = "def-nagata-global-blowup-affine-restriction-map"
kind = "definition"
title = "Affine-restriction comparison for the global blow-up"
order = 307
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupMap_preimage"]
uses = ["def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "lemma-nagata-rees-generators-cover-proj", "prop-nagata-proj-standard-open"]
+++
If $V=\operatorname{Spec}(A)\subseteq X$ and $I_V$ represents
$\mathcal I|_V$, define

$$
q_V\colon b_{X,\mathcal I}^{-1}(V)\longrightarrow
\operatorname{Bl}_{I_V}(\operatorname{Spec}A)
$$

by gluing the affine restriction maps on the basic intersections of $V$
with the chosen affine cover of $X$.
