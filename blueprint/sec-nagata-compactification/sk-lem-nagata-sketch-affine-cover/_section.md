+++
id = "sk-lem-nagata-sketch-affine-cover"
kind = "section"
title = "Affine starting pieces and dense overlaps"
order = 306
uses = ["sk-lem-nagata-sketch-closure", "sk-prop-nagata-sketch-zmt"]
lean = ["AlgebraicGeometry.Scheme.finiteAffineOpenCoverDenseIInter_spec", "AlgebraicGeometry.HasCompactification.of_isQuasiAffine"]
+++
*Lemma (sketch).*

Let $X$ be a quasi-compact scheme with finitely many irreducible
components. Then there is a finite affine open cover
$X=\bigcup_{i=1}^n U_i$ with dense total intersection. Moreover, if $U$ is
a quasi-affine scheme (for instance an affine one) and $U\to S$ is
quasi-compact and locally of finite type, then $U\to S$ is compactifiable;
this applies to each $U_i\to S$ when $S$ is Noetherian and $X\to S$ is
separated and of finite type.

## Proof

Every point $x$ of $X$ has an affine open neighbourhood containing all
the finitely many generic points of the irreducible components: take an
affine $W\ni x$ avoiding the components not through $x$ (it then contains
the generic points of the components through $x$), and add disjoint small
affine opens around the remaining generic points, avoiding $\overline W$
and the other components; a finite disjoint union of affines is affine
(compare 01ZX). By quasi-compactness finitely many of these cover $X$.
Every $U_i$ contains all generic points, so their total intersection is
dense.

If $U$ is quasi-affine and $U\to S$ is quasi-compact and locally of finite
type, there is an immersion $U\to\mathbb A^n_S$ over $S$ by
[sk-prop-nagata-sketch-zmt](ii); composed with the standard open chart
$\mathbb A^n_S\hookrightarrow\mathbb P^n_S$ it is an immersion into a
scheme proper over $S$, quasi-compact because $U\to S$ is, and its
scheme-theoretic image is a compactification by
[sk-lem-nagata-sketch-closure]. When $S$ is Noetherian and $X\to S$ is
separated of finite type, each $U_i$ is affine, hence quasi-affine, and
$U_i\to S$ is locally of finite type and quasi-compact ($U_i$ is
quasi-compact and $S$ is quasi-separated).
