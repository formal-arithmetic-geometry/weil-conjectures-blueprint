+++
id = "cor-trf-point-counting"
kind = "theorem"
title = "Point-counting trace formula"
order = 2745
tags = ["latex:corollary"]
uses = ["cor-trf-constant-stalk-trace", "def-trf-frobenius-operators", "def-weil-finite-field-fiber", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-etale-origin-witness", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "thm-trf-grothendieck-lefschetz-qbar"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, let $X_0$ be a
separated finite-type
$k_0$-scheme, put $X=X_0\times_{k_0}k$, and let
$K=(\Qlb)_X$ be the constant
Weil sheaf with its canonical
Weil structure, the geometric Frobenius acting trivially. Assume
the compactification admissibility of
[thm-trf-grothendieck-lefschetz-qbar] for the constant lattice
$(\mathcal O_E)_X$ of $E_X$ at every finite level (the etale-origin
witnesses required there are supplied in the proof). Then for every
$m\geq1$,

$$
\#X_0(\mathbf F_{q^m})
=
\sum_{i\in\mathbf Z}(-1)^i
\operatorname{Tr}\bigl(F^m\mid H_c^i(X,\Qlb)\bigr),
$$

and, when $X_0$ is
proper,

$$
\#X_0(\mathbf F_{q^m})
=
\sum_{i\in\mathbf Z}(-1)^i
\operatorname{Tr}\bigl(F^m\mid H^i(X,\Qlb)\bigr),
$$

compactly supported cohomology being the ordinary one.
