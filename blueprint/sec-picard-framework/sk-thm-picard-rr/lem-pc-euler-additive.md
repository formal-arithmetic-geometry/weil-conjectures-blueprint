+++
id = "lem-pc-euler-additive"
kind = "lemma"
title = "Additivity of the Euler characteristic"
lean = ["AlgebraicGeometry.Scheme.Modules.eulerChar_eq_add_of_shortExact", "AlgebraicGeometry.Scheme.Modules.finiteDimensional_H_of_isProper", "AlgebraicGeometry.Scheme.Modules.finite_setOf_nontrivial_H_of_isProper"]
order = 695
uses = ["def-pc-derived-direct-image", "def-pc-morphism-conventions", "lem-pc-coherent-hi"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$, and let

$$
0\to\mathcal{F}_1\to\mathcal{F}_2\to\mathcal{F}_3\to0
$$

be a short exact sequence of coherent $\mathcal{O}_X$-modules. Then

$$
\chi(X,\mathcal{F}_2)=\chi(X,\mathcal{F}_1)+\chi(X,\mathcal{F}_3).
$$
