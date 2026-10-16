+++
id = "prop-weil-rationality-criterion"
kind = "theorem"
title = "Rationality criterion"
lean = ["Matrix.bddAbove_range_rank_submatrix_iff"]
order = 3231
tags = ["latex:proposition"]
uses = ["def-weil-field", "def-weil-formal-power-series", "def-weil-hankel-matrix", "lem-weil-finite-coordinate-detection"]
+++
Let $K$ be a field and
$C(T)=\sum_{n\geq0}c_nT^n\in K[[T]]$ a
formal power series.
The following conditions are equivalent:

1. $C=P/Q$ for polynomials $P,Q\in K[T]$ with $Q(0)=1$.
1. The Hankel rank of $C$ is finite.
1. There are integers $m\geq0,d\geq1$ and
$a_0,\ldots,a_{d-1}\in K$ such that
$$
c_{n+d}+a_{d-1}c_{n+d-1}+\cdots+a_0c_n=0
\qquad(n\geq m).
$$
