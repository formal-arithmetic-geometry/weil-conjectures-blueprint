+++
id = "lemma-nagata-global-blowup-proper-local"
kind = "lemma"
title = "Local properness of the global blow-up"
order = 319
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap_restrict"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-affine-blowup-proper", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-global-blowup-affine-restrict", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
If $\mathcal I$ is of finite type, the restriction of
$b_{X,\mathcal I}$ over every affine open of $X$ is proper.

## Proof

Finite type of $\mathcal I$ gives finite generation of the corresponding
ideal on the affine open. Transfer
[lemma-nagata-affine-blowup-proper] through
[prop-nagata-global-blowup-affine-restrict].
