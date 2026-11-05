+++
kind = "proof"
of = "lemma-growth-finite-corrections--1"
order = 1205002
uses = ["definition-growth-squared-traces"]
+++
Let $\beta$ be real with $\beta>\nu(F)$ and $\beta>a-1$. By the
definition of $\nu(F)$, the nonnegative sequence
$S_n(F)/q^{n(\beta+1)}$ has limsup $0$ in $[0,+\infty]$, and hence
tends to $0$. Since $q>1$ and $a-\beta-1<0$, the positive part of
$Cq^{n(a-\beta-1)}$ also tends to $0$. This is the geometric-decay
step `limsup_eq_zero_of_le` in Lean.

Dividing the assumed inequality by $q^{n(\beta+1)}$ gives

$$
0\le\frac{S_n(E)}{q^{n(\beta+1)}}
\le\frac{S_n(F)}{q^{n(\beta+1)}}
  +\max(Cq^{n(a-\beta-1)},0).
$$

The right-hand side tends to $0$, so the normalized trace energies
of $E$ have limsup $0$. Thus no real $\beta$ with positive defining
limsup for $E$ can exceed $\max(\nu(F),a-1)$. Taking the supremum
over those $\beta$ gives the asserted inequality.
