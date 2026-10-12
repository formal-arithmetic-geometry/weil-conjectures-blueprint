+++
kind = "proof"
of = "lem-weil-pbc-affine-basic-set-difference"
+++
Define membership of a basic set as simultaneous membership of every g-coordinate in the prime ideal and nonmembership of f; this follows by unfolding toSet and zeroLocus. (`AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean))).

Induct on s. For s=0, choose the single basic set with g extended by h; its set is exactly the difference, and a singleton family is pairwise disjoint. (`AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean))).

For the successor step write C_prefix = D(h) ∩ V(k_1,...,k_s) and a = k_(s+1). Apply the induction hypothesis to B \ C_prefix. Construct E = D(fha) ∩ V(g_1,...,g_r,k_1,...,k_s). Since a product is outside a prime ideal exactly when each factor is outside, E = B ∩ C_prefix ∩ D(a). The new second basic set is C_prefix ∩ V(a). (`AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean))).

Prepend E to the old family. Every old piece lies in B \ C_prefix by the induction union equality, while E lies in C_prefix, so E is disjoint from every old piece. Old pieces remain pairwise disjoint. For each prime, split on membership in C_prefix: outside it the old union is exactly B; inside it the new difference is B ∩ D(a), exactly E. Thus B \ (C_prefix ∩ V(a)) is the union of E and the old family. (`AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean))).
