+++
id = "prop-finite-compact-support-constructibility"
kind = "theorem"
title = "Finite-level bounded constructibility for proper support"
order = 48
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image", "def-constructible-interval", "def-weil-finite-coefficient-datum", "prop-finite-extension-by-zero-properties", "prop-finite-proper-direct-image"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and $n\geq1$. For every
separated finite-type $f:X\to Y$, the preceding functor lands
in bounded constructible complexes and hence is an exact triangulated
functor

$$
Rf_{!,n}:D^b_c\bigl(X,\mathcal O_E/\varpi_E^n\bigr)
\longrightarrow D^b_c\bigl(Y,\mathcal O_E/\varpi_E^n\bigr).
$$

For each cohomological interval $[a,b]$ and each upper bound on the
relative dimension of $f$, there is an interval $[a',b']$, independent
of the compactification, such that, for every
$K\in D_c^{[a,b]}(X,\mathcal O_E/\varpi_E^n)$,

$$
Rf_{!,n}K\in
D_c^{[a',b']}\bigl(Y,\mathcal O_E/\varpi_E^n\bigr).
$$

Bounded constructibility follows after a compactification from finite-level
extension by zero and proper finiteness in Proposition
[prop-finite-proper-direct-image]. The compactification-independent
interval $[a',b']$ is the compact-support cohomological-dimension bound; it
is an additional part of the finite-level finiteness theorem and is not
deduced from proper base change alone.
