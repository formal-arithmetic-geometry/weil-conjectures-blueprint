+++
id = "lemma-weil-pbc-chow-factorization"
kind = "lemma"
title = "Chow and projective factorization"
lean = ["AlgebraicGeometry.ProjectiveDomination", "AlgebraicGeometry.ProjectiveDomination.pullback", "AlgebraicGeometry.ProjectiveDomination.nonempty_of_isAffine"]
order = 1938
uses = ["def-nagata-final-descended-model", "def-nagata-finite-type-closed-in-fp", "def-nagata-projective-space-base-change", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-proper-base-change", "lem-weil-pbc-proper-composition", "lem-weil-pbc-proper-immersion-closed", "lem-weil-pbc-proper-to-separated", "lemma-nagata-final-descended-model", "lemma-nagata-projective-space-base-change-proper", "prop-nagata-finite-type-closed-in-fp", "thm-chow-lemma"]
+++
Let $f:X\to Y$ be a proper [def-weil-pbc-scheme-conventions] morphism with
$Y$ affine. There exist a proper surjection $\pi:\widetilde X\to X$, an
integer $n\geq0$, and a closed immersion

$$
 i:\widetilde X\hookrightarrow\mathbf P^n_Y
$$

with $f\circ\pi=p\circ i$, where $p:\mathbf P^n_Y\to Y$ is the structure
morphism. No noetherian or finite-presentation hypothesis is imposed on $Y$ or
$f$. The assertion is stable under base change on $Y$: for any morphism
$Y'\to Y$ the pulled-back data are such data for $X\times_YY'\to Y'$.

(For $Y$ noetherian this is also [cor-chow-lemma-proper], which moreover makes
$\pi$ an isomorphism over a dense open subscheme of $X$.)
