+++
id = "thm-pur-vector-bundle-thom"
kind = "theorem"
title = "Vector-bundle Thom isomorphism"
order = 2943
uses = ["cor-pur-affine-space-zero-section-purity", "def-amb-vector-integration", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-vector-bundle-thom-class", "def-pur-vector-bundle-zero-section", "def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-scheme-morphism-properties", "lem-pur-cfiber-stalk", "lem-pur-kunneth-supported", "thm-pur-localized-top-chern", "thm-pur-projective-bundle-formula", "thm-pur-rank-one-local-calculation", "thm-pur-rank-one-thom"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $\pi:E\to B$ be a vector bundle of constant rank $r$ with zero
section $z$. The morphism
$\tau_E:\Lambda_B\to R\pi_!\Lambda_E(r)[2r]$ of
[def-pur-vector-bundle-thom-class] is an isomorphism, compatible
with base change and with direct sums of vector bundles. Its inverse
is the *vector-bundle trace*

$$
\operatorname{tr}_\pi:R\pi_!\Lambda_E(r)[2r]\longrightarrow\Lambda_B.
$$

It differs from the integration $t_\pi$ of [def-amb-vector-integration],
which is normalized by the projective-line trace, by a sign:
$\operatorname{tr}_\pi=(-1)^rt_\pi$. For $r=1$, $\operatorname{tr}_\pi$ is
the rank-one trace of [thm-pur-rank-one-thom], so that one is $-t_\pi$.
