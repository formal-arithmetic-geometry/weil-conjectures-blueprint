+++
id = "lem-weil-pbc-finite-purely-inseparable-scalar-descent"
kind = "lemma"
title = "A finite purely inseparable extension descends along a field extension"
lean = ["Algebra.TensorProduct.finite_purelyInseparable_of_tensorProduct"]
+++
Let $K\subseteq L$ be fields ($L$ a field extension of $K$ `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean))) and let $B$ be a commutative $K$-algebra. Regard $L\otimes_KB$ as an $L$-algebra via $l\mapsto l\otimes1$. If $L\otimes_KB$ is a field and, via this map, a finite purely inseparable field extension of $L$ `IsPurelyInseparable, Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/PurelyInseparable/Basic.lean)), then $B$ is a field, the structure map $K\to B$ makes $B$ a finite purely inseparable field extension of $K$ `IsPurelyInseparable, Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/PurelyInseparable/Basic.lean)), and $\dim_KB=\dim_L(L\otimes_KB)$.
