+++
kind = "proof"
of = "lem-weil-pbc-idempotent-endomorphism-charpoly-field"
+++
Mathlib LinearMap.IsIdempotentElem.isProj_range and LinearMap.IsProj.eq_conj_prodMap identify p as the conjugate, via Submodule.prodEquivOfIsCompl, of the identity on range p and zero on ker p. This directly supplies the complementary-subspace decomposition over k, without the stronger image/base-change theorem. Both subspaces are finite dimensional. Apply `LinearMap.finrank_range_add_finrank_ker` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/FiniteDimensional/Lemmas.lean)) and finrank k (Fin n → k) = n to obtain finrank k (ker p) = n - finrank k (range p).

Use LinearMap.charpoly_toMatrix and LinearEquiv.charpoly_conj from `LinearMap.charpoly_toMatrix, LinearEquiv.charpoly_conj, Matrix.charpoly_monic, Matrix.charpoly_natDegree_eq_dim, Module.Basis.baseChange, LinearMap.charpoly_baseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/ToMatrix.lean)) on the explicit conjugacy of step 1. Then `LinearMap.charpoly_prodMap` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/ToMatrix.lean)), implemented by LinearMap.charpoly_prodMap, gives the product of the identity and zero characteristic polynomials on range p and ker p.

Apply the identity and zero characteristic-polynomial leaves `LinearMap.charpoly_one` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/Basic.lean)) and `LinearMap.charpoly_zero` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/Basic.lean)) to the two summands. Their dimensions are $r$ and $n-r$, hence $\chi(1_{\operatorname{Im}(p)})=(T-1)^r$ and $\chi(0_{\ker(p)})=T^{n-r}$. Multiplying yields $\det(T-p)=(T-1)^rT^{n-r}$.

Since $0\le r\le n$, the factors have exponents bounded by $n$: $(T-1)^r$ divides $(T-1)^n$ and $T^{n-r}$ divides $T^n$. Thus their product divides $T^n(T-1)^n$ in $k[T]$.
