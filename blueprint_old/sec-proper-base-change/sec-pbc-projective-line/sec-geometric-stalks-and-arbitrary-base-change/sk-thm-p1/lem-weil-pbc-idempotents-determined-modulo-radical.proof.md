+++
kind = "proof"
of = "lem-weil-pbc-idempotents-determined-modulo-radical"
+++
Put d = e - e′. The idempotency equations e*e=e and e′*e′=e′ imply d*d*d=d by polynomial expansion in the commutative ring. This identity holds without any characteristic restriction.

The inclusion J ≤ jacobson(0) puts d in the Jacobson radical. Closure under multiplication and negation puts -d*d there, so (1-d*d)-1 lies in the radical. Mathlib Ideal.isUnit_of_sub_one_mem_jacobson_bot shows that 1-d*d is a unit.

The cubic identity implies d*(1-d*d)=d-d*d*d=0. Cancel the unit 1-d*d using IsUnit.mul_right_cancel to obtain d=0. Thus e=e′ by sub_eq_zero.
