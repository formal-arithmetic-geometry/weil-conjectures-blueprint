+++
id = "prop-pur-affine-line-trace-normalization"
kind = "theorem"
title = "Trace normalization of the affine-line purity"
order = 2041
tags = ["latex:proposition"]
uses = ["def-amb-p1-trace", "def-pur-affine-line-purity-comparison", "def-pur-conventions", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "lem-amb-cartier-kummer-map", "thm-amb-p1-decomposition", "thm-pur-affine-line-orientation", "thm-pur-affine-line-purity"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting), let $Y$, $K$, and $\gamma_{p,K}$ be as in
[thm-pur-affine-line-purity]. The composite

$$
Rp_!Lp^*K(1)[2]
\xrightarrow{\ Rp_!(\gamma_{p,K})\ }
Rp_!Rp^!K
\xrightarrow{\ \operatorname{Tr}_{p,K}\ }K
$$

is the compactly supported integration map of
[def-pur-affine-line-purity-comparison], i.e. the
projection-formula composite of
[def-pur-affine-line-purity-comparison]; for $K=\Lambda_Y$ it is
the affine-line integration $\int_p$, and it sends the normalized
fiber orientation to $1\in\Lambda$, the adjoint form of the
normalization of [thm-pur-affine-line-orientation].

## Proof

By [def-pur-affine-line-purity-comparison], the map
$\gamma_{p,K}$ is the adjoint of
$\mu_K=(1_K\otimes\int_p)\circ\operatorname{PF}$.
The triangle identity for the adjunction of
[def-weil-exceptional-inverse-image] gives
$\operatorname{Tr}_{p,K}\circ Rp_!(\gamma_{p,K})=\mu_K$.
For the normalization, the supported zero-section map of
[lem-amb-cartier-kummer-map] is the coordinate Kummer boundary
of [thm-pur-affine-line-orientation]. Under the projective-line
decomposition [thm-amb-p1-decomposition], its image is the class
of a degree-one divisor. The trace of [def-amb-p1-trace] sends
this class to $1$. Its restriction to the affine-line compact
support is $\int_p$, so it has the asserted normalization.
Base-change compatibility follows from [thm-pur-affine-line-purity].
