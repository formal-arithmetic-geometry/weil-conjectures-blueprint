+++
kind = "proof"
of = "corollary-point-counting-zeta-function--7"
order = 1039013
uses = ["corollary-point-counting-zeta-function--2", "corollary-point-counting-zeta-function--5", "corollary-point-counting-zeta-function--6", "lemma-hankel-rank-rationality", "lemma-reduced-fractions-integer-coefficients"]
+++
First suppose $X_0$ is separated. Choose a prime $\ell\nmid q$ and
form the trace datum from compactly supported cohomology as in
[corollary-point-counting-zeta-function--5]. The determinant product
expresses the image of $Z(X_0,T)$ in
$\overline{\mathbf Q}_\ell[[T]]$ as a fraction of polynomials whose
denominator has constant coefficient $1$.

Rationality descends to $\mathbf Q$ by
[lemma-hankel-rank-rationality]. In Lean this uses the finite-dimensional
span of shifts of the coefficient sequence: linear independence of
finitely many sequences is preserved by extending the coefficient
field, so finite-dimensionality descends. Integrality of the series
from [corollary-point-counting-zeta-function--6] and the integral
fraction theorem of [lemma-reduced-fractions-integer-coefficients]
then give $P,Q\in\mathbf Z[T]$ with $Q(0)=1$. The steps are assembled in
`AlgebraicGeometry.Scheme.Hom.zetaSeries_rational_of_traceDatum`, using
`TraceDatum.exists_rat_normalized_fraction`,
`TraceDatum.exists_int_normalized_fraction`, and
`PowerSeries.exists_int_fraction_of_rational`.

For general $X_0$ of finite type, choose a finite affine open cover.
For opens $W,U\subset X_0$, inclusion-exclusion for rational points
gives

$$
N_m(W\cup U)+N_m(W\cap U)=N_m(W)+N_m(U).
$$

The differential equations for the corresponding zeta series and
their constant coefficients $1$ imply
$Z(W\cup U,T)Z(W\cap U,T)=Z(W,T)Z(U,T)$.
When $U$ is affine, both $U$ and $W\cap U$ are separated, so their
zeta series have normalized integral fractions by the first case.
Their constant coefficients $1$ allow this identity to propagate such
a fraction from $W$ to $W\cup U$. Induction over the finite cover
proves the assertion, as in
`AlgebraicGeometry.Scheme.Hom.exists_int_mul_zetaSeries_eq`.
