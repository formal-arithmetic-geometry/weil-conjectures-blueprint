+++
id = "lemma-nagata-rees-polynomial-surjection"
kind = "lemma"
title = "Properties of the homogeneous polynomial map"
order = 243
lean = ["AlgebraicGeometry.reesGradedPresentation_surjective"]
uses = ["def-nagata-rees-polynomial-map", "lemma-nagata-rees-degree-one-element", "prop-nagata-rees-finite-generation"]
+++
The constructed map $\rho_I$ is graded and surjective.

## Proof

The assignment is homogeneous because $f_it$ lies in degree one by
[lemma-nagata-rees-degree-one-element]. A monomial
$T_{i_1}\cdots T_{i_n}$ maps to
$(f_{i_1}\cdots f_{i_n})t^n$. Such products generate $I^n$, so every
degree component is hit. Every Rees element is a finite sum of homogeneous
components, proving surjectivity.
