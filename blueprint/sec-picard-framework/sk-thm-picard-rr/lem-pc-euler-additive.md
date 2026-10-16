+++
id = "lem-pc-euler-additive"
kind = "lemma"
title = "Additivity of the Euler characteristic"
lean = ["AlgebraicGeometry.Scheme.Modules.eulerChar_eq_add_of_shortExact"]
order = 746
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

Moreover, for a morphism $f:Y\to X$ of proper $k$-schemes and a
coherent $\mathcal{O}_Y$-module $\mathcal{G}$:

$$
\chi(Y,\mathcal{G})=\sum_{i\ge0}(-1)^i\chi(X,R^if_*\mathcal{G}).
$$
