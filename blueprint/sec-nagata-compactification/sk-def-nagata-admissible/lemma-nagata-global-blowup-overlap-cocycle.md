+++
id = "lemma-nagata-global-blowup-overlap-cocycle"
kind = "lemma"
title = "Triple-overlap cocycle"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupOverlapIso_trans"]
order = 98
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-global-blowup-overlap-independent", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
Let $U$ be an affine open contained in the affine opens $V_i$, $V_j$ and
$V_k$. The overlap isomorphisms of
[def-nagata-global-blowup-overlap-basic-map] satisfy

$$
\omega_{jk,U}\circ\omega_{ij,U}=\omega_{ik,U}\colon
\mathsf B_{V_i}(\mathcal I)|_U\longrightarrow\mathsf B_{V_k}(\mathcal I)|_U.
$$
