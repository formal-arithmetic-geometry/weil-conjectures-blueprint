+++
id = "sk-prop-criterion"
kind = "lemma"
title = "Hankel rank and rationality"
order = 4101
lean = ["PowerSeries.exists_normalized_fraction_iff_finiteDimensional_shiftSpan"]
tags = ["sketch"]
+++
For a field $K$ and $C(T)=\sum_{n\geq0}c_nT^n\in K[[T]]$, the
following conditions are equivalent:

1. $C(T)$ is rational and regular at zero;
1. the finite minors of $(c_{r+s})_{r,s\geq0}$ have bounded rank;
1. the span of the rows $R_j=(c_{j+s})_{s\geq0}$ is finite-dimensional.

If $K\subset K'$ and $C$ has coefficients in $K$, rationality over
$K'$ implies rationality over $K$.
