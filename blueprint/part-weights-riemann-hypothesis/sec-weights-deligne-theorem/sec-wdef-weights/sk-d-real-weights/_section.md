+++
id = "sk-d-real-weights"
kind = "definition"
title = "Weights"
order = 633
lean = ["AlgebraicGeometry.WeilGroup.IsPunctuallyPure", "AlgebraicGeometry.WeilGroup.frobeniusWeight", "AlgebraicGeometry.WeilGroup.localPolynomial", "AlgebraicGeometry.WeilGroup.HasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost"]
uses = ["sk-d-real-weil"]
tags = ["sketch"]
+++
At a point of degree $d$, an eigenvalue $\alpha$ of Frobenius has
$\iota$-weight $w$ if

$$
|\iota(\alpha)|=q^{dw/2}.
$$

A constructible Weil sheaf is punctually $\iota$-pure of weight $w$ if
this holds for every eigenvalue at every closed point. It is
$\iota$-mixed if it has a finite filtration by Weil subsheaves whose
nonzero quotients are punctually pure, of possibly different real weights.
It has weights at most $w$ if such a filtration has quotient weights at
most $w$. A constructible Weil sheaf is *punctually of weights
$\le w$* if $|\iota(\alpha)|\le q_x^{w/2}$ for
every eigenvalue $\alpha$ at every closed point $x$.
For a bounded Weil complex $K$, the derived convention is

$$
K\text{ has weights at most }w
\quad\Longleftrightarrow\quad
\mathcal H^i(K)\text{ has weights at most }w+i\text{ for all }i.
$$

Purity of a complex means that each nonzero $\mathcal H^i(K)$ is pure of
weight $w+i$. Zero objects satisfy every bound.

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
