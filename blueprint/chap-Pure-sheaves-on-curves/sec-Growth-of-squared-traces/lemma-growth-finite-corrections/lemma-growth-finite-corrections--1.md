+++
id = "lemma-growth-finite-corrections--1"
kind = "lemma"
title = "An additive bound for trace energies"
name_showing = false
order = 1205001
aliases = ["bp-r372-1"]
lean = ["AlgebraicGeometry.WeilSheaf.l2Weight_le_max_of_traceEnergy_le_add"]
uses = ["definition-growth-squared-traces"]
+++
The equality criterion for complexes above is bypassed in Lean by the
following one-sided comparison.

Let $k_0$ be a finite field with $q$ elements, let $\ell$ be a prime
different from its characteristic, and fix an embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\C$. Let $E$ and $F$
be constructible Weil sheaves on $k_0$-schemes $X_0$ and $Y_0$,
respectively. Use the trace energies $S_n(E)$ and $S_n(F)$ of
[definition-growth-squared-traces]; on arbitrary schemes each sum is
taken over its nonzero summands if there are finitely many, and is
assigned the value $0$ otherwise. Write

$$
\nu(E)=\sup\left\{\beta\in\mathbf R:
0<\limsup_{n\to\infty}\frac{S_n(E)}{q^{n(\beta+1)}}\right\},
$$

and similarly for $F$, with the limsup in $[0,+\infty]$ and the
supremum in $[-\infty,+\infty]$; the empty supremum is $-\infty$.
If $a,C\in\mathbf R$ satisfy

$$
S_n(E)\le S_n(F)+Cq^{na}
$$

for every natural number $n$ (including the level $0$ used in Lean),
then

$$
\nu(E)\le\max(\nu(F),a-1).
$$
