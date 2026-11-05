+++
kind = "proof"
of = "theorem-chow-s-lemma-projective-form--2"
order = 1468005
uses = []
+++
Let $p:\mathbf P(N;X)\to\mathbf P(N;S)$ be the base change of $f$.
The cartesian square for projective space defines $i_X$ and gives
$p i_X=i_S$ and $q_Xi_X=\pi$. Since $f$ is separated, so is $p$.
Closed immersions cancel along separated morphisms, hence $i_X$ is
closed. This is
`AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_liftBaseChange`.

When $N$ is finite, the factorizations $\pi=q_Xi_X$ and $f\pi=q_Si_S$
express both maps as a closed immersion followed by a projective-space
projection. They are therefore projective. To use the notation
$\mathbf P^n$ with $n\geq 0$, embed the space with coordinates $N$
linearly into one with $n+1$ coordinates, as in
`AlgebraicGeometry.ProjectiveSpace.exists_isClosedImmersion_finite_coordinates`.
