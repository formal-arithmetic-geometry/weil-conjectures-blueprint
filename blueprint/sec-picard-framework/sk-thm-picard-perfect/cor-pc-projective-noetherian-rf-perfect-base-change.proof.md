+++
kind  = "proof"
of    = "cor-pc-projective-noetherian-rf-perfect-base-change"
+++
The isomorphism is [lem-pc-rf-base-change-flat-module].
By [lem-pc-projective-noetherian-rf-perfect], $Rf_*\mathcal G$ is perfect
in $D(A)$: it is isomorphic to a bounded complex $P$ of finite projective
$A$-modules, as in [def-pc-perfect-complex]. Both $P$ and the bounded flat
representative $K$ of [lem-pc-rf-base-change-flat-module] are bounded
complexes of flat modules, so they compute the derived pullback, and
$Lg^*Rf_*\mathcal G\cong P\otimes_AB$. Tensoring preserves finite
projective modules: a finite projective module is the image of an
idempotent on a finite free module, and tensoring preserves that
idempotent decomposition. Hence the derived pullback is perfect,
and the isomorphic right side is perfect as well.
