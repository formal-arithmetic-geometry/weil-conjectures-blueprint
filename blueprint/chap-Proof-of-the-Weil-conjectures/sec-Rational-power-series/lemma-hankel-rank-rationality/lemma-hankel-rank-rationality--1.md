+++
id = "lemma-hankel-rank-rationality--1"
kind = "lemma"
title = "Hankel rank and rationality (1)"
name_showing = false
order = 1379001
aliases = ["bp-r425-1"]
lean = ["PowerSeries.exists_normalized_fraction_iff_finiteDimensional_shiftSpan", "Matrix.bddAbove_range_rank_submatrix_iff"]
+++
For a field $K$ and $C(T)=\sum_{n\geq0}c_nT^n\in K[[T]]$, the
following conditions are equivalent:

1. $C(T)$ is rational and regular at zero;
2. the finite submatrices of $(c_{r+s})_{r,s\geq0}$ have bounded rank;
3. the span of the rows $R_j=(c_{j+s})_{s\geq0}$ is finite-dimensional.
