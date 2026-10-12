+++
id = "lem-weil-pbc-over-pullback-diagonal-closed-immersion"
kind = "lemma"
title = "Closed immersion of the Over-base-changed diagonal detects separatedness"
uses = ["def-pc-base-change", "def-pc-scheme"]
lean = ["AlgebraicGeometry.isClosedImmersion_overPullback_diagonal_iff"]
source = "literature/stacks-project/limits.tex, Tag 01ZQ, lemma-descend-separated-finite-presentation, proof: diagonal base-change identification; expanded by the agent directly from fibre-product universal properties"
+++
Let S,T be schemes [def-pc-scheme], g:T→S a morphism, X→S and Y→S schemes over S, and f:X→Y an S-morphism. Give X ×_Y X `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)) its structure map to S using the second projection to X. Let γ:X→X ×_Y X be the diagonal as an S-morphism. Then the base change γ_T along g [def-pc-base-change] is a closed immersion `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)) if and only if the base change f_T is separated `AlgebraicGeometry.IsProper` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Proper.lean)). No compactness or finiteness hypothesis is imposed.
