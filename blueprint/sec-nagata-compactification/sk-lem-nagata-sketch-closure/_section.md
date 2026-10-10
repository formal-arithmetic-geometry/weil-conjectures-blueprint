+++
id = "sk-lem-nagata-sketch-closure"
kind = "lemma"
title = "Scheme-theoretic closure and compactification"
order = 63
uses = ["sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.Compactification.ofIsImmersion", "AlgebraicGeometry.Compactification.denseRefinement", "AlgebraicGeometry.Compactification.baseChange"]
tags = ["sketch"]
+++
For a morphism $h:T\to Y$, its
scheme-theoretic image $\SIm(h)$ is the smallest closed subscheme of $Y$
through which $h$ factors. For quasi-compact $h$ it commutes with
restriction to an open of $Y$.
Consequently, a quasi-compact immersion into a proper $S$-scheme gives a
compactification by taking its scheme-theoretic image. In particular,
compactifications of quasi-compact morphisms admit dense refinements, and
closed subschemes of a compactifiable quasi-compact $S$-scheme are
compactifiable. Compactifications are
preserved by base change.
