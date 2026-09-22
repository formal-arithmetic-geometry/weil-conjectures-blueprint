+++
id = "lem-fin-dense-normal-open"
kind = "lemma"
title = "A dense normal open in an integral finite-type scheme"
order = 5168
lean = ["AlgebraicGeometry.exists_dense_normal_open_of_isIntegral"]
uses = ["def-sbc-normal-dominant-galois"]
+++
Every integral finite-type scheme over a field has a nonempty open subscheme
which is normal [def-sbc-normal-dominant-galois].

## Proof

Choose a nonempty affine open $\operatorname{Spec}B$ and take its
normalization in its own fraction field. The integral closure $C$ is a
finite $B$-module. Express its finitely many module generators as fractions
in $\operatorname{Frac}B$. A common nonzero denominator $b\in B$ gives
$C_b=B_b$. Since the integral closure is integrally closed and localization
preserves this property, $B_b$ is a normal domain. The nonempty open
$\operatorname{Spec}B_b$ is dense because $X$ is integral.

Unresolved dependencies: def:fin-normalization-extension, lem:fin-normalization-extension-finite, def:weil-pbc-scheme-conventions
