+++
id = "lem-weil-pbc-polynomial-presentation-height-field-extension"
kind = "lemma"
title = "Height difference in a polynomial presentation after field extension"
lean = ["AlgebraicGeometry.polynomial_presentation_height_field_extension"]
+++
Let k and K be fields, S a commutative k-algebra, and f : k[x_1,…,x_n] → S a surjective k-algebra map `MvPolynomial, MvPolynomial.aeval, MvPolynomial.algHom_ext` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/MvPolynomial/Basic.lean)); `Algebra.FiniteType` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/FiniteType.lean)). There exists a surjective ring map g : K[x_1,…,x_n] → S ⊗[k] K such that for every prime Q of S ⊗[k] K, with q its contraction to S, height(f⁻¹(q)) + height(Q) = height(g⁻¹(Q)) + height(q). The proof constructs g by scalar extension of f.
