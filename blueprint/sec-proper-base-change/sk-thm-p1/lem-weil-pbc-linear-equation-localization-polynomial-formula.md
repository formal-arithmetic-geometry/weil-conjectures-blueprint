+++
id = "lem-weil-pbc-linear-equation-localization-polynomial-formula"
kind = "lemma"
title = "Eliminated variable formula"
lean = ["MvPolynomial.linearEquationLocalizationPolynomialFormula"]
+++
Let A be a commutative ring, r a natural number, f : Fin r → A, and i : Fin r. Let I = (∑ j, f(j)X_j − 1) in A[X_j : j : Fin r] `MvPolynomial, MvPolynomial.aeval, MvPolynomial.algHom_ext` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/MvPolynomial/Basic.lean)), B its quotient, Af the localization at f(i), Bf the localization of B at the image of f(i) `Localization.Away` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/GroupTheory/MonoidLocalization/Away.lean)), and x_j the localized class of X_j. Give Bf its induced Af-algebra structure `IsLocalization.Away.lift, IsLocalization.Away.lift_eq, IsLocalization.ringHom_ext` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/Away/Basic.lean)). For any Af-algebra equivalence e : Af[Y_j : j ≠ i] ≃ Bf whose forward map is evaluation at x_j and whose inverse sends x_j to Y_j for j ≠ i, its inverse sends x_i to f(i)⁻¹(1−∑ j ≠ i f(j)Y_j).
