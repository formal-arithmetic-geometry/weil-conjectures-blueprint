+++
id = "cor-zl-all-realization-purity"
kind = "theorem"
title = "Purity for every chosen realization"
order = 3085
tags = ["latex:corollary"]
uses = ["cor-zl-purity-smooth-proper", "def-weil-finite-field-fiber", "def-weil-punctual-weights", "def-weil-smooth-proper-cohomological-family"]
+++
Let $X_0$ be a smooth proper pure-dimensional separated finite-type
$k_0$-scheme. For every field isomorphism
$\iota:\Qlb\xrightarrow{\sim}\mathbf C$, every reciprocal root of the
cohomological
factor $P_i(X_0,T)$ has $\iota$-absolute value $q^{i/2}$.

## Proof

Fix the displayed isomorphism and use it as the realization in the
coefficient datum. The theorem
[cor-zl-purity-smooth-proper] applies with this choice and gives
modulus $q^{i/2}$ for every Frobenius eigenvalue of $F$ on
$H^i(X,\Qlb)$; these eigenvalues are precisely the reciprocal roots
of the determinant $P_{i,\ell}$ by
[def-weil-smooth-proper-cohomological-family], giving the
assertion.
