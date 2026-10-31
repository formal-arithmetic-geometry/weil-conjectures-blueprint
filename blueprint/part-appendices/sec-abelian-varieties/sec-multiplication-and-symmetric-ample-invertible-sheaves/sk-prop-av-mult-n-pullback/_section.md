+++
id = "sk-prop-av-mult-n-pullback"
kind = "proposition"
title = "Commutativity, projectivity and the cube"
order = 865
lean = ["AlgebraicGeometry.IsAbelianVariety.isCommMonObj", "AlgebraicGeometry.IsAbelianVariety.exists_isClosedImmersion_projectiveSpace", "AlgebraicGeometry.IsAbelianVariety.isAmple_symmetrisation", "AlgebraicGeometry.IsAbelianVariety.nonempty_iso_overPullback_inv_symmetrisation", "AlgebraicGeometry.nonempty_iso_overPullback_npow_id"]
uses = ["sk-def-av", "sk-lem-abelian-seesaw"]
tags = ["sketch"]
+++
An abelian variety $A$ is commutative and projective. It admits a
symmetric ample invertible sheaf $\mathcal N$, and for every $n>0$

$$
[-1]^*\mathcal N\simeq\mathcal N,
\qquad [n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}.
$$
