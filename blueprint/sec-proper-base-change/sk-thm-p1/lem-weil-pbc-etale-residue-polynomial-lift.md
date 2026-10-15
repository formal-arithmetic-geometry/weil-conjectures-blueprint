+++
id = "lem-weil-pbc-etale-residue-polynomial-lift"
kind = "lemma"
title = "Clearing denominators in a residue-field minimal polynomial"
lean = ["AlgebraicGeometry.residue_polynomial_lift"]
+++
Let $R$ be a commutative ring, $\mathfrak p\subset R$ a prime, and $L/\kappa(\mathfrak p)$ a finite separable field extension `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)) `Algebra.IsSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/Separable.lean)). If $\alpha\in L$ generates $L$ over $\kappa(\mathfrak p)$, then there are $c\in R\setminus\mathfrak p$ and a monic polynomial $f\in R[T]$ such that the image of $f$ in $\kappa(\mathfrak p)[T]$ is the minimal polynomial of the image of $c\alpha$ over $\kappa(\mathfrak p)$.
