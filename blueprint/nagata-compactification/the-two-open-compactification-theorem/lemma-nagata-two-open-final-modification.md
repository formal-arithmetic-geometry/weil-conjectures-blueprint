+++
id = "lemma-nagata-two-open-final-modification"
kind = "lemma"
title = "Structural properties of the final common modification"
order = 560
lean = ["AlgebraicGeometry.nonempty_commonModification"]
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-admissible-blowup", "def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-blowup-universal-graded-map", "def-nagata-blowup-universal-lift", "def-nagata-common-modification", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-effective-cartier-ideal", "def-nagata-elimination-indeterminacy", "def-nagata-extended-admissible-blowup", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "def-nagata-two-open-final-modification", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-affine-blowup-complement", "lemma-nagata-blowup-proper", "lemma-nagata-blowup-universal-exists", "lemma-nagata-blowup-universal-graded-map", "lemma-nagata-blowup-universal-unique", "lemma-nagata-common-modification", "lemma-nagata-diagonal-base-change", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-intermediate-separated", "lemma-nagata-localization-ideal-pow", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-product-ideal-common-blowup", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-scheme-image-partial-section", "lemma-nagata-separated-two-open-cover", "lemma-nagata-strict-transform-closure-characterization", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-proper", "thm-nagata-strict-transform-is-blowup"]
+++
Each $W'_i\to W_i$ is $U$-admissible; the maps $W'_i\hookrightarrow W$
are open immersions covering $W$; their copies of $U$ agree; and $W\to S$
is separated and of finite type. In particular the induced map
$j_W\colon U\to W$ is an open immersion.

## Proof

The schemes $W_i$ are separated and of finite type by
[lemma-nagata-intermediate-separated]. Thus all hypotheses of the
common-modification property apply, and
[lemma-nagata-common-modification] gives every stated assertion.
The map $j_W$ is the composite of $U\hookrightarrow W'_i$ with either open
immersion $W'_i\hookrightarrow W$; the two composites coincide by the
gluing construction.
