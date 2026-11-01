+++
id = "def-sfb-dc-upper-star"
kind = "definition"
title = "$Lf^*$ on $D_{\\mathrm{cons}}$"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStar"]
order = 2729
uses = ["lem-sfb-dc-upper-star-preserves", "det-def-sfb-dc-setting", "det-def-sfb-module-derived-pushpull"]
+++
Let $\Lambda$ be a commutative condensed ring and let $f\colon X\to Y$ be a morphism of the
setting of [det-def-sfb-dc-setting]. The derived pullback

$$
Lf^*\colon D_{\mathrm{cons}}(Y,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda)
$$

is the restriction of the ambient derived pullback $Lf^*$ of [det-def-sfb-module-derived-pushpull]
to bounded constructible complexes, which it preserves by [lem-sfb-dc-upper-star-preserves]. It
commutes with the inclusions into $D(\Mod_{\Lambda_Y})$ and $D(\Mod_{\Lambda_X})$.
