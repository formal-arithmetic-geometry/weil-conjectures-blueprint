+++
id = "lem-weil-pbc-formal-glueing-finite-modules"
kind = "lemma"
title = "Finiteness of a module is detected by its formal glueing data"
lean = ["Module.finite_iff_formalGlueing"]
source = "literature/stacks-project/more-algebra.tex, More on Algebra, Remark 05EU (remark-formal-glueing-algebras, line 25036), the case 'finite': R -> S x prod R_{f_i} is faithfully flat, and finiteness descends along faithfully flat maps (Algebra, Lemma 03C4, lemma-descend-properties-modules)"
+++
Let $\varphi:R\to S$ be a flat ring map of commutative rings `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)), $f_1,\dots,f_t\in R$ and $I=(f_1,\dots,f_t)$, such that the induced map $R/I\to S/IS$ is an isomorphism. Let $M$ be an $R$-module. Then $M$ is a finitely generated $R$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)) if and only if the base change $M\otimes_RS$ `LinearMap.baseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/TensorProduct/Tower.lean)) is a finitely generated $S$-module and, for every $i$, the localization $M_{f_i}$ `LocalizedModule.Away` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)) is a finitely generated $R_{f_i}$-module.
