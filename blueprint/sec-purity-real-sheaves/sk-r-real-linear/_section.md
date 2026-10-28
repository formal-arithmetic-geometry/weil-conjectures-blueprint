+++
id = "sk-r-real-linear"
kind = "proposition"
title = "Elementary weight operations"
order = 3966
uses = ["sk-p-tate", "sk-d-real-weights", "sk-d-real-weil", "sk-def-sp-tate-twist", "sk-p-linear-filtration"]
lean = ["AlgebraicGeometry.WeilGroup.frobeniusWeight_inv", "AlgebraicGeometry.WeilGroup.IsPunctuallyPure.dual"]
tags = ["sketch"]
+++
Subobjects and quotients of a pure Weil sheaf of weight $w$ are pure of
weight $w$. Subquotients and extensions of mixed sheaves are mixed;
extensions preserve a common upper bound. Tensor products of pure
sheaves of weights $a,b$ are pure of weight $a+b$, and the dual of a pure
lisse sheaf of weight $a$ is pure of weight $-a$. The corresponding
mixed statements follow by finite filtrations. Inverse image preserves
purity, mixedness and their upper bounds. Shifting a complex by $[r]$
adds $r$ to its weight convention.

For $b\in\overline{\mathbf Q}_\ell^\times$, let $\mathcal B_b$ be the
geometrically constant rank-one Weil sheaf on which a degree-one Frobenius
acts by $b$. Tensoring by $\mathcal B_b$ adds
$\lambda_\iota(b)=2\log_q|\iota(b)|$ to every weight. The Tate sheaf
$\overline{\mathbf Q}_\ell(1)$ has geometric Frobenius $q^{-1}$, so twisting
by $(r)$ subtracts $2r$ from every weight.

*Complement.* The operations on Weil representations (direct sum, tensor
product, exterior powers, dual, determinant, constituents, invariants
$V^I$ and coinvariants $V_I$) are those of
[def-real-weil-representation-operations], transported to lisse Weil sheaves
by [sk-d-real-weil]; the local polynomial of [sk-d-real-weights] is computed
by any element of the local Frobenius class ([p-real-operations]). The
constant line $\mathcal B_b$ is [def-wf-constant-weil-twist], and
$\overline{\mathbf Q}_\ell(n)=\mathcal B_{q^{-n}}$. A semisimplification has the
same local polynomials $P_x$ as the sheaf, hence the same weights, and
$\wt_{\iota,q_x}(\alpha^{-1})=-\wt_{\iota,q_x}(\alpha)$.
