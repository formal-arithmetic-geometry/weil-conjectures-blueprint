+++
id = "lemma-weil-pbc-chow-embedding-over-x"
kind = "lemma"
title = "Projective embedding over $X$"
order = 1264
lean = ["AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpaceSource", "AlgebraicGeometry.ChowModification.toProjectiveSpaceSource", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_liftBaseChange"]
uses = ["def-nagata-affine-proj", "def-nagata-projective-space-base-change", "lemma-nagata-projective-space-base-change-pullback", "lemma-weil-pbc-chow-factorization", "thm-chow-lemma"]
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
