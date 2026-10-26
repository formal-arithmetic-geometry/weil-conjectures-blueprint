+++
id = "lem-sc-rational-function-morphism"
kind = "lemma"
title = "Rational functions define morphisms to $\\mathbf P^1$"
lean = ["AlgebraicGeometry.Scheme.exists_hom_projectiveLine_of_functionField"]
order = 667
uses = ["def-sc-curves", "def-sc-function-field", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field, $C$ an integral scheme, smooth of relative
dimension one and proper over $k$, and $f\in k(C)$
([def-sc-function-field]) transcendental over $k$ (for $k$
algebraically closed: $f\in k(C)\setminus k$).
Then $f$ defines a morphism of $k$-schemes

$$
\pi_f:C\to\mathbf P^1_k
$$

with $\pi_f^*t=f$, where $t$ is the standard coordinate on
$\mathbf P^1$: at the generic point of $C$ it is the point
$[1:f]$ of $\mathbf P^1(k(C))$.
