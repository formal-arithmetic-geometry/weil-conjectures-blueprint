+++
id = "sk-rem-tf-weil-lattices"
kind = "remark"
title = "Integral Frobenius correspondences need not be invertible"
order = 605
tags = ["sketch"]
+++
In Lemma [sk-lem-tf-rational-model], $K_0$ need not be a lattice in a
lisse sheaf, and $\theta$ need not be invertible even when $\psi_E$ is.
The automorphism $\ell^{-1}$ of $E$ preserves no lattice, so $\psi_E$
itself need not be integral, which is why the factor $\pi_E^{-N}$ is
needed. Even then $\theta$ cannot always be chosen invertible, already on
a point: on $E^2$, the two eigenvalues of $\operatorname{diag}(1,\ell)$
cannot both become units after multiplying the operator by a single
scalar. Thus
Lemma [sk-lem-tf-rational-model] only makes $\pi_E^N\psi_E$ integral, and
its reductions may fail to be invertible. For this reason Theorem [sk-thm-tf-coefficient-morphism-formula]
is stated for arbitrary Frobenius correspondences.
