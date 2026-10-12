+++
kind = "proof"
of = "lem-weil-pbc-idempotent-endomorphism-image-base-change"
+++
Use LinearMap.IsIdempotentElem.ker_eq_range_one_sub and isCompl to identify Im(1-p) with ker(p) and prove complementarity. Module.Finite.range gives finiteness. The restriction of p to its range is a retraction of the subtype inclusion, so Module.Projective.of_split gives projectivity from the finite free ambient module.

Let E be TensorProduct.piScalarRight, the canonical S-linear equivalence S tensor_R R^n to S^n. Base-change the inclusion i of range(p) and the retraction r induced by p. The identity r composed with i = id holds on pure tensors. Set f = E composed with i and g = r composed with E inverse; then g composed with f = id. On pure tensors f(s tensor x) has coordinates s rho(x_j), by the tensor base-change formulas `LinearMap.liftBaseChangeEquiv, LinearMap.liftBaseChange, LinearMap.liftBaseChange_tmul, LinearMap.liftBaseChangeEquiv_symm_apply` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/TensorProduct/Basic.lean)).

On pure tensors compute E(i(r(s tensor x))) using RingHom.map_mulVec and LinearMap.toMatrix'_mulVec; it agrees with p_S(E(s tensor x)). Therefore f composed with g = p_S. The two split-map identities imply p_S squared = p_S, f is injective, and range(f)=range(p_S). LinearEquiv.ofInjective followed by LinearEquiv.ofEq yields the required canonical range equivalence and subtype compatibility.
