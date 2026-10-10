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
