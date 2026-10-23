+++
id = "lem-weil-pbc-irreducible-lisse-strata"
kind = "lemma"
title = "Irreducible lisse strata"
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.exists_stratification_isIrreducible"]
order = 1598
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-noetherian-finite-components"]
+++
Let $X$ be a Noetherian scheme, $\Lambda$ a finite commutative ring, and $F$ a constructible sheaf of $\Lambda$-modules on the small etale site of $X$ [def-weil-pbc-etale-sheaves]. There is a stratification of $X$, i.e. a finite partition $X=\coprod_{i=1}^m S_i$ into locally closed subsets together with immersions of schemes $S_i\hookrightarrow X$ with image $S_i$, such that every $S_i$ is irreducible (in particular nonempty) and each inverse image $F|_{S_i}$ is finite locally constant, i.e. locally constant with finite stalks.
