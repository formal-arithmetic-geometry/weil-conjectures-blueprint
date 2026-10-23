+++
id = "lemma-nagata-strict-chart-map-surjective"
kind = "lemma"
title = "Surjectivity onto the extended-ideal chart"
order = 267
lean = ["AlgebraicGeometry.AffineBlowup.closure_range_awayAlgebraMap_union_range_awayMap", "AlgebraicGeometry.AffineBlowup.strictChartMap_surjective"]
uses = ["def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-strict-chart-to-extended-blowup-chart", "lemma-nagata-chart-ring-normal-form", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-mul", "lemma-nagata-strict-chart-to-extended-blowup-chart", "prop-nagata-rees-graded"]
+++
Let $\varphi\colon A\to B$ be a ring map, let $I\subseteq A$ be an ideal,
put $J=IB$, and let $a\in I$ with image $b=\varphi(a)$. Then the chart ring
$B[J/b]$ of the blow-up of $J$ is generated as a ring by the images of $B$
and of the chart ring $A[I/a]$. Equivalently, the homomorphism
$\sigma_a\colon B\otimes_AA[I/a]\to B[J/b]$ is surjective.
