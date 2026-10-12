+++
kind  = "proof"
of    = "lem-sfb-subfield-flat"
uses = ["sk-def-sfb-pullback-from-point"]
+++
$F_X$ is finite free over $E_X$. On the point, an $E$-basis $b_1,\dots,b_n$ of $F$ gives an
isomorphism of $\underline E$-modules $C(-,F)\cong C(-,E)^n$, $h\mapsto(h_i)$ with
$h=\sum_ih_ib_i$ (the coordinate functions $F\to E$ are continuous). The inverse image $p_X^*$
of [sk-def-sfb-pullback-from-point] is additive and monoidal, so $F_X\cong E_X^n$ as
$E_X$-modules. Hence $F_X\otimes_{E_X}M\cong M^n$ naturally in $M$, and finite direct sums are
exact.
