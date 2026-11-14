+++
kind = "proof"
of = "dag-lem-sp-ell-power-ideals-nested"
tags = ["sheaf-dag"]
+++
1. Fix n ≥ 0 and work in the commutative ring O_E. The inequality n+1 ≤ n+2 is Nat.le_succ (n+1), so Mathlib's pow_dvd_pow gives ℓ^(n+1) ∣ ℓ^(n+2) in O_E.
2. By Mathlib's Ideal.span_singleton_le_span_singleton, this divisibility gives Ideal.span {ℓ^(n+2)} ≤ Ideal.span {ℓ^(n+1)}. By the definition of spTateEllIdeal, these are spTateEllIdeal ℓ E (n+1) and spTateEllIdeal ℓ E n respectively. Thus ℓ^(n+2)O_E ⊆ ℓ^(n+1)O_E, as required.
