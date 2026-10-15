+++
id = "lem-weil-pbc-fpqc-descend-quasi-compact"
kind = "lemma"
title = "Quasi-compactness descends along flat surjective quasi-compact morphisms (Stacks 02KQ)"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.quasiCompact_of_fpqc_baseChange"]
+++
Let $g:S'\to S$ be a morphism of schemes [def-pc-scheme] which is flat `AlgebraicGeometry.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Flat.lean)), surjective `AlgebraicGeometry.Surjective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/UnderlyingMap.lean)) and quasi-compact [def-weil-finite-type-morphism] (the preimage of every affine open of $S$ is quasi-compact). Let $f:X\to S$ be a morphism of schemes and let $f':X\times_SS'\to S'$ be the second projection of the fibre product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). If $f'$ is quasi-compact, then $f$ is quasi-compact.
