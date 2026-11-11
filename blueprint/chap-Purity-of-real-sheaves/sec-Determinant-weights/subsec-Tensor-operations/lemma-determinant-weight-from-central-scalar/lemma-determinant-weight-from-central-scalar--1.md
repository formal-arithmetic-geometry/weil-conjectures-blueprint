+++
id = "lemma-determinant-weight-from-central-scalar--1"
kind = "lemma"
title = "Determinant weight for a represented degree datum"
order = 1145001
aliases = ["bp-r351-1"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair_of_basis"]
uses = ["definition-determinant-weight--1", "definition-monodromy-groups--1", "definition-monodromy-groups--2", "lemma-normality-geometric-monodromy--1"]
+++
Let $k$ be a field, let $W$ be a group with a surjective homomorphism
$\deg:W\to\mathbf Z$ and a chosen element $s$ of degree one, and let
$\rho:W\to\GL(k^n)$ be a representation. Put $P=\ker\deg$, and let
$H\subseteq G$ be the Zariski closures of $\rho(P)$ and $\rho(W)$,
as in [definition-monodromy-groups]. Let
$\lambda:k^\times\to(\R,+)$ be a homomorphism. Suppose that $N>0$ is
an integer and that

$$
z=h\rho(s)^N,\qquad h\in H(k),\qquad z\in Z(G(k)),
$$

so that $(N,z)$ is a positive central pair of the form supplied by
[proposition-central-element-arithmetic-monodromy-group].

Let $U\subsetneq S\subseteq k^n$ be $W$-stable subspaces, and put
$Q=S/U$. Assume that the determinant character $\delta_Q$ has finite
image on $P$ and that $c_Q\in k^\times$ satisfies
$zx-c_Qx\in U$ for every $x\in S$. With the determinant weight defined
as in [definition-determinant-weight], using $\lambda$ and $s$, we have

$$
\operatorname{dw}_\lambda(Q)
=\frac{\lambda(\delta_Q(s))}{\dim_k Q}
=\frac{\lambda(c_Q)}{N}.
$$

For the Weil representations of
[proposition-central-element-arithmetic-monodromy-group], take
$k=\overline{\mathbf Q}_\ell$ and $\lambda=\lambda_\iota$; the hypothesis
on $\delta_Q$ holds by [corollary-determinant-weights]. Transporting
$(N,z)$ along a tensor construction as in
[proposition-central-element-arithmetic-monodromy-group--2], the formula
gives $\operatorname{dw}_\iota(Q)=\lambda_\iota(c_Q)/N$ for every nonzero
subquotient $Q$ of a tensor construction on $V$ on which $z$ acts by a
scalar $c_Q$.
