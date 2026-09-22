+++
id = "cor-pqf-proper-quasifinite-finite"
kind = "theorem"
title = "Proper quasi-finite morphisms are finite"
order = 3241
lean = ["AlgebraicGeometry.isFinite_of_isProper_of_quasiFinite"]
tags = ["latex:corollary"]
uses = ["pqf-def-locnoeth", "pqf-def-quasifinite", "pqf-lem-qf-finitefibres", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $f:X\to S$ be a morphism of schemes with $S$ locally Noetherian
[pqf-def-locnoeth]. If $f$ is proper and quasi-finite
[pqf-def-quasifinite], then $f$ is finite.

## Proof

A quasi-finite morphism has finite fibres by [pqf-lem-qf-finitefibres];
hence $f$ is proper with finite fibres in the sense of
[pqf-def-quasifinite], and [thm-pqf-finite-iff-proper-finite-fibres]
applies, giving that $f$ is finite.

Unresolved dependencies: def:weil-pbc-scheme-conventions
