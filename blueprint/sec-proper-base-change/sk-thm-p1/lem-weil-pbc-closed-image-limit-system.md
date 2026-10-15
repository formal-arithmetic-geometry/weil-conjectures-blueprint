+++
id = "lem-weil-pbc-closed-image-limit-system"
kind = "lemma"
title = "Closed subschemes are limits of their stage scheme-theoretic images"
uses = ["def-pc-scheme", "pqf-def-affine-morphism"]
lean = ["AlgebraicGeometry.exists_closed_image_limit_system"]
+++
Let $J$ be a small nonempty cofiltered category and $D:J\to\mathsf{Scheme}$ a diagram of schemes [def-pc-scheme]. Suppose every $D_j$ is quasi-compact `CompactSpace` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Defs/Filter.lean)) and quasi-separated (the intersection of any two quasi-compact open subsets is quasi-compact), and every transition morphism is affine [pqf-def-affine-morphism]. Let $\pi_Y$ be a limit cone with vertex $Y$ and let $i:X\to Y$ be a closed immersion `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)). Then there exist a diagram $Z:J\to\mathsf{Scheme}$, a natural transformation $k:Z\to D$ with closed immersion components, and a cone $\pi_X$ with vertex $X$, such that $X$ is its limit, every transition of $Z$ is affine, and $\pi_{X,j}\mathbin{;}k_j=i\mathbin{;}\pi_{Y,j}$ for every $j\in J$ (composition written in diagram order).
