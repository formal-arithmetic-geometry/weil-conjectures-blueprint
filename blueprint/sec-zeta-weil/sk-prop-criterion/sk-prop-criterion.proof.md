+++
kind  = "proof"
of    = "sk-prop-criterion"
+++
(1)$\Rightarrow$(3): clear the denominator $Q=1+a_{d-1}T+\dots+a_0T^{d}$;
the coefficients of $QC=P$ vanish beyond $\deg P$. (3)$\Rightarrow$(2): the
recurrence exhibits every column of $\mathcal H$ beyond the $m$-th as a fixed
linear combination of $d$ preceding columns, so the rank is $\le m+d$.
(2)$\Rightarrow$(1): if the rank is $d$, the first $d$ columns span all
columns, giving a linear recurrence; solving the resulting linear system
produces $Q$ of degree $d$ with $Q(0)=1$ and $P=QC$ a polynomial. This is the
Hankel/linear-recurrence dictionary, the same statement as the classical
criterion for a power series to be rational.
