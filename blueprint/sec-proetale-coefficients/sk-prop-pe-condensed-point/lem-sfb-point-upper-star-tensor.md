+++
id = "lem-sfb-point-upper-star-tensor"
kind = "lemma"
title = "$p^*$ preserves tensor products"
order = 1080
uses = ["def-sfb-point-adjunction", "lem-sfb-point-upper-star-unit", "lem-sfb-profinite-to-proetale-finite-limits", "lem-weil-pbc-sheaf-tensor-closed"]
lean = ["AlgebraicGeometry.ProEtale.isIso_δ_pointUpperStar"]
+++
For condensed abelian groups $F$ and $G$, the oplax tensor comparison
morphism $p^*(F\otimes G)\to p^*F\otimes p^*G$ of $p^*$ (for the oplax
structure of [lem-sfb-point-upper-star-unit] and the tensor products of
[lem-weil-pbc-sheaf-tensor-closed]) is an isomorphism.
