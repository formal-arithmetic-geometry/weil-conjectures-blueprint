+++
id = "prop-weil-pbc-cohomology-resolution-independent"
kind = "theorem"
title = "Resolution independence of etale cohomology"
order = 1068
lean = ["CochainComplex.IsKInjective.nonempty_homology_iso"]
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-site", "def-weil-pbc-kinjective-resolutions", "prop-weil-pbc-kinjective-resolutions-exist"]
tags = ["latex:proposition"]
+++
Let $\mathcal C$ and $\mathcal D$ be abelian categories, $G:\mathcal C\to\mathcal D$
an additive functor, and $K$ a complex in $\mathcal C$. If $K\to I^\bullet$ and
$K\to J^\bullet$ are two K-injective resolutions
[def-weil-pbc-kinjective-resolutions] of $K$, then for every $q$ the objects
$\mathcal H^q(G(I^\bullet))$ and $\mathcal H^q(G(J^\bullet))$ are isomorphic.

In particular, let $T$ be a scheme and $F$ an etale abelian sheaf on the small
etale site [def-weil-pbc-etale-site] of $T$. For $G=\Gamma(T,-)$ and $K=F$
placed in degree $0$, the groups $\mathcal H^q(\Gamma(T,I^\bullet))$ and
$\mathcal H^q(\Gamma(T,J^\bullet))$ are isomorphic, so the groups
$H^q(T_{\Et},F)$ of [def-weil-pbc-etale-cohomology] are independent of the
chosen resolution.

## Proof

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
