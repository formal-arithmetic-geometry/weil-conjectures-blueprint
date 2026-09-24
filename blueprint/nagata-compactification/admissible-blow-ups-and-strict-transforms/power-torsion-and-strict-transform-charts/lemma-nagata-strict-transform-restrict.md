+++
id = "lemma-nagata-strict-transform-restrict"
kind = "lemma"
title = "Strict transform over the complement of the center"
order = 348
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isPullback_strictTransform_over_blowupMap"]
uses = ["def-nagata-global-blowup-cover-comparison", "def-nagata-strict-transform", "lemma-nagata-strict-transform-over-complement", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X'\to X$ be the blow-up of a center $C\hookrightarrow X$. Over
$X\setminus C$, the strict transform is canonically the ordinary pullback.
This identification is compatible with the projection to the original
scheme.

## Proof

This is exactly
[lemma-nagata-strict-transform-over-complement], applied to the ideal
defining $C$. The compatibility with the projection is part of that
canonical identification.
