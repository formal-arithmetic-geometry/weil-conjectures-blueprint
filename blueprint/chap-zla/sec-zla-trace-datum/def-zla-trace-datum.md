+++
id = "def-zla-trace-datum"
kind = "definition"
title = "Finite cohomological trace datum"
order = 992
uses = ["def-zla-recip-charpoly"]
+++
Let $E$ be a field of characteristic zero. A *finite cohomological trace
datum* over $E$ consists of:

1. an integer $r\geq0$ and, for each $0\leq i\leq r$, a finite-dimensional
$E$-vector space $V_i$ together with an endomorphism
$F_i\in\operatorname{End}_E(V_i)$;
1. integers $N_n\in\mathbf Z$ for every $n\geq1$;
1. the equalities
$$
N_n=\sum_{i=0}^r(-1)^i\Tr(F_i^n\mid V_i)
\qquad\text{in }E,\qquad(n\geq1),
$$
the left-hand side being the image of $N_n$ under
$\mathbf Z\to\mathbf Q\to E$.

Put $P_i(T)=\det(1-TF_i\mid V_i)$. In the intended application $V_i$ is the
$i$-th cohomology group of a perfect complex and $F_i$ is induced by a
Frobenius automorphism, but nothing below uses a complex: only the finite
family $(V_i,F_i)_{0\leq i\leq r}$ and the trace equalities enter.
