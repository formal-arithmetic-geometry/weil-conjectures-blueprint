+++
id = "sk-prop-av-jacobian-general"
kind = "section"
title = "The Jacobian over an arbitrary ground field"
order = 597
uses = ["sk-def-av", "sk-def-av-pic", "sk-prop-av-jacobian"]
+++
*Proposition (sketch).*

Let $k$ be any field and $C$ a smooth projective geometrically
connected curve over $k$ of genus $g$. Then there is an abelian
variety $J$ over $k$ of dimension $g$ with a natural isomorphism
$h_J\cong\Pic^0_{C/k}$ of fppf sheaves, and $J_K\cong \Pic^0_{C_K/K}$ for every field extension $K/k$. No $k$-rational
point of $C$ is assumed.

## Proof

Fix a separable closure $k_s$. By [sk-prop-av-jacobian] the base change
$\Pic^0_{C_{k_s}/k_s}$ is represented by an abelian variety $J_s$ of
dimension $g$. The single functor $\Pic^0_{C/k}$ produces by Yoneda a
canonical descent datum on $J_s$ over $\Spec(k_s)/\Spec(k)$, which
satisfies the cocycle condition automatically; it is defined at a
finite separable level $K/k$ by spreading out, and effective descent
for the projective $J_K$ along the finite locally free cover
$\Spec K\to\Spec k$ produces a $k$-scheme $J$ with
$J\times_kK\cong J_K$ and $J\times_kk_s\cong J_s$. The group law of
$J_s$ is defined over $K$ and compatible with the datum, so it
descends; the geometric properties (finite type, smooth, proper,
connected, dimension $g$) descend by fpqc-locality; hence $J$ is an
abelian variety by [sk-prop-av-char]. Finally $h_J$ and
$\Pic^0_{C/k}$ become isomorphic after the faithfully flat base change
$\Spec k_s\to\Spec k$, so they were isomorphic.

Uses: [sk-def-av-pic], [sk-def-av], [sk-prop-av-jacobian]
