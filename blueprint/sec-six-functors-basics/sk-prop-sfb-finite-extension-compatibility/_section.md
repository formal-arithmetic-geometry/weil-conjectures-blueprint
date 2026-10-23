+++
id = "sk-prop-sfb-finite-extension-compatibility"
kind = "proposition"
title = "Compatibility for $E\\subseteq F$ and $E\\subseteq\\Qlb$"
order = 2572
uses = ["sk-def-sfb-coefficient-comparisons"]
lean = ["AlgebraicGeometry.ProEtale.padicSubfieldRingObjMap", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_extendScalars_padicSubfieldRingObjMap", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjMap", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjToPadicAlgCl_of_isProper"]
tags = ["sketch"]
+++
Let $\ell$ be a prime and $E\le F$ finite extensions of $\mathbf Q_\ell$ inside $\Qlb$. Apply
[sk-def-sfb-coefficient-change] to the inclusions of condensed rings
$\underline E\to\underline F$ and $\underline E\to\underline{\Qlb}$
([det-def-sfb-condensed-ring], [det-def-sfb-qlbar-condensed], [det-prop-sfb-qlbar-colimit-point]):
on a scheme $X$ they give coefficient changes $E_X\to F_X$ and $E_X\to\overline{\mathbf Q}_{\ell,X}$ between the
pulled-back coefficient rings ([det-def-sfb-pulled-back-coefficients]), with
$E_X\to F_X\to\overline{\mathbf Q}_{\ell,X}$ equal to $E_X\to\overline{\mathbf Q}_{\ell,X}$, and derived extensions of scalars

$$
T^X_{E,F}=F_X\otimes^{\mathrm L}_{E_X}-,\qquad T^X_{E,\Qlb}=\overline{\mathbf Q}_{\ell,X}\otimes^{\mathrm L}_{E_X}-.
$$

1. **Flatness.** For every scheme $X$, $F_X$ and $\overline{\mathbf Q}_{\ell,X}$ are flat over $E_X$: the
   extensions of scalars $F_X\otimes_{E_X}-$ and $\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}-$ are exact. Hence the
   comparisons (Pull), (Push) and (Shriek) of [sk-def-sfb-coefficient-comparisons] are defined
   for both coefficient changes, and (Pull) is an isomorphism on the unbounded derived
   categories.
2. **Finite extensions.** For every morphism of schemes $f\colon X\to Y$, (Push)
   $T^Y_{E,F}\circ Rf_*\to Rf_*\circ T^X_{E,F}$ is an isomorphism; consequently (Shriek)
   $T^Y_{E,F}\circ Rf_!\to Rf_!\circ T^X_{E,F}$ is an isomorphism for every $f$ admitting a
   compactification.
3. **$E\subseteq\Qlb$.** For every *proper* morphism $f\colon X\to Y$, (Push)
   $T^Y_{E,\Qlb}\circ Rf_*\to Rf_*\circ T^X_{E,\Qlb}$ is an isomorphism; consequently (Shriek)
   $T^Y_{E,\Qlb}\circ Rf_!\to Rf_!\circ T^X_{E,\Qlb}$ is an isomorphism for every $f$ admitting a
   compactification.

All isomorphisms are on the unbounded derived categories.
