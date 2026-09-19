+++
id = "prop-zla-cohomological-factorization"
kind = "theorem"
title = "Cohomological determinant factorization"
order = 994
tags = ["latex:proposition"]
uses = ["def-zla-trace-datum", "lem-zla-counting-log", "lem-zla-trace-det"]
+++
For a finite cohomological trace datum,

$$
\operatorname{Exp}\left(\sum_{n\geq1}N_n\frac{T^n}{n}\right)
=\prod_{i=0}^rP_i(T)^{(-1)^{i+1}}
\qquad\text{in }E[[T]],
$$

where a negative exponent denotes the inverse in $E[[T]]$, available because
$P_i(0)=1$. Equivalently, clearing the inverses,

$$
\operatorname{Exp}\left(\sum_{n\geq1}N_n\frac{T^n}{n}\right)
\cdot\prod_{\substack{0\leq i\leq r\\ i\text{ even}}}P_i(T)
=\prod_{\substack{0\leq i\leq r\\ i\text{ odd}}}P_i(T),
$$

which is the shape of the factorization required by
`IsWeilFactorization`. In particular the left-hand side is the Taylor
expansion at the origin of a rational function in $E(T)$.

## Proof

By [lem-zla-counting-log] the exponent may be rewritten as the finite
alternating sum $\sum_i(-1)^i\sum_{n\geq1}\Tr(F_i^n\mid V_i)T^n/n$. The formal
exponential turns a finite sum into a finite product, so the left-hand side is
$\prod_i\operatorname{Exp}\left(\sum_n\Tr(F_i^n)T^n/n\right)^{(-1)^i}$, and
each factor is $P_i(T)^{-1}$ by [lem-zla-trace-det].
