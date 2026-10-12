+++
id = "lem-sfb-subfield-push-iso"
kind = "lemma"
title = "(Push) is an isomorphism for $F/E$ finite"
order = 1750
uses = ["def-sfb-subfield-coefficient-map", "lem-sfb-subfield-flat", "def-sfb-derived-push-hom"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjMap"]
+++
For finite extensions $E\le F$ of $\mathbf Q_\ell$ inside $\Qlb$ and every morphism of schemes
$f\colon X\to Y$, the comparison (Push) ([def-sfb-derived-push-hom]) for the coefficient change
$E\to F$ ([def-sfb-subfield-coefficient-map]; flat by [lem-sfb-subfield-flat]),

$$
T^Y_{E,F}\circ Rf_*\longrightarrow Rf_*\circ T^X_{E,F},
$$

is an isomorphism of functors on the unbounded derived category $D(\Mod_{E_X})$.
