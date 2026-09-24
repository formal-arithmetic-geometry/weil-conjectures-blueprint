+++
id = "lemma-nagata-proj-closed-center-finite-degree"
kind = "lemma"
title = "Properties of the finite-degree center data"
order = 301
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center_le_blowup"]
uses = ["def-nagata-global-blowup-cover-comparison", "def-nagata-proj-closed-center-finite-degree", "lemma-nagata-affine-image-kernel-flat", "lemma-nagata-extended-ideal-affine-chart", "lemma-nagata-proj-closed-center-finite-degree-exists", "lemma-nagata-scheme-image-flat-base-change", "prop-nagata-global-blowup-cover-independent"]
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
