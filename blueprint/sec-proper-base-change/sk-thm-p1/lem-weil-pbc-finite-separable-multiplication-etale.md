+++
id = "lem-weil-pbc-finite-separable-multiplication-etale"
kind = "lemma"
title = "Multiplication of a finite separable extension is etale"
lean = ["AlgebraicGeometry.finite_separable_multiplication_etale"]
+++
Let $k'/k$ be a field extension `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean)) which is finite ($\dim_kk'<\infty$) and separable algebraic `Algebra.IsSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/Separable.lean)). Let $\mu:k'\otimes_kk'\to k'$, $a\otimes b\mapsto ab$, be the multiplication map. Then $\operatorname{Spec}\mu:\operatorname{Spec}k'\to\operatorname{Spec}(k'\otimes_kk')$ is etale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)); in particular $\mu$ is a smooth ring map `Algebra.Smooth` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Smooth/Basic.lean)).
