+++
id = "lemma-nagata-finite-presentation-descends"
kind = "lemma"
title = "Property of finite-presentation descent, [stacks-project]"
order = 370
lean = ["AlgebraicGeometry.Scheme.exists_isPullback_of_finitePresentation", "AlgebraicGeometry.isPullback_finitePresentationDescent"]
uses = ["def-nagata-finite-presentation-descent", "lemma-nagata-relative-gluing-axioms-eventually", "lemma-nagata-relative-gluing-datum-descends"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of quasi-compact
quasi-separated schemes with affine transition maps and limit $S$, and let
$X\to S$ be of finite presentation. Then there are an index $\lambda$ and a
scheme $X_\lambda$ of finite presentation over $S_\lambda$ such that
$X\cong X_\lambda\times_{S_\lambda}S$ over $S$. Concretely, the constructed
$X^{\mathrm{desc}}_{\lambda_{\mathrm{rel}}}\to S_{\lambda_{\mathrm{rel}}}$ is of finite presentation, and
$\epsilon_X$ is an isomorphism over $S$.
