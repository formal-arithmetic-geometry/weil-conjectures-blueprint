+++
id = "det-def-sfb-dc-lower-shriek-definition"
kind = "definition"
title = "The lower shriek on $D_{\\mathrm{cons}}$ for a compactification"
order = 2565
uses = ["def-sfb-dc-open-lower-shriek", "def-sfb-dc-lower-star", "sk-def-sfb-dc-setting", "def-sfb-compactification-over-field", "sk-def-nagata-sketch-data"]
+++
Work in the setting of [sk-def-sfb-dc-setting]: schemes separated and of finite type over a field
$k$ of characteristic $p\ne\ell$. Let $\Lambda$ be a commutative condensed ring such that for every
morphism $q$ of the setting the ambient derived pushforward $Rq_*$ preserves bounded constructible
complexes, so that the restricted functor $Rq_*\colon D_{\mathrm{cons}}(-,\Lambda)\to D_{\mathrm{cons}}(-,\Lambda)$ of
[def-sfb-dc-lower-star] is defined (e.g. $\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$).

Let $f\colon X\to Y$ be a morphism of the setting and $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$ a
compactification of $f$ ([sk-def-nagata-sketch-data]): $i$ an open immersion, $p$ proper,
$f=p\circ i$; by [sk-def-sfb-dc-setting], $Z$ and $i,p$ belong to the setting. The *lower shriek
attached to $c$* is the composite
$$
Rf_!^c:=Rp_*\circ i_!\colon D_{\mathrm{cons}}(X,\Lambda)\xrightarrow{\ i_!\ }D_{\mathrm{cons}}(Z,\Lambda)\xrightarrow{\ Rp_*\ }D_{\mathrm{cons}}(Y,\Lambda),
$$
of the restricted extension by zero $i_!$ ([def-sfb-dc-open-lower-shriek]) and the restricted
derived pushforward $Rp_*$ ([def-sfb-dc-lower-star]). The *derived lower shriek* is
$Rf_!:=Rf_!^{c_f}$ for the chosen compactification $c_f=(X\xrightarrow{i_f}Z_f\xrightarrow{p_f}Y)$ of
[def-sfb-compactification-over-field]. Since both factors are functors between the categories
$D_{\mathrm{cons}}$, no separate statement that $Rf_!^c$ preserves bounded constructible complexes is
needed.
