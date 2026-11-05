+++
kind = "proof"
of = "corollary-point-counting-zeta-function--4"
order = 1039010
uses = ["corollary-point-counting-zeta-function--3"]
+++
Fix $n$. There are only finitely many closed points of degree at most
$n$, and all degrees are positive. Hence the coefficient of $T^n$ in
the infinite product is that in the finite product over these points.
This is the truncation used in
`PowerSeries.coeff_tprod_inv_one_sub_X_pow`.

Write $N_m=\#X_0(\mathbf F_{q^m})$. Counting the points above each
closed point gives

$$
N_m=\sum_{\deg(x)\mid m}\deg(x)\qquad(m\geq1),
$$

as in `AlgebraicGeometry.Scheme.Hom.pointCount_eq_sum`.
By the exponential definition in
[corollary-point-counting-zeta-function--3], the series $Z$ satisfies

$$
TZ'(T)=\left(\sum_{m\geq1}N_mT^m\right)Z(T),\qquad Z(0)=1.
$$

The finite product has the same logarithmic derivative through degree
$n$, by the point-counting identity, and the same constant coefficient.
The coefficient recurrence in
`PowerSeries.coeff_eq_of_X_mul_derivative_eq` therefore identifies
the coefficients through degree $n$. Since $n$ was arbitrary, the
Euler product follows.
