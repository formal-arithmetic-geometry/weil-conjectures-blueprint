+++
id = "det-def-sfb-finite-upper-shriek"
kind = "definition"
title = "Exceptional pullback $Rf^!$ (finite coefficients)"
order = 2548
uses = ["sk-def-nagata-sketch-data", "det-def-sfb-finite-derived-lower-shriek", "sk-prop-ctf-finite-proper", "sec-proper-base-change"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
+++
Let $\Lambda$ be a finite ring and let $f\colon X\to Y$ admit a compactification
[sk-def-nagata-sketch-data], with chosen compactification
$X\xrightarrow{i}\bar X\xrightarrow{g}Y$.

*Étale site.* For proper $g$ the derived pushforward $Rg_*$ on the unbounded derived
categories of étale sheaves of $\Lambda$-modules commutes with direct sums, so it has a right
adjoint $Rg^!$. The étale exceptional inverse image is $f^\times:=D(i^*)\circ Rg^!$, and the
étale $Rf_!=Rg_*\circ D(i_!)$ is left adjoint to $f^\times$.

*Pro-étale site.* Here $Rg_*$ need not commute with direct sums, and the pro-étale $Rf_!$
([det-def-sfb-finite-derived-lower-shriek]) is in general not a left adjoint, not even on
$D^+$; this already fails for the structure morphism of an elliptic curve. The exceptional
pullback is instead transported from the étale site along the comparison morphism $\nu$:

$$
Rf^!:=\nu_X^*\circ f^\times\circ R\nu_{Y,*}\colon D(Y_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda).
$$

For $Y$ quasi-compact it sends bounded below objects to bounded below objects of étale origin,
and for $K$ bounded below of étale origin and $L$ bounded below,
$\Hom(Rf_!K,L)\simeq\Hom(K,Rf^!L)$ naturally. In particular $Rf_!\dashv Rf^!$ on the bounded
constructible objects of finite Tor amplitude.
