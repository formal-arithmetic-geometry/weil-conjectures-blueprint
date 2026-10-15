+++
id = "lem-weil-pbc-fpqc-descend-finite"
kind = "lemma"
title = "Being finite descends along fpqc coverings (Stacks 02LA)"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.isFinite_of_fpqc_cover"]
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme] and let $\{g_i:S_i\to S\}_{i\in I}$ be an fpqc covering of $S$ `AlgebraicGeometry.Scheme.fpqcPrecoverage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean)). For $i\in I$ let $f_i:X\times_SS_i\to S_i$ be the base change of $f$ along $g_i$, the second projection of the fibre product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). If $f_i$ is finite `AlgebraicGeometry.IsFinite, AlgebraicGeometry.IsIntegralHom` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Finite.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Integral.lean)) for every $i\in I$, then $f$ is finite.
