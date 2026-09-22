+++
id = "lem-kun-rgamma-unbounded-well-defined"
kind = "lemma"
title = "Independence of the K-injective resolution"
order = 6039
lean = ["AlgebraicGeometry.Etale.RGamma_indep_kinjective"]
uses = ["def-kun-rgamma-unbounded"]
+++
Let $T$ be a scheme, $\Lambda$ a commutative ring and
$K\in D(T_{\Et},\Lambda)$, and let $K\to I$ and $K\to J$ be two K-injective
resolutions of $K$. Then any comparison $I\to J$ over $K$ induces an
isomorphism $\Gamma(T_{\Et},I)\to\Gamma(T_{\Et},J)$ in $D(\Lambda)$;
consequently $R\Gamma(T_{\Et},K)$ of [def-kun-rgamma-unbounded] is
independent, up to canonical isomorphism, of the chosen K-injective
resolution.

## Proof

Two K-injective resolutions of $K$ are chain-homotopy equivalent, and a
bounded-below complex of injective objects is K-injective; a comparison
$I\to J$ over $K$ between K-injective resolutions is therefore a homotopy
equivalence. The functor $\Gamma(T_{\Et},-)$ carries chain-homotopy
equivalences to homotopy equivalences of complexes of $\Lambda$-modules,
hence to isomorphisms in the derived category, so $\Gamma(T_{\Et},I)$ is
independent of the chosen K-injective resolution $I$ of $K$.

Unresolved dependencies: def:weil-pbc-kinjective-resolutions, prop:weil-pbc-kinjective-resolutions-exist
