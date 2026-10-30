+++
id = "sk-r-real-linear"
kind = "proposition"
title = "Weights under the usual operations"
order = 637
lean = ["AlgebraicGeometry.WeilGroup.frobeniusWeight_inv", "AlgebraicGeometry.WeilGroup.IsPunctuallyPure.dual"]
uses = ["sk-p-tate", "sk-d-real-weights", "sk-d-real-weil", "sk-def-sp-tate-twist", "sk-p-linear-filtration"]
tags = ["sketch"]
+++
Subobjects and quotients of a pure Weil sheaf of weight $w$ are pure of
weight $w$. Subquotients and extensions of mixed sheaves are mixed,
and an extension of two sheaves with a common upper bound has the same
bound. Tensor products of pure sheaves of weights $a$ and $b$ are pure
of weight $a+b$, and the dual of a pure lisse sheaf of weight $a$ is
pure of weight $-a$. A tensor product of mixed sheaves of weights at
most $a$ and at most $b$ is mixed of weights at most $a+b$, and the dual
of a mixed lisse sheaf is mixed, with graded pieces the duals of the
given ones, of the negated weights. Inverse image preserves purity,
mixedness and their upper bounds. If a complex $K$ has weights at most
$w$, then $K[r]$ has weights at most $w+r$.

For $b\in \overline{\mathbf Q}_\ell^\times$, let $\mathcal B_b$ be the geometrically constant
rank-one Weil sheaf on which a degree-one Frobenius acts by $b$.
Tensoring by $\mathcal B_b$ adds
$\lambda_\iota(b)=2\log_q|\iota(b)|$ to every weight. The Tate sheaf
$\overline{\mathbf Q}_\ell(1)$ has geometric Frobenius $q^{-1}$, so twisting by $(r)$
subtracts $2r$ from every weight.

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
