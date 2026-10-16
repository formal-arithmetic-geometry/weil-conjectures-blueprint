+++
id = "thm-weil-karoubian-bounded-t"
kind = "theorem"
title = "Bounded t-structures are Karoubian"
lean = ["CategoryTheory.Triangulated.TStructure.isIdempotentComplete_of_bounded", "CategoryTheory.Triangulated.TStructure.isEquivalence_toKaroubi_of_bounded", "CategoryTheory.Triangulated.TStructure.isEquivalence_toKaroubi_and_isTriangulated_of_bounded"]
order = 1482
uses = ["def-weil-karoubi-envelope", "def-weil-t-structure", "lem-weil-envelope-tstructure", "lem-weil-karoubi-envelope-fully-faithful", "lem-weil-karoubi-envelope-idempotent-complete", "lem-weil-karoubi-envelope-triangulated", "prop-weil-heart-abelian"]
+++
If a triangulated category $\mathcal T$ has a bounded t-structure, then
$\mathcal T$ is idempotent complete: every idempotent $e:K\to K$ of $\mathcal
T$ splits, and the canonical fully faithful functor $\mathcal T\to\Kar(\mathcal
T)$ of [def-weil-karoubi-envelope] is an exact equivalence.
