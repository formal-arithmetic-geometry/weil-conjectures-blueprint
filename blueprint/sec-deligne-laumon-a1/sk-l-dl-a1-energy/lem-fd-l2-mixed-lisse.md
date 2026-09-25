+++
id = "lem-fd-l2-mixed-lisse"
kind = "lemma"
title = "The $L^2$-weight of a mixed lisse sheaf"
order = 3021
uses = ["def-weil-punctual-weights", "def-wf-l2-norm", "lem-wf-l2-purity-rigidity", "lem-wf-l2-upper"]
+++
Let $\mathcal A\neq0$ be lisse on a smooth geometrically connected
affine curve, and suppose it has a finite filtration with nonzero
punctually pure graded pieces. If $W$ is the largest weight of
these pieces, then $\|\mathcal A\|=W$.

## Proof

Replace the filtered sheaf by the direct sum of its graded pieces;
local Frobenius traces are unchanged by exact sequences.
Let $\mathcal P$ be the sum of pieces of weight $W$, and
$\mathcal Q$ the sum of lower-weight pieces.
The sheaf $\mathcal P$ is nonzero and punctually pure by
[def-weil-punctual-weights], so
[lem-wf-l2-purity-rigidity] gives $\|\mathcal P\|=W$.
If $\mathcal Q\neq0$, its weights have a maximum $W'<W$,
and [lem-wf-l2-upper] gives $\|\mathcal Q\|\leq W'$.
For $W'<b<c<W$, the definition [def-wf-l2-norm] supplies
a subsequence on which
$\|f_{\mathcal P}\|_m\geq\epsilon q^{m(c+1)/2}$, whereas
$\|f_{\mathcal Q}\|_m=o(q^{m(b+1)/2})$.
The Euclidean triangle inequality for the trace functions shows that
$\|\mathcal A\|\geq b$. Let $b\uparrow W$.
The reverse bound is [lem-wf-l2-upper].
If $\mathcal Q=0$, the pure rigidity already proves equality.
