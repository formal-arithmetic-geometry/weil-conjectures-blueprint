+++
id = "lemma-hankel-rank-rationality--1"
kind = "lemma"
title = "Rationality and the shift span"
name_showing = false
order = 1376001
aliases = ["bp-r425-1"]
lean = ["PowerSeries.exists_normalized_fraction_iff_finiteDimensional_shiftSpan"]
uses = []
+++
The bounded-rank condition on finite Hankel submatrices is bypassed by
the Lean route, which uses the shift span directly.

For a field $K$ and $C(T)=\sum_{n\geq0}c_nT^n\in K[[T]]$, the
following conditions are equivalent:

1. there are $P,Q\in K[T]$ with $Q(0)=1$ and $C(T)Q(T)=P(T)$;
2. the $K$-span of the rows $R_j=(c_{j+s})_{s\geq0}$ is finite-dimensional.

The first condition says that $C(T)$ is rational and regular at zero.
