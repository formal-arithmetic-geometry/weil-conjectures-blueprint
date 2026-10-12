+++
kind = "proof"
of = "lem-weil-pbc-etale-infinitesimal-restrictions-proper-open"
uses = ["def-pc-base-change"]
+++
Set h = g followed by f. The complement C of W is closed, so properness makes h(C) closed in Spec A. Write it as V(K). If x belongs to C, then K is contained in the prime ideal h(x), which is contained in a maximal ideal m. Thus m belongs to V(K), so m = h(t) for some t in C. (`AlgebraicGeometry.IsProper` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Proper.lean)), `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean))).

Completeness gives I ≤ jacobson(0) ≤ m. The range of Spec(A/I) → Spec A is V(I), by range_comap_of_surjective and Ideal.mk_ker; Scheme.Pullback.range_fst says that the range of Y_0 → Y is f⁻¹(V(I)). Hence g(t) lies in that range. The containment hypothesis puts t in W, contradicting t in C. Thus W = X. (`IsAdicComplete.le_jacobson_bot` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)), `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)), [def-pc-base-change]).
