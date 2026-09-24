+++
id = "lem-weil-pbc-finite-hypercover-descent"
kind = "lemma"
title = "Finite hypercover skeleta descend"
order = 1218
uses = ["def-weil-pbc-finite-split-hypercover", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-finite-data-descent"]
+++
Let $(X_i)$ be a cofiltered inverse system of quasi-compact quasi-separated
[def-weil-pbc-scheme-conventions] schemes with affine transition maps and
limit $X$. For each $r\geq0$, a truncation through degree $r$ of a split
etale hypercover finite in each degree
[def-weil-pbc-finite-split-hypercover], every morphism between two such
truncations, and every equality between such morphisms descend to one finite
stage $X_i$. The descended matching maps are covers at a sufficiently late
stage.

## Proof

The finite-presentation requirement is part of
[def-weil-pbc-finite-split-hypercover]; it does not follow just from
truncating a simplicial object. There are finitely many nondegenerate terms,
face maps, and simplicial identities through degree $r$. Apply
[lem-weil-pbc-etale-finite-data-descent] to these data, including the
splitting isomorphisms. Matching schemes are finite limits, so their
formation commutes with base change. The last assertion of that lemma makes
each of the finitely many descended matching maps a cover at a common later
stage. The same finite-data argument descends morphisms and equalities. If a
full hypercover is needed at that stage, continue above degree $r$ by taking
the matching scheme itself as a new nondegenerate covering term in each
degree.
