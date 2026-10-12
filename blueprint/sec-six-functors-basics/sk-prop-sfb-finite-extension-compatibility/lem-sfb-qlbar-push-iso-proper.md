+++
id = "lem-sfb-qlbar-push-iso-proper"
kind = "lemma"
title = "(Push) is an isomorphism for $E\\subseteq\\Qlb$ and $f$ proper"
order = 1700
uses = ["def-sfb-subfield-to-qlbar-coefficient-map", "lem-sfb-qlbar-flat", "def-sfb-derived-push-hom"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjToPadicAlgCl_of_isProper"]
+++
For a finite extension $E$ of $\mathbf Q_\ell$ inside $\Qlb$ and every proper morphism of
schemes $f\colon X\to Y$, the comparison (Push) ([def-sfb-derived-push-hom]) for the coefficient
change $E\to\Qlb$ ([def-sfb-subfield-to-qlbar-coefficient-map]; flat by [lem-sfb-qlbar-flat]),

$$
T^Y_{E,\Qlb}\circ Rf_*\longrightarrow Rf_*\circ T^X_{E,\Qlb},
$$

is an isomorphism of functors on the unbounded derived category $D(\Mod_{E_X})$.
