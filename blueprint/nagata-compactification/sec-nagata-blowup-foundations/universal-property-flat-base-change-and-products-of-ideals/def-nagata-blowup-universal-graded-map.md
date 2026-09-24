+++
id = "def-nagata-blowup-universal-graded-map"
kind = "definition"
title = "Graded map induced by an invertible quotient"
order = 347
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-sheaf-rees-algebra", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
Let $f\colon Y\to X$, let $\mathcal I\subseteq\mathcal O_X$ be a
quasi-coherent ideal, and let
$\mathcal L\hookrightarrow\mathcal O_Y$ be an invertible ideal together with
a surjection $q\colon f^*\mathcal I\twoheadrightarrow\mathcal L$ such that
the composite $\mathcal L\hookrightarrow\mathcal O_Y$ after $q$ is the
canonical map whose image is the extended ideal
$\mathcal I\mathcal O_Y$ of
[def-nagata-extended-ideal]. Define $\alpha_f$ degreewise by the
tensor powers of this quotient:

$$
\alpha_f\colon
f^*\Bigl(\bigoplus_{n\geq0}\mathcal I^n\Bigr)
\longrightarrow\bigoplus_{n\geq0}\mathcal L^{\otimes n}.
$$
