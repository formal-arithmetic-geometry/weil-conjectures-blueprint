+++
id = "lem-weil-pbc-linear-equation-localization-polynomial-core"
kind = "lemma"
title = "Core localization polynomial equivalence"
lean = ["MvPolynomial.linearEquationLocalizationPolynomialCore"]
+++
Let A be a commutative ring, r a natural number, f : Fin r → A, and i : Fin r. Write I = (∑ j, f(j)X_j - 1), B = A[X_j : j : Fin r]/I `MvPolynomial, MvPolynomial.aeval, MvPolynomial.algHom_ext` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/MvPolynomial/Basic.lean)), Af = A localized at f(i), and Bf = B localized at the image of f(i) `Localization.Away` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/GroupTheory/MonoidLocalization/Away.lean)). Equip Bf with its induced Af-algebra structure `IsLocalization.Away.lift, IsLocalization.Away.lift_eq, IsLocalization.ringHom_ext` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/Away/Basic.lean)). Then there exists an Af-algebra equivalence Af[Y_j : j ≠ i] ≃ Bf whose forward homomorphism is evaluation at the localized classes x_j of X_j, and whose inverse sends x_j to Y_j for every j ≠ i.
