+++
id = "def-sfb-dc-lower-star"
kind = "definition"
title = "$Rf_*$ on $D_{\\mathrm{cons}}$"
order = 2732
uses = ["lem-sfb-dc-lower-star-preserves", "det-def-sfb-dc-setting", "det-def-sfb-module-derived-pushpull"]
+++
Let $f\colon X\to Y$ be a morphism of the setting of [det-def-sfb-dc-setting], and let $\Lambda$
be a commutative condensed ring such that the ambient derived pushforward $Rf_*$ of
[det-def-sfb-module-derived-pushpull] carries bounded constructible complexes to bounded
constructible complexes. By [lem-sfb-dc-lower-star-preserves] this holds for
$\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$. The derived pushforward

$$
Rf_*\colon D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y,\Lambda)
$$

is the restriction of the ambient $Rf_*$. It commutes with the inclusions.
