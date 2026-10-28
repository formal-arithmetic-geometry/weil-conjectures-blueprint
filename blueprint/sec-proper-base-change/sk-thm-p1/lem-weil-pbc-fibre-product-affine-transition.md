+++
id = "lem-weil-pbc-fibre-product-affine-transition"
kind = "lemma"
title = "Affine transitions on compatible fibre products"
uses = ["def-pc-scheme", "pqf-def-affine-morphism"]
lean = ["AlgebraicGeometry.isAffineHom_pullback_map"]
order = 1861
+++
Let $X'\to S'\leftarrow T'$ and $X\to S\leftarrow T$ be diagrams of schemes [def-pc-scheme], and suppose there are compatible morphisms $X'\to X$, $S'\to S$, and $T'\to T$ commuting with the two structure maps. If all three comparison morphisms are affine [pqf-def-affine-morphism], then the induced morphism $X'\times_{S'}T'\to X\times_ST$ of fibre products is affine.
