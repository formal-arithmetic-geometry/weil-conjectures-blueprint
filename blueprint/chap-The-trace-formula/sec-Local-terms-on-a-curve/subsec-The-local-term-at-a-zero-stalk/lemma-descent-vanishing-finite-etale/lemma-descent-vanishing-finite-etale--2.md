+++
id = "lemma-descent-vanishing-finite-etale--2"
kind = "lemma"
title = "Descent of vanishing along a trace of invertible degree"
order = 987003
aliases = ["bp-r301-2"]
lean = ["DerivedCategory.eq_zero_of_comp_trace_of_isUnit"]
+++
Let $A$ be a commutative ring, let $M_1,M_2,M'_1,M'_2\in D(A)$, and
let

$$
r:M_1\to M_2,\qquad r':M'_1\to M'_2,\qquad
p_1:M_1\to M'_1,\qquad p_2:M_2\to M'_2
$$

satisfy $p_2\circ r=r'\circ p_1$. Suppose there are a morphism
$t:M'_2\to M_2$ and an integer $n$ whose image in $A$ is invertible,
such that $t\circ p_2=n\,\operatorname{id}_{M_2}$. If $r'=0$, then
$r=0$.

In particular, let $n$ be invertible in $A$, and let $p$ and $t$ be the
pullback map and the trace of [lemma-descent-vanishing-finite-etale--1].
Taking $r=\alpha$, $p_1=\operatorname{id}_M$, $r'=p\circ\alpha$ and
$p_2=p$ shows that a morphism $\alpha:M\to R\Gamma(W,L)$ in $D(A)$ is
zero if $p\circ\alpha=0$.
