+++
id = "def-nagata-global-blowup-affine-restriction-map"
kind = "definition"
title = "Affine-restriction comparison for the global blow-up"
order = 307
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupMap_preimage"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
If $V=\operatorname{Spec}(A)\subseteq X$ and $I_V$ represents
$\mathcal I|_V$, define

$$
q_V\colon b_{X,\mathcal I}^{-1}(V)\longrightarrow
\operatorname{Bl}_{I_V}(\operatorname{Spec}A)
$$

by gluing the affine restriction maps on the basic intersections of $V$
with the chosen affine cover of $X$.
