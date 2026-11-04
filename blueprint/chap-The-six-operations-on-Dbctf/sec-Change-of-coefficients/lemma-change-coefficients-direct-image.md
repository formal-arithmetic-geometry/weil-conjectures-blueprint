+++
id = "lemma-change-coefficients-direct-image"
kind = "lemma"
title = "Change of coefficients for direct image"
order = 629
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicIntegers_of_isGE", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjMap", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicSubfieldRingObjToPadicAlgCl_of_isGE", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedUpperStarExtendScalarsPushHom_integersModPow_app"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-proper-direct-image-unbounded-complexes", "definition-change-of-coefficients-maps"]
+++
For each map $\Lambda\to\Lambda'$ listed above, every morphism $f:X\to Y$
of schemes of finite type over $k$ and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the
map $(Rf_*K)_{\Lambda'}\to Rf_*(K_{\Lambda'})$ of
Definition [definition-change-of-coefficients-maps](4) is an
isomorphism.
