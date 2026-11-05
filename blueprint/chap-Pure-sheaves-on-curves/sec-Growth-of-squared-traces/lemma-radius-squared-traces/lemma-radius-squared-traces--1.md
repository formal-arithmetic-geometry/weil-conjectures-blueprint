+++
id = "lemma-radius-squared-traces--1"
kind = "lemma"
title = "Radius characterization for Weil sheaves"
name_showing = false
order = 1199001
aliases = ["bp-r370-1"]
lean = ["AlgebraicGeometry.WeilSheaf.l2Series", "AlgebraicGeometry.WeilSheaf.lt_l2Weight_iff"]
uses = ["definition-growth-squared-traces"]
+++
Let $k_0$ be a finite field of cardinality $q$, let $\ell$ be a prime
different from its characteristic, and fix an embedding
$\iota:\Qbarl\hookrightarrow\C$. Let $F$ be a constructible Weil
sheaf on a $k_0$-scheme $X_0$. Write $S_n(F)$ for its trace energy
as in [definition-growth-squared-traces]. For an arbitrary $X_0$, the
sum is taken over the nonzero summands when there are finitely many,
and is assigned the value $0$ otherwise.

Use the following form of the growth parameter:

$$
\nu(F)=\sup\left\{\gamma\in\R:
\limsup_{n\to\infty}\frac{S_n(F)}{q^{n(\gamma+1)}}>0\right\},
$$

where the limsup lies in $[0,+\infty]$, the supremum lies in
$[-\infty,+\infty]$, and the supremum of the empty set is $-\infty$.
Let $r_F\in[0,+\infty]$ be the radius of the real power series

$$
\varphi_F(t)=\sum_{n\ge1}S_n(F)t^{n-1}.
$$

For every $\beta\in\R$,

$$
\beta<\nu(F)\quad\Longleftrightarrow\quad r_F<q^{-(\beta+1)}.
$$

This characterizes $r_F=q^{-\nu(F)-1}$, with $r_F=+\infty$ when
$\nu(F)=-\infty$ and $r_F=0$ when $\nu(F)=+\infty$.
