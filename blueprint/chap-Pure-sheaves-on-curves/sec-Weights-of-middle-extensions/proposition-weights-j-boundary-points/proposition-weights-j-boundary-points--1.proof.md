+++
kind = "proof"
of = "proposition-weights-j-boundary-points--1"
order = 1180002
uses = ["theorem-trace-formula-euler-product", "lemma-point-count-bound", "lemma-extreme-degrees-affine-curve", "lemma-degree-zero-top-cohomology", "lemma-filtrations-spectra"]
+++
Put $J=j_*\mathcal F$ and $Z_0=X_0-U_0$. At a closed point of $U_0$,
the stalk of $J$ is that of $\mathcal F$, with the same Frobenius, so the
required bound is the hypothesis. The set of boundary points is finite.
We first bound their weights by $a+2$.

Write $P_i(t)=\det(1-\operatorname{Frob}_q t\mid H_c^i(X,J))$ and

$$
B(t)=\prod_{z\in Z_0}
\det(1-\operatorname{Frob}_z t^{\deg(z)}\mid J_{\bar z}).
$$

The trace formula [theorem-trace-formula-euler-product] and the vanishing
outside degrees $1,2$ in [lemma-extreme-degrees-affine-curve] give the
identity of formal power series

$$
L(U_0,\mathcal F,t)P_2(t)=P_1(t)B(t).
$$

In Lean this is obtained by splitting the coefficientwise Euler-product
identity `AlgebraicGeometry.WeilSheaf.coeff_prod_inv_localPolynomial_stalk_directImage`
into the open part and the finite boundary.

The ranks of the stalks of $\mathcal F$ are bounded, and its local
eigenvalues have absolute value at most $q_x^{a/2}$ under $\iota$.
The point-count bound [lemma-point-count-bound], applied on $X_0$, bounds
the number of closed points of degree $n$ in the open part by $Aq^n$.
These estimates give convergence of the inverse Euler product
$(\iota L(U_0,\mathcal F,t))^{-1}$ on $|t|<q^{-a/2-1}$.

By [lemma-extreme-degrees-affine-curve],
$H_c^2(X,J)=V_{\pi_1(U)}(-1)$, where $V$ is the geometric generic fibre
of $\mathcal F$. The geometric coinvariants have weights at most $a$:
they are dual to the global sections of $\mathcal F^\vee$, and the
global-section eigenvalues are detected, after taking powers, on closed
stalks. This is the upper-bound argument of
[lemma-degree-zero-top-cohomology], implemented by
`AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_geometricCoinvariants`.
Thus the eigenvalues on $H_c^2(X,J)$ have absolute value at most
$q^{a/2+1}$, and $(\iota P_2)^{-1}$ converges on the same disc.

The displayed identity now gives

$$
(\iota B)^{-1}
=\iota P_1\,(\iota P_2)^{-1}
  (\iota L(U_0,\mathcal F,t))^{-1}.
$$

The right side converges on that disc. Hence $\iota B$ has no zero
there; this is `PowerSeries.one_le_mul_norm_of_tprod_mul_eq_mul`.
For an eigenvalue $\alpha$ at $z$, a root of
$1-\iota(\alpha)t^{\deg(z)}$ therefore has absolute value at least
$q^{-a/2-1}$, giving

$$
|\iota(\alpha)|\le q_z^{a/2+1}.
$$

This is the preliminary bound
`AlgebraicGeometry.WeilSheaf.norm_le_of_hasEigenvalue_stalk_directImage`.

For every $m\ge1$, the tensor power $\mathcal F^{\otimes m}$ is lisse,
and [lemma-filtrations-spectra] shows that it is punctually of weights
$\le ma$.
Moreover, $\alpha^m$ is an eigenvalue on
$(j_*(\mathcal F^{\otimes m}))_{\bar z}$.
Lean proves this directly for sheaves: represent a nonzero eigenvector
by the germ of a section, take its tensor powers, and use the natural
pairings of direct images to check the Frobenius action. The resulting
germs are nonzero because $\mathcal F$ is lisse. This is
`AlgebraicGeometry.WeilSheaf.hasEigenvalue_stalk_directImage_tensorPow`.
Applying the preliminary bound gives

$$
|\iota(\alpha)|^m\le q_z^{ma/2+1}.
$$

Taking logarithms, dividing by $m$, and letting $m$ grow proves
$|\iota(\alpha)|\le q_z^{a/2}$.
