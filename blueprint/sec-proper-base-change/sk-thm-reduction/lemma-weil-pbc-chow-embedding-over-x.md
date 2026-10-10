+++
id = "lemma-weil-pbc-chow-embedding-over-x"
kind = "lemma"
title = "Projective embedding over $X$"
order = 1198
lean = ["AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpaceSource", "AlgebraicGeometry.ChowModification.toProjectiveSpaceSource", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_liftBaseChange"]
uses = ["cor-chow-lemma-proper", "def-nagata-affine-proj", "def-nagata-projective-space-base-change", "lem-weil-pbc-closed-immersion-from-composite", "lemma-nagata-projective-space-base-change-pullback", "lemma-weil-pbc-chow-factorization", "thm-chow-lemma"]
+++
Let $f:X\to Y$ be a proper morphism with $Y$ Noetherian, let $\pi:X'\to X$
be its Chow modification and $\iota_Y:X'\hookrightarrow\mathbf P^n_Y$ the
closed immersion over $Y$. Then

$$
\iota_X=(\pi,\iota_Y):X'\longrightarrow
X\times_Y\mathbf P^n_Y=\mathbf P^n_X
$$

is a closed immersion over $X$. More generally, for a separated morphism
$f:X\to Y$, a morphism $a:T\to X$ and a closed immersion
$b:T\hookrightarrow\mathbf P^n_Y$ with $fa$ equal to the composite of $b$
with $\mathbf P^n_Y\to Y$, the induced morphism
$(a,b):T\to\mathbf P^n_X$ is a closed immersion.

## Proof

We prove the general statement first. The identification
$\mathbf P^n_X=X\times_Y\mathbf P^n_Y$ is the defining fibre-product identity
([lemma-nagata-projective-space-base-change-pullback]), so the condition
$fa=q_Y\circ b$ (with $q_Y:\mathbf P^n_Y\to Y$) gives a unique morphism
$(a,b):T\to\mathbf P^n_X$ over $X$ whose composite with the base change
$\mathbf P^n_X\to\mathbf P^n_Y$ of $f$ is $b$. That base change is
separated, because $f$ is separated and separatedness is stable under base
change. A morphism whose composite with a separated morphism is a closed
immersion is itself a closed immersion
([lem-weil-pbc-closed-immersion-from-composite]); as $b$ is a closed
immersion, so is $(a,b)$.

For the first assertion, $f$ is proper, hence separated, and the Chow
modification ([lemma-weil-pbc-chow-factorization]) satisfies
$f\pi=q_Y\circ\iota_Y$ with $\iota_Y$ a closed immersion. Applying the
general statement with $T=X'$, $a=\pi$ and $b=\iota_Y$ shows that
$\iota_X=(\pi,\iota_Y)$ is a closed immersion over $X$.
