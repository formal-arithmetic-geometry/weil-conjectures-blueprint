+++
id = "lem-weil-pbc-idempotent-endomorphism-charpoly-field"
kind = "lemma"
title = "Characteristic polynomial of an idempotent endomorphism over a field"
lean = ["LinearMap.charpoly_toMatrix_of_idempotent"]
+++
Let $k$ be a field, $n\ge0$, $V=k^{\oplus n}$ and $p:V\to V$ a $k$-linear map with $p\circ p=p$. Let $r=\dim_k\operatorname{Im}(p)$. Then the characteristic polynomial of $p$ `Matrix.charpoly` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean)) (computed in any basis `LinearMap.charpoly_toMatrix, LinearEquiv.charpoly_conj, Matrix.charpoly_monic, Matrix.charpoly_natDegree_eq_dim, Module.Basis.baseChange, LinearMap.charpoly_baseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/ToMatrix.lean))) is $\det(T-p)=(T-1)^rT^{n-r}\in k[T]$. In particular it divides $T^n(T-1)^n$ in $k[T]$.
