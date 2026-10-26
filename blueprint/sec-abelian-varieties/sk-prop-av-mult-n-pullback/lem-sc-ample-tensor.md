+++
id = "lem-sc-ample-tensor"
kind = "lemma"
title = "Tensor products of ample modules"
lean = ["AlgebraicGeometry.IsAmple.tensorObj", "AlgebraicGeometry.IsAbelianVariety.isAmple_symmetrisation", "AlgebraicGeometry.IsAbelianVariety.nonempty_iso_overPullback_inv_symmetrisation"]
order = 472
uses = ["def-sc-abelian-variety", "def-sc-ample"]
+++
Let $X$ be a scheme over a field $k$ and let $\mathcal L$ and
$\mathcal M$ be ample invertible
$\mathcal O_X$-modules. Then $\mathcal L\otimes\mathcal M$ is
ample. In particular, for an
abelian variety $A$ and an
invertible module $\mathcal L$ on $A$, the module
$\mathcal L\otimes[-1]^*\mathcal L$ satisfies
$[-1]^*(\mathcal L\otimes[-1]^*\mathcal L)\cong\mathcal L\otimes [-1]^*\mathcal L$,
and it is ample if $\mathcal L$ is ample.
