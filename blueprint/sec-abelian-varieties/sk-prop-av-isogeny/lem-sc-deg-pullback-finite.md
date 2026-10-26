+++
id = "lem-sc-deg-pullback-finite"
kind = "lemma"
title = "Degree of the pullback under a finite morphism"
lean = ["AlgebraicGeometry.Scheme.Hom.degree_pullback"]
order = 482
uses = ["def-sc-ample", "def-sc-function-field", "def-sc-hilbert-degree", "lem-sc-hilbert-polynomial"]
+++
Let $f:X\to Y$ be a finite surjective morphism of proper
varieties over a field $k$, let $\mathcal M$ be an
ample invertible $\mathcal O_Y$-module,
and let $\deg(f)=[k(X):k(Y)]$ be the degree of the finite
dominant morphism $f$
(function fields). Then

$$
\deg_{f^*\mathcal M}(X)=\deg(f)\deg_{\mathcal M}(Y),
$$

where the degrees are those of [def-sc-hilbert-degree].
