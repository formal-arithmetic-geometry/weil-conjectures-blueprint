+++
id = "chap-zla"
kind = "section"
title = "Zeta linear algebra"
order = 987
+++
This chapter is the purely algebraic endgame of the Weil conjectures: what one
can deduce about a power series

$$
Z(T)=\operatorname{Exp}\left(\sum_{n\geq1}N_n\frac{T^n}{n}\right)
$$

from the sole knowledge that its counting numbers $N_n$ are the alternating
sums of the traces of the iterates of an endomorphism on a finite family of
finite-dimensional vector spaces. No geometry and no cohomology enter here; the
input is a *trace datum* ([def-zla-trace-datum]), which is what the
Grothendieck–Lefschetz trace formula will eventually supply.

The two statements this material serves are

- `AlgebraicGeometry.Scheme.zetaSeries_rational` of
`WeilConjectures/Statement.lean`: the zeta series of a scheme of
finite type over a finite field is $P/Q$ with $P,Q\in\mathbf Z[T]$ and
$Q(0)=1$. The chain that produces it is
[prop-zla-cohomological-factorization] (rationality after scalar
extension), [thm-zla-hankel-descent] together with
[cor-zla-rationality-counting-field] (descent of rationality to
$\mathbf Q$), and [thm-zla-integral-fatou] (integrality of the
reduced fraction).
- `AlgebraicGeometry.IsWeilFactorization` of
`Comparator/Weil/Definitions.lean`: the factorization
$Z\cdot\prod_{i\text{ even}}P_i=\prod_{i\text{ odd}}P_i$ with
$P_i\in\mathbf Z[T]$, $P_i(0)=1$. Its factorization identity comes from
[prop-zla-cohomological-factorization], and the integrality of the
individual $P_i$ from
[prop-zla-parity-identification],
[prop-zla-unique-recovery] and
[prop-zla-factor-integrality], which separate the factors by
weight. The last section prepares the functional equation by computing
the reciprocal characteristic polynomial of the partner of a Frobenius
under a perfect similitude pairing
([thm-zla-degreewise-reciprocal]).

The source is the sketch article
`blueprint/src/version/sketch/49_zeta_linear_algebra.tex`, and only
the statements that are to be formalised in this subtree are reproduced here:
its sections on formal power series at the origin, locally finite products,
periodic permutations, closed points and the Hasse–Weil series, compatible
realizations, the middle pairing and its determinant sign, bounded graded
duality systems, the raw and normalized functional equations,
realization-independent constants and the final arithmetic theorem are
deliberately omitted, as are the derived-category formulation of a trace datum
and the statements about perfect complexes that go with it.

Throughout, $R[[T]]$ is the ring of formal power series over a commutative
ring $R$, identities in it are coefficientwise, and for a commutative
$\mathbf Q$-algebra $R$ we write

$$
\operatorname{Exp}(U)=\sum_{r\geq0}\frac{U^r}{r!}\in1+TR[[T]],
\qquad
\operatorname{Log}(1+V)=\sum_{r\geq1}(-1)^{r+1}\frac{V^r}{r}\in TR[[T]]
$$

for $U,V\in TR[[T]]$; both sums are coefficientwise finite.
