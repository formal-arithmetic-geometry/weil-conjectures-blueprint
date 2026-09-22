+++
id = "lem-kun-rgamma-unbounded-bounded"
kind = "lemma"
title = "Agreement with the bounded derived global sections"
order = 6040
lean = ["AlgebraicGeometry.Etale.RGamma_eq_of_boundedBelow"]
uses = ["def-kun-rgamma-unbounded"]
+++
Let $T$ be a scheme, $\Lambda$ a commutative ring and
$K\in\Dplus(T_{\Et},\Lambda)$. Then $R\Gamma(T_{\Et},K)$ of
[def-kun-rgamma-unbounded] agrees canonically with
$\Gamma(T,\operatorname{Kinj}(K))$ of the ambient chapter.

## Proof

The object $R\Gamma(T_{\Et},K)$ is $\Gamma(T_{\Et},I)$ for a K-injective
resolution $K\to I$, while the ambient definition uses the functorial
K-injective resolution $\operatorname{Kinj}(K)$. The two resolutions are
chain-homotopy equivalent, and the comparison between them is a homotopy
equivalence; applying $\Gamma(T_{\Et},-)$ therefore gives a canonical
isomorphism in $D(\Lambda)$.

Unresolved dependencies: def:weil-pbc-etale-cohomology, prop:weil-pbc-kinjective-resolutions-exist
