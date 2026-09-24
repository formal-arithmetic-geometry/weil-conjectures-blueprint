+++
id = "def-nagata-blowup-universal-lift"
kind = "definition"
title = "Universal lift construction"
order = 351
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-universal-graded-map", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-relative-proj", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-sheaf-rees-algebra", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-relative-proj-base-change-arbitrary", "lemma-nagata-relative-proj-invertible-tensor-powers", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
Under the data of
[def-nagata-blowup-universal-graded-map], use the inverse of the canonical isomorphism in
[lemma-nagata-relative-proj-invertible-tensor-powers], apply the
contravariant relative-Proj map induced by $\alpha_f$. Then use the
arbitrary base-change comparison in
[lemma-nagata-relative-proj-base-change-arbitrary] to identify the
resulting target with $Y\times_X\operatorname{Bl}_{\mathcal I}(X)$. Here
$\operatorname{Proj}_X(\mathcal R_X(\mathcal I))$ is identified with
[def-nagata-global-blowup]: both are obtained by gluing the same affine
Rees-algebra Proj schemes, and the comparison respects the restriction
cocycles. Compose
the resulting map with the second projection
$Y\times_X\operatorname{Bl}_{\mathcal I}(X)\to \operatorname{Bl}_{\mathcal I}(X)$, and
define

$$
\widetilde f\colon Y\longrightarrow\operatorname{Bl}_{\mathcal I}(X)
$$

to be the resulting composite. The affine maps and their gluing data are
part of the relative-Proj interface; no identification of $Y$ with a Proj
is left implicit.
