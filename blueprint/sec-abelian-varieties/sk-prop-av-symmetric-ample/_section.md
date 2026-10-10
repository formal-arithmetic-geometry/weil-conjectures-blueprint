+++
id = "sk-prop-av-symmetric-ample"
kind = "proposition"
title = "A symmetric ample module"
lean = ["AlgebraicGeometry.IsAbelianVariety.isAmple_symmetrisation", "AlgebraicGeometry.IsAbelianVariety.nonempty_iso_overPullback_inv_symmetrisation"]
order = 475
uses = ["sk-def-av", "sk-def-av-ample-degree", "sk-prop-av-projective"]
tags = ["sketch"]
+++
Let $A$ be an abelian variety over $k$ and let $\cL$ be an
invertible $\cO_A$-module. Then

$$
\cN:=\cL\otimes[-1]^*\cL
$$

is *symmetric*: $[-1]^*\cN\cong\cN$. If moreover $\cL$ is ample, then
$\cN$ is ample.
