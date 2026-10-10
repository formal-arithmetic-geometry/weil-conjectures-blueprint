+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-affine-cover"
uses = ["sk-prop-nagata-sketch-zmt"]
+++
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
