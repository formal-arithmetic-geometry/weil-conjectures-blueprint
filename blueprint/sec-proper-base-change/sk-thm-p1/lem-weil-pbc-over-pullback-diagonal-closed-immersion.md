+++
id = "lem-weil-pbc-over-pullback-diagonal-closed-immersion"
kind = "lemma"
title = "Closed immersion of the Over-base-changed diagonal detects separatedness"
uses = ["def-pc-base-change", "def-pc-scheme"]
lean = ["AlgebraicGeometry.isClosedImmersion_overPullback_diagonal_iff"]
order = 2007
+++
Let S,T be schemes [def-pc-scheme], g:T→S a morphism, X→S and Y→S schemes over S, and f:X→Y an S-morphism. Give X ×_Y X its structure map to S using the second projection to X. Let γ:X→X ×_Y X be the diagonal as an S-morphism. Then the base change γ_T along g [def-pc-base-change] is a closed immersion if and only if the base change f_T is separated. No compactness or finiteness hypothesis is imposed.
