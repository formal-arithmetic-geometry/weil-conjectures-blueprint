+++
id = "lem-weil-pbc-fibre-product-affine-transition"
kind = "lemma"
title = "Affine transitions on compatible fibre products"
uses = ["def-pc-scheme", "pqf-def-affine-morphism"]
lean = ["AlgebraicGeometry.isAffineHom_pullback_map"]
source = "literature/stacks-project/morphisms.tex, Lemmas Tags 01SD (base change of affine morphisms), 01SC (composition of affine morphisms), and 01SG (affine permanence), applied to the compatible fibre-product square; the diagonal of the affine morphism S' -> S is affine because affine morphisms are separated"
+++
Let $X'\to S'\leftarrow T'$ and $X\to S\leftarrow T$ be diagrams of schemes [def-pc-scheme], and suppose there are compatible morphisms $X'\to X$, $S'\to S$, and $T'\to T$ commuting with the two structure maps. If all three comparison morphisms are affine [pqf-def-affine-morphism], then the induced morphism $X'\times_{S'}T'\to X\times_ST$ of fibre products `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)) is affine.
