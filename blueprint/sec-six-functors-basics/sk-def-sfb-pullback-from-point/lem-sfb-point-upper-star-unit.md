+++
id = "lem-sfb-point-upper-star-unit"
kind = "lemma"
title = "$p^*$ preserves the unit"
order = 1527
uses = ["def-sfb-point-adjunction", "lem-sfb-profinite-to-proetale-finite-limits", "sk-def-sfb-sheaf-tensor"]
lean = ["AlgebraicGeometry.ProEtale.isIso_η_pointUpperStar"]
+++
Give $\Sh(*_{\mathrm{proét}},\Ab)$ and $\Sh((\Spec\Z)_{\mathrm{proét}},\Ab)$
the tensor products of [sk-def-sfb-sheaf-tensor], whose units are the
constant sheaves $\Z$. The functor $p_*$ is lax monoidal. By the adjunction
[def-sfb-point-adjunction], $p^*$ is therefore oplax monoidal. Its unit
comparison morphism $p^*\Z\to\Z$ is an isomorphism.
