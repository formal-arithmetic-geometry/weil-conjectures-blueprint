+++
id = "prop-nagata-global-blowup-cover-independent"
kind = "theorem"
title = "The global blow-up map, its affine restrictions, and independence of the affine cover"
order = 64
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowup", "AlgebraicGeometry.Scheme.IdealSheafData.blowupMap", "AlgebraicGeometry.Scheme.IdealSheafData.blowupMap_preimage", "AlgebraicGeometry.Scheme.IdealSheafData.blowupι_blowupMap", "AlgebraicGeometry.Scheme.IdealSheafData.isPullback_blowupι"]
tags = ["latex:proposition"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-restrict", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be a quasi-coherent ideal. The blow-up
$\operatorname{Bl}_{\mathcal I}(X)$ comes with a morphism
$b_{X,\mathcal I}\colon\operatorname{Bl}_{\mathcal I}(X)\to X$ and, for
every affine open $V\subseteq X$, an open immersion
$\iota_V\colon\mathsf B_V(\mathcal I)\to\operatorname{Bl}_{\mathcal I}(X)$
such that:

1. $b_{X,\mathcal I}\circ\iota_V$ is the structure morphism
$\mathsf B_V(\mathcal I)\to V$ followed by the inclusion $V\subseteq X$;
2. $b_{X,\mathcal I}^{-1}(V)$ is the image of $\iota_V$;
3. the square formed by $\iota_V$, $b_{X,\mathcal I}$, the structure
morphism $\mathsf B_V(\mathcal I)\to V$ and the inclusion $V\subseteq X$
is cartesian; that is, $\iota_V$ identifies
$\operatorname{Bl}_{I_V}(V)$ with $b_{X,\mathcal I}^{-1}(V)$ over $V$.
