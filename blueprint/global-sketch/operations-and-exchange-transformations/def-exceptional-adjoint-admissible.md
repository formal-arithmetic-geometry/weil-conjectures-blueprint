+++
id = "def-exceptional-adjoint-admissible"
kind = "definition"
title = "Exceptional-adjoint admissibility"
order = 54
uses = ["def-compact-support-candidate", "def-compact-support-direct-image", "def-constructible-interval", "def-finite-tor-amplitude", "def-full-cohomological-dimension", "def-qbar-coefficient-category", "def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "prop-ambient-exceptional-adjoint", "prop-compactification-coherence"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let $n\geq1$, let
$f:X\to Y$ be separated and of finite type, and
choose a compactification
$X\xrightarrow{j}\overline X\xrightarrow{p}Y$. Say that $f$ is
*exceptional-adjoint admissible at
$\mathcal O_E/\varpi_E^n$* if:

1. $\operatorname{FullCD}(p,\mathcal O_E/\varpi_E^n;c)$ holds for some
integer $c\geq0$, and
$Rf_n^{\times}$ is the ambient right adjoint furnished by
Proposition [prop-ambient-exceptional-adjoint];
1. there is an integer $c_f$ such that, for every pair of integers
$a\leq b$ and
every $L\in D_c^{[a,b]}(Y,\mathcal O_E/\varpi_E^n)$,
$$
Rf_n^{\times}L\in
D_c^{[a-c_f,b]}\bigl(X,\mathcal O_E/\varpi_E^n\bigr)
$$
;
1. for every
$L\in D^b_{ctf}(Y,\mathcal O_E/\varpi_E^n)$, one has
$$
Rf_n^{\times}L\in
D^b_{ctf}\bigl(X,\mathcal O_E/\varpi_E^n\bigr).
$$
1. for any two compactifications satisfying the preceding conditions,
the mate of the constructible coherence isomorphism in
Proposition [prop-compactification-coherence] identifies the restrictions
of their ambient right adjoints to $D^b_c$, and these identifications
satisfy the cocycle condition.

At the $\mathcal O_E$, $E$, or $\Qlb$ stage, admissibility means that
these hypotheses hold at the finite stages with uniform bounds and that the
finite-reduction and scalar-extension comparisons for the representing
objects are isomorphisms. Admissibility is always an explicit hypothesis;
it is not inferred from separated finite type alone.
