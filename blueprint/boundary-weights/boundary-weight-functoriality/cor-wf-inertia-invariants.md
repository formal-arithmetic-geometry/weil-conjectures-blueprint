+++
id = "cor-wf-inertia-invariants"
kind = "theorem"
title = "Weights of inertia invariants"
order = 4206
tags = ["latex:corollary"]
uses = ["def-weil-punctual-weights", "def-wf-middle-extension", "lem-wf-boundary-semicontinuity", "lem-wf-boundary-stalk-invariants"]
+++
Let $\mathcal F$ be lisse and
punctually $\iota$-pure of
weight $w$ on a punctured smooth curve $U_0$ over $k_0$, let
$x$ be a missing point, and let $V=\mathcal F_{\bar\eta}$ be the
local geometric generic stalk, with its local geometric monodromy, and
the local inertia action. Then every eigenvalue $\alpha$ of
the local Frobenius $F_x$ on the
boundary stalk
$(j_*\mathcal F)_{\bar x}$ of the
middle extension at $x$
satisfies $|\iota(\alpha)|^2\leq q_x^{w}$: the boundary stalk has
weights at most $w$, by the
boundary semicontinuity of
[lem-wf-boundary-semicontinuity] rather than by any purity
assertion on the graded pieces.

## Proof

For the bound, [lem-wf-boundary-semicontinuity] requires an
affine ambient curve, so choose a smooth geometrically connected affine
open $X_0$ of the curve containing $x$ and replace $U_0$ by
$U_0':=X_0\setminus\{x\}$: then $j:U_0'\hookrightarrow X_0$ is a
dense open immersion with finite complement, and $\mathcal F|_{U_0'}$
is again lisse and punctually $\iota$-pure of weight $w$. The
boundary stalk of the middle extension of [def-wf-middle-extension]
at $x$ is unchanged by this shrinking, that stalk being computed on
the strict henselian trait at $x$. By the punctual purity of weight
$w$ of [def-weil-punctual-weights], every eigenvalue of every
local Frobenius on $\mathcal F|_{U_0'}$ has $\iota$-modulus
$q_y^{w/2}$; the trivial filtration
$0\subset\mathcal F|_{U_0'}$ therefore exhibits $\mathcal F|_{U_0'}$
as punctually $\iota$-mixed of weights at most $w$ in
the sense of [def-weil-punctual-weights]. The boundary
semicontinuity of [lem-wf-boundary-semicontinuity], applied to the
dense open immersion $j$ with $\beta=w$, now gives
$|\iota(\alpha)|^2\leq q_x^{w}$ for every eigenvalue $\alpha$ of
$F_x$ on $(j_*\mathcal F)_{\bar x}$, which is the asserted bound.
