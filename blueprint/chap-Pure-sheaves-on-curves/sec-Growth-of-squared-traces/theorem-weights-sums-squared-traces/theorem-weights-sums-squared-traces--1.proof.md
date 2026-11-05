+++
kind = "proof"
of = "theorem-weights-sums-squared-traces--1"
order = 1208002
uses = ["definition-trace-function", "theorem-trace-formula-euler-product", "proposition-weights-under-usual-operations", "lemma-positivity-euler-factors", "lemma-positivity-convergence", "lemma-degree-zero-top-cohomology", "lemma-extreme-degrees-affine-curve", "lemma-radius-squared-traces", "lemma-bounds-squared-traces"]
+++
Put $\mathcal T=\mathcal G\otimes\mathcal G$ and
$L(t)=L(X_0,\mathcal T,t)$. By
[proposition-weights-under-usual-operations], $\mathcal T$ is lisse and
pure of weight $2w$. Since the traces of $\mathcal G$ are real, at
$x\in X_0(k_n)$ we have
$\iota t_{\mathcal T,n}(x)=|\iota t_{\mathcal G,n}(x)|^2$.
Grouping the local logarithmic
derivatives by degree gives the formal power-series identity

$$
\varphi_{\mathcal G}(t)L(t)=L'(t).
$$

This is the real case of
`AlgebraicGeometry.WeilSheaf.traceFunction_tensorObj_and_l2Series_mul_lSeries`.
It implies $\operatorname{rad}(\varphi_{\mathcal G})\le
\operatorname{rad}(L)$ by
`PowerSeries.radius_le_radius_of_derivative_eq_mul`.

We first show that $L$ has finite radius of convergence. A nonzero
sheaf has a nonzero stalk at some closed point $x$. The Frobenius on
$\mathcal T_{\bar x}$ is invertible and this stalk has positive rank,
so the polynomial

$$
Q_x(t)=\iota\det(1-\operatorname{Frob}_x t^{\deg(x)}
\mid\mathcal T_{\bar x})
$$

is nonconstant and has constant coefficient one. Choose a complex
root $z$ of $Q_x$. The local factor $Q_x^{-1}$ has radius at most
$|z|$. By [lemma-positivity-euler-factors], all the local factors have
nonnegative coefficients and constant coefficient one. Thus
[lemma-positivity-convergence] gives
$\operatorname{rad}(L)\le\operatorname{rad}(Q_x^{-1})\le|z|<\infty$.

The trace formula [theorem-trace-formula-euler-product] and the
cohomological vanishing in [lemma-degree-zero-top-cohomology] give

$$
L(t)D(t)=N(t),\qquad
D(t)=\iota\det(1-Ft\mid H_c^2(X,\mathcal T)),\qquad
N(t)=\iota\det(1-Ft\mid H_c^1(X,\mathcal T)).
$$

Lean uses
`AlgebraicGeometry.WeilSheaf.lSeries_mul_localPolynomial_compactlySupportedCohomology_two`
for this identity. Apply [lemma-extreme-degrees-affine-curve] to the
identity open immersion: $H_c^2(X,\mathcal T)$ is pure of weight
$2w+2$, so every root of $D$ has absolute value $R=q^{-w-1}$.
Since $D(0)=1$ and $L$ has finite radius,
`PowerSeries.radius_le_of_mul_coe_eq` gives
$\operatorname{rad}(L)\le R$. Indeed, after cancelling the common
factors of $N$ and $D$, the denominator is nonconstant, and any of its
roots is a pole and is still a root of $D$.

Consequently $\operatorname{rad}(\varphi_{\mathcal G})\le R$.
For every real $\beta<w$, this implies
$\operatorname{rad}(\varphi_{\mathcal G})<q^{-\beta-1}$; the strict
radius criterion in [lemma-radius-squared-traces] gives
$\beta<\nu(\mathcal G)$. Hence $w\le\nu(\mathcal G)$.
The opposite inequality follows from [lemma-bounds-squared-traces](1),
and the two inequalities prove the assertion.
