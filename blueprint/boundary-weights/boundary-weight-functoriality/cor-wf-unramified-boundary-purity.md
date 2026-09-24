+++
id = "cor-wf-unramified-boundary-purity"
kind = "theorem"
title = "Purity at an unramified boundary point"
order = 4202
tags = ["latex:corollary"]
uses = ["def-weil-frobenius-module-weights", "def-weil-punctual-weights", "lem-wf-boundary-semicontinuity", "lem-wf-boundary-stalk-invariants"]
+++
Let $\mathcal F$ be lisse and $\iota$-pure of weight $w$ on a
punctured smooth curve, and let $x$ be the missing point. If the
local inertia action at $x$ is trivial, then the extended stalk
$(j_*\mathcal F)_{\bar x}$ is pure of weight $w$.

## Proof

By [lem-wf-boundary-stalk-invariants], trivial inertia identifies
the boundary stalk with the full local representation.
Apply [lem-wf-boundary-semicontinuity] on an affine neighbourhood
of the missing point to $\mathcal F$, and then to
$\mathcal F^\vee$. The latter is punctually pure of weight $-w$,
since duality inverts local eigenvalues, by
[def-weil-punctual-weights].
Because inertia is trivial, the extended dual stalk is the linear dual
of the extended stalk. The two bounds are therefore
$|\iota(\alpha)|^2\leq q_x^w$ and
$|\iota(\alpha^{-1})|^2\leq q_x^{-w}$.
Together they give equality, namely purity in
[def-weil-frobenius-module-weights].
