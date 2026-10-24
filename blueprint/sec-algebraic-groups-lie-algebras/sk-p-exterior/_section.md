+++
id = "sk-p-exterior"
kind = "proposition"
title = "Exterior determinant weights"
lean = ["Representation.CompositionSeries.exteriorPower_detWeight"]
order = 3776
uses = ["sk-d-weights", "sk-i-restriction", "sk-p-central", "sk-p-readout", "sk-r-linear-library"]
tags = ["sketch"]
+++
Let $A_1,\ldots,A_t$ be the composition factors of a nonzero Weil
representation $V$. Write $d_a=\dim A_a$ and $\gamma_a=\dw_\iota(A_a)$. Fix
$0\le r\le\dim V$, and assume that every $A_a$ and every simple factor of
$\bigwedge^rV$ has finite geometric determinant. The determinant weights of
its simple factors are exactly the possible values

$$
\sum_an_a\gamma_a,
\qquad 0\le n_a\le d_a,\qquad \sum_an_a=r.
$$

Equivalently, if $m(\gamma)=\sum_{\gamma_a=\gamma}d_a$, they are the sums
$\sum_\gamma n_\gamma\gamma$ with $0\le n_\gamma\le m(\gamma)$ and
$\sum_\gamma n_\gamma=r$. These are equalities of sets of weights; the
multiplicities of the simple factors may differ.

*Complement.* The inclusion "every weight is such a sum" holds for every
real weight character $\lambda$ in place of $\lambda_\iota$, over any
algebraically closed field of characteristic zero, and for an arbitrary
group $W$ with a homomorphism $\deg\colon W\to\mathbf Z$ and an element
$\gamma\in W$ as in the complement of [sk-p-tensor]: if
$a_1,\ldots,a_{\dim V}$ is the rank-counted weight list of the factors,
every simple subquotient $Q$ of $\bigwedge^rV$ with finite geometric
determinant has $\dw_\lambda(Q)=a_{i_1}+\cdots+a_{i_r}$ for some
$i_1<\cdots<i_r$.
