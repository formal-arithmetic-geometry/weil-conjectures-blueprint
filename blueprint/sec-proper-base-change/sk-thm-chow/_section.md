+++
id = "sk-thm-chow"
kind = "lemma"
title = "Chow's lemma"
order = 1063
lean = ["AlgebraicGeometry.ChowModification.nonempty_data", "AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpace"]
uses = ["sk-def-conv"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be proper with $Y$ affine. There exist a proper surjection
$\pi:\widetilde X\to X$ and a closed immersion
$i_Y:\widetilde X\hookrightarrow\mathbf P^n_Y$ such that $f\pi=q_Yi_Y$, where
$q_Y:\mathbf P^n_Y\to Y$ is the projection. Moreover

$$
i_X=(\pi,i_Y):\widetilde X\hookrightarrow X\times_Y\mathbf P^n_Y=\mathbf P^n_X
$$

is a closed immersion. In particular both $\pi$ and $f\pi$ are projective
morphisms.
