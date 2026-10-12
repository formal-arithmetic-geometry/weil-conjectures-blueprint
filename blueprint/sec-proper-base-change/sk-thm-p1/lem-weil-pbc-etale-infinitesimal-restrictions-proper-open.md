+++
id = "lem-weil-pbc-etale-infinitesimal-restrictions-proper-open"
kind = "lemma"
title = "An open containing the closed fiber of a proper scheme over a complete base is everything"
uses = ["def-pc-base-change"]
lean = ["AlgebraicGeometry.proper_closed_fiber_open_eq_top"]
source = "literature/stacks-project/pione.tex, Fundamental Groups, Lemma 0GS2"
+++
Let A be a commutative ring complete for an ideal I `IsAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)). Let f : Y → Spec A `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean)) and g : X → Y be scheme morphisms with g followed by f proper `AlgebraicGeometry.IsProper` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Proper.lean)). Let W be an open subset of X containing g⁻¹(image(Y ×_A Spec(A/I) → Y)) [def-pc-base-change], `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). Then W = X.
