+++
id = "lem-weil-pbc-irreducible-lisse-strata"
kind = "lemma"
title = "Irreducible lisse strata"
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.exists_stratification_isIrreducible"]
order = 1157
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-noetherian-finite-components"]
+++
Let $X$ be Noetherian and $F$ a constructible abelian etale sheaf on $X$.
There is a finite partition $X=\coprod_{i=1}^m S_i$ into nonempty irreducible
locally closed subschemes such that each $F|_{S_i}$ is locally constant with
finite stalks.
