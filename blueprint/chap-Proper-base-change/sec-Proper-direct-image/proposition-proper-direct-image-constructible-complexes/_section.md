+++
id = "proposition-proper-direct-image-constructible-complexes"
kind = "proposition"
title = "Proper direct image of constructible complexes"
order = 425
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar_of_isProper_of_isNoetherian", "AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj", "AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_obj_of_ringChar_ne", "AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl", "AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerStarProjectionMap_app_app_of_boundedConstructible_of_field", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_padicIntegersRingObj_of_boundedConstructible", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMorphism_boundedConstructible_padicAlgCl"]
uses = ["definition-constructible-sheaves", "definition-pro-etale-base-change-map", "definition-projection-formula-map"]
+++
Let $p:X\to Y$ be proper and let $\Lambda$ be admissible.

1. $Rp_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$ maps
   $D^b_{\mathrm{ctf}}(X,\Lambda)$ into $D^b_{\mathrm{ctf}}(Y,\Lambda)$.
2. For a cartesian square with $g:Y'\to Y$, $g':X'\to X$ and
   $p':X'\to Y'$, the base change map (4.5)
   $g^*Rp_*\to Rp'_*g'^*$ is an isomorphism of functors
   $D^b_{\mathrm{ctf}}(X,\Lambda)\to D^b_{\mathrm{ctf}}(Y',\Lambda)$.
3. The projection formula map (4.14)
   is an isomorphism for $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and $M\in D^b_{\mathrm{ctf}}(Y,\Lambda)$.
