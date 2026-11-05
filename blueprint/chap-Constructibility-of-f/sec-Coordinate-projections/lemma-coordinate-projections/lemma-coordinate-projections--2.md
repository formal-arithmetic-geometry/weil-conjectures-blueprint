+++
id = "lemma-coordinate-projections--2"
kind = "lemma"
title = "Coordinate projections (2)"
name_showing = false
order = 572003
aliases = ["bp-r173-2"]
lean = ["AlgebraicGeometry.exists_isFinite_morphismRestrict_of_range_subset"]
uses = []
+++
More generally, let $S$ be an integral locally Noetherian scheme, and let
$p:Y\to S$ be proper. Choose a finite open cover
$Y=\bigcup_\alpha Y_\alpha$ and closed immersions
$Y_\alpha\hookrightarrow\mathbf A^{m_\alpha}_S$ over $S$, where the
$m_\alpha$ are nonnegative integers. Write
$t_{\alpha r}:Y_\alpha\to\mathbf A^1_S$ for the coordinate functions.
Suppose given a nonempty open $V_{\alpha r}\subset\mathbf A^1_S$ for
each $\alpha,r$, and put

$$
G=\bigcup_{\alpha,r}
t_{\alpha r}^{-1}(V_{\alpha r})\subset Y.
$$

There is a nonempty open $W\subset S$ such that, for every closed
immersion $i:Z\hookrightarrow Y$ whose image is contained in
$Y\setminus G$, the morphism $Z\times_S W\to W$ is finite. The same
$W$ works for all such closed subschemes, including the reduced closed
complement.
