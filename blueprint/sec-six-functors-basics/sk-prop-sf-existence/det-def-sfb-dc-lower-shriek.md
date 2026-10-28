+++
id = "det-def-sfb-dc-lower-shriek"
kind = "definition"
title = "$Rf_!$ on $D_{\\mathrm{cons}}$: assembled from $i_!$ and $Rp_*$"
order = 2557
uses = ["det-def-sfb-dc-restricted-functors"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekOfCompactificationCompatibility", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekCompatibility"]
+++
Work in the setting of [det-def-sfb-dc-setting]. Let $\Lambda$ be a commutative condensed ring
for which the derived pushforwards restrict to bounded constructible complexes
([det-def-sfb-dc-restricted-functors]; for instance $\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$).
For a morphism $f\colon X\to Y$ and a compactification $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$
of $f$, the *lower shriek attached to $c$* is the composite of the two restricted functors of
[det-def-sfb-dc-restricted-functors]:

$$
Rf_!^c:=Rp_*\circ i_!\colon D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y,\Lambda).
$$

The *derived lower shriek* is $Rf_!:=Rf_!^{c_f}$ for the chosen compactification $c_f$ of
[det-def-sfb-dc-setting]. No separate preservation statement is needed for $Rf_!$.

The functor $Rf_!^c$ is compatible with the ambient lower shriek
$Rf_!^c=R(p_*)\circ D(i_!)$ on $D(\Mod_{\Lambda_X})$ of [det-def-sfb-module-derived-lower-shriek]:
there is a natural isomorphism $\iota\circ Rf_!^c\cong Rf_!^c\circ\iota$, with $\iota$ the inclusions
of $D_{\mathrm{cons}}$. In particular $Rf_!$ on $D_{\mathrm{cons}}$ is compatible with the ambient
$Rf_!$ for the chosen compactification.
