+++
id = "lemma-nagata-rees-degree-one-element"
kind = "lemma"
title = "Degree-one element associated to an ideal element"
order = 23
lean = ["AlgebraicGeometry.reesX", "AlgebraicGeometry.coe_reesX", "AlgebraicGeometry.reesX_mem"]
uses = ["def-nagata-rees-algebra", "def-nagata-rees-piece", "lemma-nagata-rees-piece-membership"]
+++
Every $a\in I$ determines an element $at$ of $\mathcal R_A(I)$, whose
underlying polynomial is the monomial $at$; it is homogeneous of degree one.

## Proof

Since $a\in I=I^1$, the monomial $at$ belongs to the degree-one piece by
[lemma-nagata-rees-piece-membership]. The underlying-polynomial and
coefficient formulas follow from the corresponding formulas for a
polynomial monomial.
