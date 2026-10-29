+++
id = "def-sfb-dc-upper-shriek-of-compactification"
kind = "definition"
title = "$Rf^!_c$ for a compactification $c$"
order = 2788
uses = ["def-sfb-dc-lower-star", "def-sfb-dc-upper-star", "det-def-sfb-dc-setting"]
+++
Let $\Lambda$ be as in [def-sfb-dc-lower-star], let $f\colon X\to Y$ be a morphism of the setting
of [det-def-sfb-dc-setting], and let $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$ be a compactification
of $f$ such that $Rp_*\colon D_{\mathrm{cons}}(Z,\Lambda)\to D_{\mathrm{cons}}(Y,\Lambda)$ has a right
adjoint. Let $Rp^!$ be a chosen right adjoint. The *exceptional inverse image attached to $c$*
is

$$
Rf^!_c:=Li^*\circ Rp^!\colon D_{\mathrm{cons}}(Y,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda),
$$

with $Li^*$ the restricted pullback of [def-sfb-dc-upper-star] along the open immersion $i$.
