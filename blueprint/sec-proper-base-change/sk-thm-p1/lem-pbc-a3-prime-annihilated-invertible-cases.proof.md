+++
kind = "proof"
of = "lem-pbc-a3-prime-annihilated-invertible-cases"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Apply the additive stalk functors to the annihilation equality. If r is a unit, it is a common positive invertible annihilator, as required by the coefficient condition.

Use ΓSpecIso to pass to k. If r is not a unit, r is zero in k. An integer n invertible in k is not divisible by r. The stalk is killed by both r and n, and nsmul_eq_zero_iff_of_coprime makes it zero.

Use sheafHom_ext_of_sheafFiber_map_algClosurePoint and IsZero.iff_id_eq_zero to conclude that F is zero. ([lemma-weil-pbc-geometric-stalk-conservative]).
