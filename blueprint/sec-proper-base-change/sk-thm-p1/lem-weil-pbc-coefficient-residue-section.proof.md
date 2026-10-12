+++
kind = "proof"
of = "lem-weil-pbc-coefficient-residue-section"
+++
Every nonzero integer has nonzero residue, hence is a unit in R. The localization universal property for Q as the fraction ring of Z gives R a Q-algebra structure.

Choose a transcendence basis of the residue field over Q. Its intermediate rational function field has characteristic zero and is perfect, and the residue field is algebraic and thus separable over it. Apply the Mathlib formally smooth separably generated extension theorem. (`Algebra.FormallySmooth.of_algebraicIndependent_of_isSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Smooth/Field.lean))).

Apply Algebra.FormallySmooth.exists_mkₐ_comp_eq_of_isAdicComplete to the identity ring map of R/m, made into a Q-algebra map by uniqueness of ring maps from Q. It lifts into R, and its reduction is the identity. This Mathlib theorem constructs the compatible lifts and their inverse limit. (`IsAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)), `AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean))).
