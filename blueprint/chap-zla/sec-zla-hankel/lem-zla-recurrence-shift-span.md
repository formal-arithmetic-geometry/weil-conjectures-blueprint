+++
id = "lem-zla-recurrence-shift-span"
kind = "lemma"
title = "A recurrence gives finite shift span"
order = 1001
uses = ["def-zla-eventual-recurrence", "def-zla-shift-span"]
+++
If $a\in K^{\mathbf N}$ satisfies an eventual recurrence, then
$\operatorname{Sh}_K(a)$ is finite-dimensional.

## Proof

Let $(c_1,\ldots,c_d;N)$ be the recurrence and put
$M=\max\{N,d\}$. Beyond the threshold the recurrence expresses $S^ma$, for
$m\geq M$, as a $K$-linear combination of $S^{m-1}a,\ldots,S^{m-d}a$ up to a
sequence supported in the finitely many coordinates below the threshold; hence
$\operatorname{Sh}_K(a)$ is contained in the span of
$a,Sa,\ldots,S^{M-1}a$ together with the finitely many coordinate vectors
supported before the recurrence threshold, and by induction on $m$ every shift
lies in that finite-dimensional space.
