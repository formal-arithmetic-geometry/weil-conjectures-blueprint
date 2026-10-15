+++
id = "lem-weil-pbc-finite-galois-receiving-separable-extensions"
kind = "lemma"
title = "Finitely many finite separable extensions embed into one finite Galois extension"
lean = ["finite_galois_receiving_separable_extensions"]
+++
Let $k$ be a field, $n\ge0$, and let $L_1,\dots,L_n$ be field extensions of $k$ `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean)) which are finite ($\dim_kL_i<\infty$) and separable algebraic `Algebra.IsSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/Separable.lean)). Then there are a field extension $L/k$ and homomorphisms of $k$-algebras $\tau_i:L_i\to L$ ($i=1,\dots,n$) such that $L/k$ is finite ($\dim_kL<\infty$), separable algebraic `Algebra.IsSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/Separable.lean)), and normal: for every $\beta\in L$ the minimal polynomial of $\beta$ over $k$ (as in `Algebra.IsSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/Separable.lean))) is a product of polynomials of degree one in $L[T]$. (That is, $L/k$ is a finite Galois extension, Stacks, Fields, Definition 09I0, receiving every $L_i$.)
