+++
id = "sk-prop-av-jacobian"
kind = "section"
title = "The Jacobian: $\\Pic^0_{C/k}$ is representable — input"
order = 595
uses = ["sk-def-av", "sk-def-av-jacobian", "sk-def-av-pic"]
+++
*Proposition (sketch).*

Let $k$ be a separably closed field and $C$ a smooth projective
geometrically integral curve over $k$ of genus $g$. Then
$\Pic^0_{C/k}$ is representable: there is an abelian variety $J_C$ of
dimension $g$ over $k$, the *Jacobian*, with a natural
isomorphism $\Pic^0_{C/k}\cong h_{J_C}$ of group-valued functors, and
$J_C(k)\cong\Pic^0(C)$; moreover $J_C$ is projective and compatible
with base change along extensions of separably closed fields.

## Proof

This is the Jacobian theorem: over an
algebraically closed field it is [sk-prop-jacobian] of
[sec-picard-framework], which derives it from the representability
of the Picard functor, [sk-thm-picard-main]. It is the one
representation-theoretic input of the abelian-variety block.
The proper smooth connected $g$-dimensional group scheme $J_C$ is an
abelian variety in the sense of [sk-def-av] by [sk-prop-av-char].

Uses: [sk-def-av-jacobian], [sk-def-av-pic], [sk-def-av]
