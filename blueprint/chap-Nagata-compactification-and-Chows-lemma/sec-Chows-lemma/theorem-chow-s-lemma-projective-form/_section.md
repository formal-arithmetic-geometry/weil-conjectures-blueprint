+++
id = "theorem-chow-s-lemma-projective-form"
kind = "theorem"
title = "Chow's lemma, projective form"
order = 1468
lean = ["AlgebraicGeometry.ProjectiveDomination.nonempty_of_isAffine", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_liftBaseChange"]
+++
Let $f:X\to S$ be proper with $S$ qcqs. There are a proper
surjection $\pi:\widetilde X\to X$ and a closed immersion
$i_S:\widetilde X\hookrightarrow\mathbf P^n_S$ such that
$f\pi=q_Si_S$, where $q_S:\mathbf P^n_S\to S$ is the projection. Moreover,

$$
i_X=(\pi,i_S):\widetilde X\hookrightarrow
X\times_S\mathbf P^n_S=\mathbf P^n_X
$$

is a closed immersion. Both $\pi$ and $f\pi$ are projective.
