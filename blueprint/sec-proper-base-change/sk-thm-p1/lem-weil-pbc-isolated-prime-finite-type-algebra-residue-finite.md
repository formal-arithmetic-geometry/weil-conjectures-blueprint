+++
id = "lem-weil-pbc-isolated-prime-finite-type-algebra-residue-finite"
kind = "lemma"
title = "An isolated prime of a finite type algebra over a field has finite residue field"
lean = ["isolatedPrime_finiteType_residueField"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma 00PJ (algebra-lemma-isolated-point, line 30106), implication (1) => (6), using Lemmas 00G1 and 00G3 to make an isolated prime maximal and Theorem 00FV (algebra-theorem-nullstellensatz, line 6524) for finiteness of the residue field of a maximal ideal"
+++
Let $k$ be a field and let $B$ be a finite type (finitely generated) $k$-algebra `Algebra.FiniteType` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/FiniteType.lean)). If $\mathfrak p\in\operatorname{Spec}B$ `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean)) has singleton $\{\mathfrak p\}$ open in $\operatorname{Spec}B$, then $\mathfrak p$ is a maximal ideal of $B$, and the residue field $\kappa(\mathfrak p)=B_{\mathfrak p}/\mathfrak pB_{\mathfrak p}$ `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)), with its field extension structure from $k\to B\to\kappa(\mathfrak p)$ `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean)), is finite over $k$, i.e. $\dim_k\kappa(\mathfrak p)<\infty$.
