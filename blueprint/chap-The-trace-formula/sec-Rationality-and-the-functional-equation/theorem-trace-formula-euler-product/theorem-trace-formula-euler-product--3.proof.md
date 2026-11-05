+++
kind = "proof"
of = "theorem-trace-formula-euler-product--3"
order = 1036009
uses = ["theorem-trace-formula-euler-product--2"]
+++
For each $n$, take the finite set of closed points of degree at most
$n$. Every factor outside this set is $1$ modulo $T^{n+1}$, by
[theorem-trace-formula-euler-product--2]. Consequently the coefficients
through degree $n$ are unchanged by enlarging a partial product once
this set is included.

The power-series product criterion
`PowerSeries.WithPiTopology.hasProd_of_X_pow_dvd_sub_one` gives
multipliability. The definition of
`AlgebraicGeometry.WeilSheaf.lSeries` then identifies the limit with
$L_\iota(X_0,\mathcal F,T)$; the resulting assertion is
`AlgebraicGeometry.WeilSheaf.hasProd_lFactor`.
