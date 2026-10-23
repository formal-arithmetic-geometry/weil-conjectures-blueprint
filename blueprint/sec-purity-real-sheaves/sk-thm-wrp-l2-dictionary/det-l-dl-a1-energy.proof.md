+++
kind  = "proof"
of    = "det-l-dl-a1-energy"
+++
Let $T_v$ be the constant Weil line whose Frobenius has realization
$q^v$, and set $N^c=N^\vee\otimes T_v$. The line $T_v$ has weight
$2v$, while $N^c$ has weight $v$ and conjugate realized local spectra.
Thus $D=N\otimes N^c$ has weight $2v$ and point traces
$|\iota t_{N,n}(x)|^2$. The trace formula and the determinant identity give

$$
E_N(T):=\exp\left(\sum_{n\ge1}S_n(V_0,N)\frac{T^n}{n}\right)
=\frac{\iota\det(1-T\DLAFr_q\mid H_c^1(V,D))}
{\iota\det(1-T\DLAFr_q\mid H_c^2(V,D))}.
$$

There is a closed point with a nonzero stalk. Some positive power of its
invertible Frobenius has nonzero trace; otherwise the determinant
identity would make its characteristic polynomial constant. Hence some
$S_n$ is positive. All $S_n$ are nonnegative, so the exponential has
infinitely many nonzero coefficients: a positive coefficient in its
exponent contributes positively in arbitrarily high powers.
Consequently the rational function $E_N$ is not a polynomial and has
at least one surviving finite pole.

By [sk-lem-wrp-hc2] and [lem-a1-affine-hc2], $H_c^2(V,D)$ is pure of weight $2v+2$,
so every possible denominator pole has modulus $q^{-(v+1)}$.
The assumed energy bound makes the series in the exponential converge
for $|T|<q^{-B}$. Its analytic exponential is holomorphic there and
agrees with the rational germ; therefore the surviving pole cannot lie
in that disk. Thus $q^{-(v+1)}\ge q^{-B}$, or $v\le B-1$.
This argument uses no weight estimate for $H_c^1(V,D)$ and requires
only one surviving pole, rather than noncancellation of every factor.
