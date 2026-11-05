+++
id = "lemma-bounds-squared-traces--text-1"
kind = "hidden"
title = "Bounds for squared traces"
order = 1202001
uses = ["definition-growth-squared-traces"]
+++
Fix a finite field $k_0$ of cardinality $q$, a prime $\ell$ different
from its characteristic, and an embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
All weight parameters are real. Write $S_n$ and $\nu$ for the trace
energy and growth parameter of [definition-growth-squared-traces].
Lean uses the equivalent supremum of the real $\beta$ for which the
upper limit of $S_n/q^{n(\beta+1)}$ is positive, with that upper limit
taken in $[0,+\infty]$ and the supremum in $[-\infty,+\infty]$.

The statements below use Weil sheaves. Where a bound or an identity is asserted
for every $n\in\mathbf N$, it includes Lean's formal value at $n=0$,
where the Frobenius power is the identity. On a general scheme the sum is interpreted as Lean's sum over
the support of the summand, with value zero when that support is
infinite; on the curves considered here the point sets are finite.
