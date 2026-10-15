+++
id = "lem-weil-pbc-fpqc-descend-separated"
kind = "lemma"
title = "Separatedness descends along flat surjective quasi-compact morphisms (Stacks 02KU)"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.isSeparated_of_flat_surjective_baseChange"]
+++
Let $g:S'\to S$ be a morphism of schemes [def-pc-scheme] which is flat `AlgebraicGeometry.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Flat.lean)), surjective `AlgebraicGeometry.Surjective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/UnderlyingMap.lean)) and quasi-compact [def-weil-finite-type-morphism]. Let $f:X\to S$ be a morphism of schemes and let $f':X\times_SS'\to S'$ be the second projection of the fibre product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). If $f'$ is separated `AlgebraicGeometry.IsProper` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Proper.lean)) (its diagonal $X\times_SS'\to(X\times_SS')\times_{S'}(X\times_SS')$ is a closed immersion), then $f$ is separated.
