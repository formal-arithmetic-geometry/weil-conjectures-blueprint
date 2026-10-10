+++
kind  = "proof"
of    = "prop-weil-pbc-cohomology-resolution-independent"
+++
The two K-injective resolutions of $K$ are chain-homotopy equivalent (a
quasi-isomorphism between K-injective complexes is a homotopy equivalence;
compare [prop-weil-pbc-kinjective-resolutions-exist]), so there are chain maps
$I^\bullet\to J^\bullet$ and $J^\bullet\to I^\bullet$ over $K$ whose
composites are homotopic to the identities. The additive functor
$G$ (for instance $\Gamma(T,-)$ of [def-weil-pbc-etale-cohomology]) carries chain maps
to chain maps and preserves homotopies and composites, so
$G(I^\bullet)$ and $G(J^\bullet)$ are chain-homotopy equivalent complexes. Chain-homotopy equivalent complexes
have isomorphic cohomology in every degree, so $\mathcal
H^q(G(I^\bullet))\cong\mathcal H^q(G(J^\bullet))$ for all $q$.
For $G=\Gamma(T,-)$ and $K=F$ these cohomology groups are the groups $H^q(T_{\Et},F)$ of
[def-weil-pbc-etale-cohomology], which is therefore independent of the
resolution, the resolutions being those of
[def-weil-pbc-kinjective-resolutions].
