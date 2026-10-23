+++
id = "lemma-nagata-relative-affine-space-charts"
kind = "lemma"
title = "Relative affine-space charts and base change"
order = 408
lean = ["AlgebraicGeometry.AffineSpace.chart", "AlgebraicGeometry.AffineSpace.opensRange_chart", "AlgebraicGeometry.AffineSpace.iSup_opensRange_chart", "AlgebraicGeometry.AffineSpace.chartTransition", "AlgebraicGeometry.AffineSpace.chartTransition_chart", "AlgebraicGeometry.AffineSpace.chartTransition_comp", "AlgebraicGeometry.AffineSpace.pullbackIso", "AlgebraicGeometry.AffineSpace.chart_pullbackIso_inv"]
uses = ["def-nagata-relative-affine-space"]
+++
Let $S$ be a scheme and $n$ an index set.

1. For every affine open $V\subseteq S$ the chart
$\operatorname{Spec}\bigl(\mathcal O_S(V)[T_i:i\in n]\bigr)\to\mathbb A^n_S$
of [def-nagata-relative-affine-space] is an open immersion onto the preimage
of $V$, and these charts cover $\mathbb A^n_S$.
1. For affine opens $V'\subseteq V$ of $S$, the chart over $V'$ is the chart
over $V$ precomposed with the morphism induced by the restriction
$\mathcal O_S(V)[T_i]\to\mathcal O_S(V')[T_i]$, and these transition
morphisms satisfy the cocycle condition: for $V''\subseteq V'\subseteq V$ the
transition for $V''\subseteq V$ is the composite of those for
$V''\subseteq V'$ and $V'\subseteq V$.
1. For every morphism $g\colon T\to S$ there is a canonical isomorphism
$\mathbb A^n_S\times_ST\cong\mathbb A^n_T$ over $T$, compatible with the
charts: for affine opens $W\subseteq T$ and $V\subseteq S$ with
$g(W)\subseteq V$, the chart of $\mathbb A^n_T$ over $W$ corresponds to the
chart of $\mathbb A^n_S$ over $V$, after changing coefficients along
$g^\sharp\colon\mathcal O_S(V)\to\mathcal O_T(W)$, together with the
structure morphism to $T$.
