+++
id = "sk-def-sfb-dc-upper-shriek"
kind = "definition"
title = "$Rf^!$ on $D_{\\mathrm{cons}}$"
order = 1793
uses = ["sk-def-sfb-dc-lower-shriek"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isLeftAdjoint_boundedConstructibleLowerStar_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isLeftAdjoint_boundedConstructibleLowerStar_padicIntegersRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isLeftAdjoint_boundedConstructibleLowerStar_padicAlgClRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekOfCompactificationAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriek", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekAdjunction"]
tags = ["sketch"]
+++
Work in the setting of [sk-def-sfb-dc-setting], with $\Lambda$ as in [sk-def-sfb-dc-lower-shriek].
Let $f\colon X\to Y$ be a morphism and $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$ a compactification
of $f$. Assume that the restricted pushforward
$Rp_*\colon D_{\mathrm{cons}}(Z,\Lambda)\to D_{\mathrm{cons}}(Y,\Lambda)$
([sk-def-sfb-dc-restricted-functors]) along the proper morphism $p$ has a right adjoint. For
every proper $p$ this holds when $\Lambda$ is $\underline E$ ($E/\mathbf Q_\ell$ finite),
$\underline{\cO}_E$ ($E\subseteq\Qlb$ finite over $\mathbf Q_\ell$; [sk-def-sfb-condensed-ring])
or $\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed]). Let $Rp^!$ be a chosen right adjoint of
$Rp_*$, and let $i^*=Li^*$ be the restricted pullback, which is right adjoint to $i_!$. Define

$$
Rf^!_c:=i^*\circ Rp^!\colon D_{\mathrm{cons}}(Y,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda),
$$

and $Rf^!:=Rf^!_{c_f}$ for the chosen compactification $c_f$ of [sk-def-sfb-dc-setting], under
the assumption for $p_f$. The composite of the adjunctions $i_!\dashv i^*$ and $Rp_*\dashv Rp^!$ is
an adjunction

$$
Rf_!^c\dashv Rf^!_c,
$$

with $Rf_!^c=Rp_*\circ i_!$ the lower shriek of [sk-def-sfb-dc-lower-shriek]. In particular
$Rf_!\dashv Rf^!$, so $Rf_!$ is a left adjoint and $Rf^!$ is a right adjoint. The functor $Rp^!$
is an abstract choice, determined up to unique isomorphism, and is used only through the
adjunction. The functor $Rf^!$ is constructed directly on $D_{\mathrm{cons}}$, so no separate
statement that it preserves constructibility is needed.
