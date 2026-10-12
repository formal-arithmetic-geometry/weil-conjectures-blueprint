+++
kind = "proof"
of = "lem-weil-pbc-flat-iso-mod-ideal-powers"
+++
Equip B with the A-algebra structure induced by φ. Surjectivity of β₁ gives surjectivity of A → B/IB. Induct on n, starting with the zero quotient for n=0. Given a lift modulo I^n, Mathlib AdicCompletion.exists_smodEq_pow_smul_top_and_mkQ_eq corrects it modulo I^(n+1). Ideal.smul_top_eq_map identifies module quotients with the ring quotients, proving surjectivity of every βₙ. This is the coefficient-lifting argument of Algebra 051H, implemented in the private helper surjective_mkQ_pow.

For J = I^n, the quotient tensor equivalence `Algebra.TensorProduct.quotIdealMapEquivTensorQuot` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/TensorProduct/Quotient.lean)), in its swapped form Algebra.TensorProduct.quotIdealMapEquivQuotTensor, identifies B/JB with (A/J) tensor_A B as an A/J-algebra. Module.Flat.baseChange and Module.Flat.of_linearEquiv give flatness of βₙ `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)). The private helper flat_quotientMap implements this argument.

For n ≥ 1, I^n ≤ I. If βₙ(a mod I^n)=0, then φ(a) belongs to IB; injectivity of β₁ implies a belongs to I. Thus ker βₙ is contained in the image of I in A/I^n. Its nth power is zero, since Ideal.map_pow identifies that power with the image of I^n. Hence ker βₙ is nilpotent.

For a surjective flat ring map f, the first isomorphism theorem identifies R/ker(f) with its flat target. Thus ker(f) is pure. Mathlib Ideal.isIdempotentElem_of_pure makes it idempotent; IsIdempotentElem.pow_succ_eq shows every positive power equals it. Nilpotence forces it to be zero (the exponent-zero case forces the entire ring to be zero). RingHom.injective_iff_ker_eq_bot gives injectivity. Apply this proved private helper injective_of_flat_surjective_nilpotent_ker to βₙ and combine with its surjectivity. No short five lemma or graded-piece maps are needed. (`Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean))).
