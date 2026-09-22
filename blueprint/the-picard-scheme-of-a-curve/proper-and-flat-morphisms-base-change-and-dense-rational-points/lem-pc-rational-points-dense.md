+++
id = "lem-pc-rational-points-dense"
kind = "lemma"
title = "Rational points on smooth schemes over separably closed fields"
order = 4339
lean = ["AlgebraicGeometry.dense_rationalPoints_of_isSepClosed"]
uses = ["def-pc-separably-closed", "lem-pc-dense-separable-points", "lem-pc-sepclosed-finite-sep-trivial"]
+++
Let $k$ be a separably closed field [def-pc-separably-closed], let $X$ be a
scheme over $k$ which is smooth over $k$. Then $X(k)$ is dense in $X$; if
$X$ is nonempty, then $X(k)\neq\emptyset$.

## Proof

By [lem-pc-dense-separable-points] the set of closed points $x$ with
$\kappa(x)/k$ finite separable is dense in $X$. For such an $x$,
$\kappa(x)=k$ by [lem-pc-sepclosed-finite-sep-trivial], so $x$ is a
$k$-rational point and the assertion follows.
