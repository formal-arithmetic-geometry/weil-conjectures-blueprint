+++
id = "sk-prop-criterion"
kind = "proposition"
title = "Rationality criterion"
order = 3228
lean = ["PowerSeries.exists_normalized_fraction_iff_finiteDimensional_shiftSpan"]
uses = ["sk-def-roots"]
tags = ["sketch"]
+++
Let $K$ be a field and $C(T)=\sum_{n\ge0}c_nT^{n}\in K[[T]]$. The following
are equivalent:

1. there are $P,Q\in K[T]$ with $Q(0)=1$ and $QC=P$ in $K[[T]]$;
1. the shift span of $(c_n)_{n\ge0}$, i.e. the $K$-span of the shifted
sequences $(c_{n+m})_{n\ge0}$, $m\ge0$ (the rows of the Hankel matrix
$\mathcal H(C)=(c_{r+s})_{r,s\ge0}$), is finite-dimensional.
