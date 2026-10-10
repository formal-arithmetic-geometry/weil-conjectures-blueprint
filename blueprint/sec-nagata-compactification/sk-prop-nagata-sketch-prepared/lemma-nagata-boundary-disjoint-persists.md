+++
id = "lemma-nagata-boundary-disjoint-persists"
kind = "lemma"
title = "Disjoint boundary closures persist"
order = 269
lean = ["AlgebraicGeometry.TwoOpenSide.Prepared.admissibleBlowup", "AlgebraicGeometry.disjoint_range_strictTransformMap_of_disjoint"]
uses = ["def-nagata-strict-transform", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-strict-transform-restrict"]
+++
Let $\pi\colon X'\to X$ be a morphism, $W\subseteq X$ an open, and
$f_1\colon Y_1\to X$, $f_2\colon Y_2\to X$ morphisms with disjoint images.
Then the strict transforms of $f_1$ and $f_2$ along $\pi$ relative to $W$
have disjoint images in $X'$. In particular, for a side over a Noetherian
base $S$: if $\overline Z_{i,i}$ and $\overline Z_{i,j}$ are disjoint, then
after every further $V_i$-admissible blow-up $b\colon X_i'\to X_i$ the
closures in $X_i'$ of $b^{-1}(Z_{i,i})$ and $b^{-1}(Z_{i,j})$ (the boundary
closures of the transported side) remain disjoint, and so do the strict
transforms of $\overline Z_{i,i}$ and $\overline Z_{i,j}$; in particular a
prepared side stays prepared.

## Proof

Every point of $Y_k\times_XX'$ maps to a point of $X'$ whose image in $X$
lies in $f_k(Y_k)$. The strict transform of $f_k$ is a closed subscheme of
$Y_k\times_XX'$ ([def-nagata-strict-transform]), so its image in $X'$ is
contained in $\pi^{-1}(f_k(Y_k))$. The inverse images under $\pi$ of the
disjoint sets $f_1(Y_1)$ and $f_2(Y_2)$ are disjoint, which proves the first
assertion.

For the second, let $b\colon X'_i\to X_i$ be a further $V_i$-admissible
blow-up; it is an isomorphism over $V_i$, and the transported $Z_{i,k}$ is
$b^{-1}(Z_{i,k})\subseteq b^{-1}(V_i)$. Since $b^{-1}(\overline Z_{i,k})$ is
closed and contains $b^{-1}(Z_{i,k})$, the closure of $b^{-1}(Z_{i,k})$ is
contained in $b^{-1}(\overline Z_{i,k})$. By the argument for the first
assertion (with $f_k$ the inclusion of $\overline Z_{i,k}$), the strict transform of
$\overline Z_{i,k}$ lies in $b^{-1}(\overline Z_{i,k})$ as well. The
inverse images of the disjoint closed subsets $\overline Z_{i,i}$ and
$\overline Z_{i,j}$ are disjoint, so both pairs are disjoint.
