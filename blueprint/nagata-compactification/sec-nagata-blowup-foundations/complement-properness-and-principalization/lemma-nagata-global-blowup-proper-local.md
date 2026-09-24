+++
id = "lemma-nagata-global-blowup-proper-local"
kind = "lemma"
title = "Local properness of the global blow-up"
order = 249
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap_restrict"]
uses = ["def-nagata-global-blowup-cover-comparison", "lemma-nagata-affine-blowup-proper", "prop-nagata-global-blowup-affine-restrict", "prop-nagata-global-blowup-cover-independent"]
+++
If $\mathcal I$ is of finite type, the restriction of
$b_{X,\mathcal I}$ over every affine open of $X$ is proper.

## Proof

Finite type of $\mathcal I$ gives finite generation of the corresponding
ideal on the affine open. Transfer
[lemma-nagata-affine-blowup-proper] through
[prop-nagata-global-blowup-affine-restrict].
