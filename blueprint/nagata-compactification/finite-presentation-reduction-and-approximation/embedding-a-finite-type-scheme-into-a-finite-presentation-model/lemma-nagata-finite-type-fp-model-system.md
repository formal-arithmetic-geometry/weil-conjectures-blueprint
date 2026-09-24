+++
id = "lemma-nagata-finite-type-fp-model-system"
kind = "lemma"
title = "Properties of the finite-presentation model system, [stacks-project]"
order = 550
lean = ["AlgebraicGeometry.Scheme.Hom.exists_isClosedImmersion_locallyOfFinitePresentation", "AlgebraicGeometry.Scheme.Hom.nonempty_finitePresentationApproximation"]
uses = ["def-nagata-finite-type-fp-model-system", "lemma-nagata-closed-subscheme-fp-system", "lemma-nagata-immersion-into-fp-model", "lemma-nagata-immersion-shrink-to-closed"]
+++
Every $X_\alpha\to S$ is of finite presentation, every transition map is a
closed immersion, every $i_\alpha$ is a closed immersion, and
$X\cong\varprojlim_\alpha X_\alpha$ over $S$.

## Proof

The immersion model is of finite presentation over $S$. Since $S$ is
quasi-separated, its source is quasi-separated; the selected open
$Y^\circ$ is quasi-compact and remains of finite presentation over $S$.
The closed-subscheme system then has closed transitions and limit $X$.
Composition of each finite-presentation closed immersion
$X_\alpha\hookrightarrow Y^\circ$ with $Y^\circ\to S$ is of finite
presentation. The canonical maps from the limit are closed immersions
because the transition maps are closed immersions.
