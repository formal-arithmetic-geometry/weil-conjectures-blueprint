+++
id = "sk-def-sfb-dc-lower-shriek"
kind = "definition"
title = "$Rf_!$ on $D_{\\mathrm{cons}}$: assembled from $i_!$ and $Rp_*$"
order = 1641
uses = ["sk-def-sfb-dc-restricted-functors"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekOfCompactificationCompatibility", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekCompatibility"]
tags = ["sketch"]
+++
Work in the setting of [sk-def-sfb-dc-setting]. Let $\Lambda$ be a commutative condensed ring
for which the derived pushforwards restrict to bounded constructible complexes
([sk-def-sfb-dc-restricted-functors]; for instance $\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$).
For a morphism $f\colon X\to Y$ and a compactification $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$
of $f$, the *lower shriek attached to $c$* is the composite of the two restricted functors of
[sk-def-sfb-dc-restricted-functors]:

$$
Rf_!^c:=Rp_*\circ i_!\colon D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y,\Lambda).
$$

The *derived lower shriek* is $Rf_!:=Rf_!^{c_f}$ for the chosen compactification $c_f$ of
[sk-def-sfb-dc-setting]. No separate preservation statement is needed for $Rf_!$.

The functor $Rf_!^c$ is compatible with the ambient lower shriek
$Rf_!^c=R(p_*)\circ D(i_!)$ on $D(\Mod_{\Lambda_X})$ of [sk-def-sfb-module-derived-lower-shriek]:
there is a natural isomorphism $\iota\circ Rf_!^c\cong Rf_!^c\circ\iota$, with $\iota$ the inclusions
of $D_{\mathrm{cons}}$. In particular $Rf_!$ on $D_{\mathrm{cons}}$ is compatible with the ambient
$Rf_!$ for the chosen compactification.
