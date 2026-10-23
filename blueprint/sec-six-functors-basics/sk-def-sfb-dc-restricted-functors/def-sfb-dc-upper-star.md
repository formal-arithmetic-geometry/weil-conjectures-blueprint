+++
id = "def-sfb-dc-upper-star"
kind = "definition"
title = "$Lf^*$ on $D_{\\mathrm{cons}}$"
order = 2626
uses = ["lem-sfb-dc-upper-star-preserves", "sk-def-sfb-dc-setting", "sk-def-sfb-module-derived-pushpull"]
+++
Let $\Lambda$ be a commutative condensed ring and let $f\colon X\to Y$ be a morphism of the
setting of [sk-def-sfb-dc-setting]. The derived pullback

$$
Lf^*\colon D_{\mathrm{cons}}(Y,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda)
$$

is the restriction of the ambient derived pullback $Lf^*$ of [sk-def-sfb-module-derived-pushpull]
to bounded constructible complexes, which it preserves by [lem-sfb-dc-upper-star-preserves]. It
commutes with the inclusions into $D(\Mod_{\Lambda_Y})$ and $D(\Mod_{\Lambda_X})$.
