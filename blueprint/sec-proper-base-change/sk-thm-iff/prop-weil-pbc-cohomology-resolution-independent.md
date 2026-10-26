+++
id = "prop-weil-pbc-cohomology-resolution-independent"
kind = "theorem"
title = "Resolution independence of etale cohomology"
order = 1538
lean = ["CochainComplex.IsKInjective.nonempty_homology_iso"]
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-site", "def-sp-kinjective-bridge", "prop-weil-pbc-kinjective-resolutions-exist"]
tags = ["latex:proposition"]
+++
Let $\mathcal C$ and $\mathcal D$ be abelian categories, $G:\mathcal C\to\mathcal D$
an additive functor, and $K$ a complex in $\mathcal C$. If $K\to I^\bullet$ and
$K\to J^\bullet$ are two K-injective resolutions
[def-sp-kinjective-bridge] of $K$, then for every $q$ the objects
$\mathcal H^q(G(I^\bullet))$ and $\mathcal H^q(G(J^\bullet))$ are isomorphic.

In particular, let $T$ be a scheme and $F$ an etale abelian sheaf on the small
etale site [def-weil-pbc-etale-site] of $T$. For $G=\Gamma(T,-)$ and $K=F$
placed in degree $0$, the groups $\mathcal H^q(\Gamma(T,I^\bullet))$ and
$\mathcal H^q(\Gamma(T,J^\bullet))$ are isomorphic, so the groups
$H^q(T_{\Et},F)$ of [def-weil-pbc-etale-cohomology] are independent of the
chosen resolution.
