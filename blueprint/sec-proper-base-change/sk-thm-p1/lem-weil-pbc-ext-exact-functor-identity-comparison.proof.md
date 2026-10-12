+++
kind = "proof"
of = "lem-weil-pbc-ext-exact-functor-identity-comparison"
uses = ["def-pc-ext", "def-weil-abstract-derived-category"]
+++
By `CategoryTheory.Functor.mapDerivedCategoryFactors` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/DerivedCategory/ExactFunctor.lean)), F acts termwise on complexes and preserves quasi-isomorphisms, so induces a functor on their localization. The termwise identity functor localizes to the identity, and e induces a natural isomorphism from the induced F to the identity. This follows from the localization universal property [def-weil-abstract-derived-category]. The components of this isomorphism commute with shifts because e acts termwise.

Under [def-pc-ext], x is a morphism A[0] to B[0][n]. Apply naturality of the localized e to x. The source component is mk_0(e_A), the target component is mk_0(e_B)[n], and the identity functor leaves x unchanged. This gives exactly the asserted equality.
