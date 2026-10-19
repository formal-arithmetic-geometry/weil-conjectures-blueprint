+++
id = "def-nagata-affine-compactification"
kind = "definition"
title = "Affine compactification construction"
order = 318
lean = ["AlgebraicGeometry.Compactification.ofIsImmersionAffineSpace"]
uses = ["def-nagata-affine-proj", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-immersion-compactification", "def-nagata-projective-space-base-change", "def-nagata-quasi-affine-immersion-affine-space", "def-nagata-relative-affine-space", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-relative-affine-space-open-immersion"]
+++
Let $U\to S$ be quasi-compact and let
$\iota_U\colon U\to\mathbb A^n_S$ be an immersion over $S$ into relative
affine space with finitely many coordinates, as supplied by
[def-nagata-quasi-affine-immersion-affine-space] when $U$ is
quasi-affine. Compose $\iota_U$ with the standard open immersion
$\mathbb A^n_S\hookrightarrow\mathbb P^n_S$ and define

$$
\mathsf C_{\mathrm{aff}}(U/S)
=\mathsf C\bigl(U\longrightarrow\mathbb P^n_S\bigr)
$$

using [def-nagata-immersion-compactification].
