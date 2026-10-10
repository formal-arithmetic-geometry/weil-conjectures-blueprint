+++
id = "sk-prop-criterion"
kind = "section"
title = "Rationality criterion"
order = 2885
lean = ["PowerSeries.exists_normalized_fraction_iff_finiteDimensional_shiftSpan"]
uses = ["sk-def-roots"]
+++
*Proposition (sketch).*

Let $K$ be a field and $C(T)=\sum_{n\ge0}c_nT^{n}\in K[[T]]$. The following
are equivalent:

1. there are $P,Q\in K[T]$ with $Q(0)=1$ and $QC=P$ in $K[[T]]$;
1. the shift span of $(c_n)_{n\ge0}$, i.e. the $K$-span of the shifted
sequences $(c_{n+m})_{n\ge0}$, $m\ge0$ (the rows of the Hankel matrix
$\mathcal H(C)=(c_{r+s})_{r,s\ge0}$), is finite-dimensional.

## Proof

(1)$\Rightarrow$(3): clear the denominator $Q=1+a_{d-1}T+\dots+a_0T^{d}$;
the coefficients of $QC=P$ vanish beyond $\deg P$. (3)$\Rightarrow$(2): the
recurrence exhibits every column of $\mathcal H$ beyond the $m$-th as a fixed
linear combination of $d$ preceding columns, so the rank is $\le m+d$.
(2)$\Rightarrow$(1): if the rank is $d$, the first $d$ columns span all
columns, giving a linear recurrence; solving the resulting linear system
produces $Q$ of degree $d$ with $Q(0)=1$ and $P=QC$ a polynomial. This is the
Hankel/linear-recurrence dictionary, the same statement as the classical
criterion for a power series to be rational.
