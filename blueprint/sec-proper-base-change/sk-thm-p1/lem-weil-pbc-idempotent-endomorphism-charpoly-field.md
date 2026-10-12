+++
id = "lem-weil-pbc-idempotent-endomorphism-charpoly-field"
kind = "lemma"
title = "Characteristic polynomial of an idempotent endomorphism over a field"
lean = ["LinearMap.charpoly_toMatrix_of_idempotent"]
source = "literature/stacks-project/more-algebra.tex, More on Algebra, proof of Lemma Tag 07M5 (lemma-lift-projective-module, line 2020): 'For every prime p containing I the image of f in kappa(p) is (x-1)^r x^{n-r} where r is the dimension of P-bar (x) kappa(p)' (stated without proof)"
+++
Let $k$ be a field, $n\ge0$, $V=k^{\oplus n}$ and $p:V\to V$ a $k$-linear map with $p\circ p=p$. Let $r=\dim_k\operatorname{Im}(p)$. Then the characteristic polynomial of $p$ `Matrix.charpoly` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean)) (computed in any basis `LinearMap.charpoly_toMatrix, LinearEquiv.charpoly_conj, Matrix.charpoly_monic, Matrix.charpoly_natDegree_eq_dim, Module.Basis.baseChange, LinearMap.charpoly_baseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/ToMatrix.lean))) is $\det(T-p)=(T-1)^rT^{n-r}\in k[T]$. In particular it divides $T^n(T-1)^n$ in $k[T]$.
