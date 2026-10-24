+++
id = "sk-d-real-weights"
kind = "definition"
title = "Weights"
order = 3795
uses = ["sk-d-real-weil"]
lean = ["AlgebraicGeometry.WeilGroup.IsPunctuallyPure", "AlgebraicGeometry.WeilGroup.frobeniusWeight", "AlgebraicGeometry.WeilGroup.localPolynomial", "AlgebraicGeometry.WeilGroup.HasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost"]
tags = ["sketch"]
+++
A Frobenius module over $\overline{\mathbf Q}_\ell$ is a finite-dimensional
space with an invertible operator. At a point of degree $d$, an eigenvalue
$\alpha$ has $\iota$-weight $w$ if

$$
 |\iota(\alpha)|=q^{dw/2}.
$$

A constructible Weil sheaf is punctually $\iota$-pure of weight $w$ if
this holds for every eigenvalue at every closed point. It is
$\iota$-mixed if it has a finite filtration by Weil subsheaves whose
nonzero quotients are punctually pure, of possibly different real weights.
It has weights at most $w$ if such a filtration has quotient weights at
most $w$. We say that a constructible Weil sheaf has a
*punctual bound at most $w$* if $|\iota(\alpha)|\le q_x^{w/2}$ for
every eigenvalue $\alpha$ at every closed point $x$; this is weaker
than having weights at most $w$, since no filtration is required.
Every mixed sheaf of weights at most $w$ has a punctual bound at most
$w$. For a bounded Weil complex $K$, the derived convention is

$$
 K\text{ has weights at most }w
 \quad\Longleftrightarrow\quad
 \mathcal H^i(K)\text{ has weights at most }w+i\text{ for all }i.
$$

Purity of a complex means that each nonzero $\mathcal H^i(K)$ is pure of
weight $w+i$. Zero objects satisfy every bound.

Weights only depend on the characteristic polynomials of Frobenius;
for instance, a Jordan block and its semisimplification have the same
weights. At a point over $k_m=\mathbf F_{q^m}$ lying above $x$, with
$d(x)\mid m$, the operator is $F_x^{m/d(x)}$ and a weight-$w$ eigenvalue
has modulus $q^{mw/2}$.

*Complement.* For a Weil sheaf $\mathcal F$ and a closed point $x$, with
local Frobenius $F_x$ of [sk-d-real-weil] acting on the stalk
$\mathcal F_{\bar x}$ (for a lisse sheaf, on the generic fibre $V$ through
$\rho(F_x)$), the local characteristic polynomial and the weight of a local
eigenvalue are

$$
P_x(\mathcal F,T)=\det(1-TF_x\mid\mathcal F_{\bar x}),\qquad
\wt_{\iota,q_x}(\alpha)=\frac{2\log|\iota(\alpha)|}{\log q_x}.
$$

For a Frobenius module the same notions are [def-weil-frobenius-module-weights].
