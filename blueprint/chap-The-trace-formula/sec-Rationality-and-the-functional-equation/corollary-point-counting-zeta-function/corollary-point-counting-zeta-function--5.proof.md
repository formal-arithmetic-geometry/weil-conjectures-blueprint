+++
kind = "proof"
of = "corollary-point-counting-zeta-function--5"
order = 1039011
uses = ["lemma-logarithm-determinant", "corollary-point-counting-zeta-function--2", "theorem-grothendieck-lefschetz-trace-formula--5"]
+++
Use the determinant-trace identity of [lemma-logarithm-determinant]
in its logarithmic derivative form
`LinearMap.X_mul_derivative_charpolyRev`:

$$
TP_i'(T)=-\left(\sum_{m\geq1}\operatorname{Tr}(F_i^m\mid V_i)T^m\right)P_i(T).
$$

The defining alternating trace identity for $N_m$ shows that
$Z_D\prod_{i\text{ even}}P_i$ and $\prod_{i\text{ odd}}P_i$ satisfy
the same differential equation $TA'=BA$, with $B(0)=0$.
Both have constant coefficient $1$. Comparing coefficients recursively
proves their equality. Mapping the exponential definition of $Z(X_0,T)$
from $\mathbf Q$ to $L$ gives the comparison with $Z_D$ when the
sequences of point counts agree.

For the cohomological application, compactly supported cohomology is
finite-dimensional and vanishes outside a finite interval, as in
[theorem-grothendieck-lefschetz-trace-formula--5]. Choose an even integer
$a_0$ below this interval and an integer $r\geq0$ such that
$[a_0,a_0+r]$ contains it. The spaces $V_j=H_c^{a_0+j}$ with their
Frobenius operators form a trace datum by
[corollary-point-counting-zeta-function--2]; the even shift preserves
the signs. Each $P_j$ has constant coefficient $1$ and is invertible as
a power series, so the displayed product identity gives the claimed
alternating determinant product. This is the construction inside
`AlgebraicGeometry.Scheme.Hom.exists_int_mul_zetaSeries_eq_of_isSeparated`.
