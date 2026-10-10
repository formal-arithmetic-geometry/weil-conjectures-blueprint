+++
id = "prop-nagata-affine-compactification"
kind = "theorem"
title = "Property of the affine compactification construction"
order = 312
lean = ["AlgebraicGeometry.HasCompactification.of_isQuasiAffine"]
tags = ["latex:proposition"]
uses = ["def-nagata-affine-compactification", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-relative-affine-space", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-nagata-immersion-into-proper", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-quasi-affine-immersion-affine-space", "lemma-nagata-quasi-affine-immersion-affine-space-exists", "lemma-nagata-relative-affine-space-open-immersion"]
+++
If $U$ is a quasi-affine scheme and $U\to S$ is quasi-compact and locally
of finite type, then $U\to S$ is compactifiable; this applies in particular
when $U$ is affine.

## Proof

By [lemma-nagata-quasi-affine-immersion-affine-space-exists] and
[lemma-nagata-quasi-affine-immersion-affine-space] there are a finite
$n$ and an immersion $\iota_U\colon U\to\mathbb A^n_S$ over $S$. Its
composite with the standard open immersion
$\mathbb A^n_S\hookrightarrow\mathbf P(\{0\}\sqcup n;S)$ of
[lemma-nagata-relative-affine-space-open-immersion] is an immersion
$g\colon U\to\mathbf P(\{0\}\sqcup n;S)$ over $S$, and
$\mathbf P(\{0\}\sqcup n;S)\to S$ is proper by
[lemma-nagata-projective-space-base-change-proper]. The composite
$U\to S$ is quasi-compact by hypothesis. Hence
[lemma-nagata-immersion-into-proper] applies: $g$ is quasi-compact and the
factorization $\mathsf C(g)$ is a compactification of $U\to S$; this is
$\mathsf C_{\mathrm{aff}}(U/S)$ of [def-nagata-affine-compactification].
So $U\to S$ is compactifiable [def-nagata-compactifiable]. If $U$ is
affine, it is quasi-affine by
[lemma-nagata-affine-finite-type-is-quasi-affine], so the statement
applies.
