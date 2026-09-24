+++
id = "lemma-nagata-proj-closed-center-finite-degree"
kind = "lemma"
title = "Properties of the finite-degree center data"
order = 393
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center_le_blowup"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-proj-closed-center-finite-degree", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-affine-image-kernel-flat", "lemma-nagata-affine-image-kernel-localization", "lemma-nagata-chart-extended-ideal-principal", "lemma-nagata-diagonal-base-change", "lemma-nagata-extended-ideal-affine-chart", "lemma-nagata-finite-type-ideal-extension-exists", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-proj-closed-center-finite-degree-exists", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-scheme-image-flat-base-change", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
The selected integer $d(Z')$ is positive, $\mathcal F(Z')$ is a finite
type submodule of $\mathcal I^{d(Z')}$, and

$$
Z'=\operatorname{Proj}_X
\bigl(\mathcal A/\mathcal F(Z')\mathcal A\bigr).
$$

Moreover the support of
$\mathcal I^{d(Z')}/\mathcal F(Z')$ lies over the underlying topological
image $b(|Z'|)$ together with the first center.

## Proof

These are the properties required of the witness selected in
[def-nagata-proj-closed-center-finite-degree]; existence of such a
witness is
[lemma-nagata-proj-closed-center-finite-degree-exists].
