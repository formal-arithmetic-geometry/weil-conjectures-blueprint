+++
id = "def-kun-rgamma-unbounded"
kind = "definition"
title = "Unbounded derived global sections"
order = 6038
lean = ["AlgebraicGeometry.Etale.RGamma"]
+++
For a scheme $T$, a commutative ring $\Lambda$ and
$K\in D(T_{\Et},\Lambda)$, choose a K-injective resolution $K\to I$ and put
$$
R\Gamma(T_{\Et},K)=\Gamma(T_{\Et},I),\qquad
H^q(T_{\Et},K)=\mathcal H^q(R\Gamma(T_{\Et},K)).
$$

The independence of the result of the chosen resolution is
[lem-kun-rgamma-unbounded-well-defined], and for
$K\in\Dplus(T_{\Et},\Lambda)$ its agreement with the bounded-below functor
is [lem-kun-rgamma-unbounded-bounded].

Unresolved dependencies: def:weil-pbc-etale-cohomology, def:weil-pbc-kinjective-resolutions, prop:weil-pbc-kinjective-resolutions-exist
