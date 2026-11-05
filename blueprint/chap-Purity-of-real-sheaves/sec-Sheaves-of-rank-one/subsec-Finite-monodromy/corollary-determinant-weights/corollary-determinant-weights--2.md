+++
id = "corollary-determinant-weights--2"
kind = "corollary"
title = "Independence of the Frobenius lift"
name_showing = false
order = 1111002
aliases = ["bp-r341-2"]
lean = ["Representation.detWeight_mul_of_mem_ker"]
uses = ["situation-weil", "definition-weil-representation", "definition-determinant-weight"]
+++
The comparison of finite coefficient fields in this part is bypassed by
Lean, which works over the fixed field $\overline{\mathbf Q}_\ell$.
Independence of the lift is proved in the following general form.

Let $G$ be a group, $E$ a field, $\rho$ a representation of $G$ on an
$E$-vector space $V$, and $\deg:G\to\mathbf Z$ a homomorphism. Suppose
that $\det\rho(\ker\deg)$ is finite, and let
$\lambda:E^\times\to(\mathbf R,+)$ be a homomorphism. For any $s\in G$
and $u\in\ker\deg$,

$$
\frac{\lambda(\det\rho(us))}{r}
=\frac{\lambda(\det\rho(s))}{r},
\qquad r=\operatorname{finrank}_E V.
$$

Here $\operatorname{finrank}_E V=\dim_E V$ in finite dimension and is
zero in infinite dimension; division by zero is interpreted as zero.
There is no restriction on the degree of $s$.

In particular, for the lisse Weil representation of
[corollary-determinant-weights--1] with $r>0$, take
$\lambda=\lambda_\iota$. Any two degree-one lifts differ by left
multiplication by an element of $\pi_1(U)$, so
$\operatorname{dw}_\iota(\mathcal V)$ is independent of the lift.
