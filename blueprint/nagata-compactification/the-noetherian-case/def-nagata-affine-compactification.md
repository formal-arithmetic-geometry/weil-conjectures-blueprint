+++
id = "def-nagata-affine-compactification"
kind = "definition"
title = "Affine compactification construction"
order = 507
lean = ["AlgebraicGeometry.Compactification.ofIsImmersionAffineSpace"]
uses = ["def-nagata-immersion-compactification", "def-nagata-quasi-affine-immersion-affine-space", "def-nagata-relative-affine-space", "def-nagata-relative-projective-space"]
+++
Let $U\to S$ be quasi-compact and of finite type and let
$\iota_U\colon U\to\mathbb A^n_S$ be an immersion over $S$, as supplied by
[def-nagata-quasi-affine-immersion-affine-space] when $U$ is
quasi-affine. Compose $\iota_U$ with the standard open immersion
$\mathbb A^n_S\hookrightarrow\mathbb P^n_S$ and define

$$
\mathsf C_{\mathrm{aff}}(U/S)
=\mathsf C\bigl(U\longrightarrow\mathbb P^n_S\bigr)
$$

using [def-nagata-immersion-compactification].
