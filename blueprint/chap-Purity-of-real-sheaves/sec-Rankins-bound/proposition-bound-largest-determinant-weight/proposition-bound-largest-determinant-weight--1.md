+++
id = "proposition-bound-largest-determinant-weight--1"
kind = "proposition"
title = "The Rankin bound and iterated tensor squares"
name_showing = false
order = 1162001
aliases = ["bp-r358-1"]
lean = ["AlgebraicGeometry.WeilGroup.frobeniusWeight_le_add_two_of_hasNonnegCoeffs", "AlgebraicGeometry.WeilGroup.frobeniusWeight_le_add_inv_two_pow_of_isReal"]
uses = ["situation-weil", "definition-weil-representation", "definition-determinant-weight", "definition-real-sheaves"]
+++
Let $U_0/\mathbf F_q$ be a smooth geometrically connected affine curve
with the coefficients and Weil group of Convention [situation-weil].
For a local Frobenius eigenvalue $\alpha$ at $x$, put

$$
\lambda_{\iota,x}(\alpha)
=\frac{2\log|\iota(\alpha)|}{\log q_x}.
$$

1. Let $\mathcal H$ be a lisse Weil sheaf, and suppose that every
   determinant weight of an irreducible constituent of $\mathcal H$ is
   at most $D\in\mathbf R$. If every inverse local factor
   $\iota\det(1-\operatorname{Frob}_xt^{\deg(x)}\mid\mathcal H_{\bar x})^{-1}$
   has nonnegative real coefficients, then
   $\lambda_{\iota,x}(\alpha)\le D+2$ for every local eigenvalue $\alpha$.
2. Let $\mathcal G$ be a lisse $\iota$-real Weil sheaf, and suppose that
   every determinant weight of an irreducible constituent of $\mathcal G$
   is at most $d\in\mathbf R$. Then, for every integer $j\ge0$,

   $$
   \lambda_{\iota,x}(\alpha)\le d+\frac1{2^j}
   \quad(x\in|U_0|,\ \alpha\text{ an eigenvalue on }\mathcal G_{\bar x}).
   $$

Neither assertion requires the sheaf to be nonzero.
