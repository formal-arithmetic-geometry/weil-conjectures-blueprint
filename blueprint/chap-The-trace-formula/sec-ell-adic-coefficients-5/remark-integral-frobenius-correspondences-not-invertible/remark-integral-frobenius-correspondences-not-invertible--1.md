+++
id = "remark-integral-frobenius-correspondences-not-invertible--1"
kind = "remark"
title = "Integral Frobenius correspondences need not be invertible (1)"
name_showing = false
order = 1016001
aliases = ["bp-r310-1"]
lean = ["Submodule.eq_bot_of_fg_of_inv_mul_mem", "not_exists_algebraMap_units_eq_and_eq_mul"]
+++
In Lemma [lemma-integral-models-rational-frobenius-correspondences], $K_0$ need not be a lattice in a
lisse sheaf, and $\theta$ need not be invertible even when $\psi_E$ is.
The factor $\pi_E^{-N}$ is needed because $\psi_E$ itself need not be
integral: on a point, the automorphism $\ell^{-1}$ of $E$ preserves no lattice.
Even with this factor, $\theta$ cannot always be chosen invertible, already on
a point. On $E^2$, the two eigenvalues of $\operatorname{diag}(1,\ell)$
cannot both become units after multiplying the operator by a single
scalar. So Lemma [lemma-integral-models-rational-frobenius-correspondences]
only makes $\pi_E^N\psi_E$ integral, and the reductions of $\theta$ may fail to
be invertible. For this reason Theorem [theorem-trace-formula-frobenius-correspondence]
is stated for arbitrary Frobenius correspondences.
