+++
id = "lemma-weil-pbc-chow-embedding-over-x"
kind = "lemma"
title = "Projective embedding over $X$"
order = 687
lean = ["AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpaceSource", "AlgebraicGeometry.ChowModification.toProjectiveSpaceSource", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_liftBaseChange"]
uses = ["cor-chow-lemma-proper", "def-nagata-projective-space-base-change", "lemma-weil-pbc-chow-factorization"]
+++
Let $\iota_Y:X'\hookrightarrow\mathbf P^n_Y$ be the closed immersion and
$\pi:X'\to X$ the Chow modification. Then

$$
\iota_X=(\pi,\iota_Y):X'\longrightarrow
X\times_Y\mathbf P^n_Y=\mathbf P^n_X
$$

is a closed immersion over $X$.

## Proof

The identification $\mathbf P^n_X=X\times_Y\mathbf P^n_Y$ is the defining fibre-product
identity, so the pair $\iota_X=(\pi,\iota_Y)$ is a morphism over $X$ by construction, and
composing it with the base change $\mathbf P^n_X\to\mathbf P^n_Y$ of $f$ gives back
$\iota_Y$. That base change is separated, because $f$ is separated and separatedness is
stable under base change. A morphism whose composite with a separated morphism is a closed
immersion is itself a closed immersion; hence $\iota_X$ is a closed immersion.
