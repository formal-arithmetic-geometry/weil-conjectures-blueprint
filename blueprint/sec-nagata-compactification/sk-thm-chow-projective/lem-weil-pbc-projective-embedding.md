+++
id = "lem-weil-pbc-projective-embedding"
kind = "lemma"
title = "Projective embedding over the source"
order = 439
lean = ["AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_liftBaseChange", "AlgebraicGeometry.ProjectiveSpace.liftBaseChange", "AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpaceSource", "AlgebraicGeometry.ChowModification.toProjectiveSpaceSource"]
uses = ["cor-chow-lemma-proper", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-proper-immersion-closed", "lem-weil-pbc-proper-to-separated"]
+++
Let $f:X\to Y$ be a separated morphism, let $a:T\to X$ be a morphism and
let $b:T\hookrightarrow\mathbf P^n_Y$ be a closed immersion with $f\circ a$
equal to $b$ followed by the projection $\mathbf P^n_Y\to Y$. Then the
induced morphism

$$
 (a,b):T\longrightarrow X\times_Y\mathbf P^n_Y\simeq\mathbf P^n_X
$$

is a closed immersion over $X$. In particular, if $f$ is proper, $Y$ is
Noetherian and $\pi:\widetilde X\to X$ with $i_Y:\widetilde X\hookrightarrow
\mathbf P^n_Y$ is its Chow modification [cor-chow-lemma-proper], then the map
$i_X=(\pi,i_Y):\widetilde X\to\mathbf P^n_X$ is a closed immersion over $X$.
