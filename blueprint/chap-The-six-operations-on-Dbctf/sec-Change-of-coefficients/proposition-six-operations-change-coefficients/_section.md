+++
id = "proposition-six-operations-change-coefficients"
kind = "proposition"
title = "The six operations and change of coefficients"
order = 645
lean = [
  "AlgebraicGeometry.ProEtale.boundedConstructible_leftDerivedExtendScalars_obj",
  "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_integersModPowReduction",
  "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_residueField",
  "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarExtendScalarsIso",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicIntegers_of_isGE",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjMap",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicSubfieldRingObjToPadicAlgCl_of_isGE",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedUpperStarExtendScalarsPushHom_residueField_app",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerStarIntegersModPowReduction'",
  "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekExtendScalarsIso",
  "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekToPadicAlgClIso",
  "AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionLowerShriekIsoOfCompactification",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleUpperShriekExtendScalars",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleUpperShriekToPadicAlgCl",
  "AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionUpperShriekIso",
  "AlgebraicGeometry.ProEtale.CondensedRing.derivedExtendScalarsTensorIso",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_leftDerivedIntegersModPowReduction",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_derivedExtendScalarsSubfield",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_boundedConstructibleExtendScalars",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_constructibleToPadicAlgCl",
  "AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_boundedConstructibleIntegersToPadicAlgCl",
  "AlgebraicGeometry.ProEtale.CondensedRing.derivedPushHom_comp_app",
  "AlgebraicGeometry.ProEtale.CondensedRing.isMonoidal_derivedExtendScalarsCompIso_hom",
  "CategoryTheory.Functor.LaxMonoidal.ihomComparison_comp_app",
  "AlgebraicGeometry.ProEtale.CondensedRing.derivedPullIsoCompCoherence",
  "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarExtendScalarsIsoCompCoherence",
  "AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerStarComp",
  "CategoryTheory.NatTrans.SquareCompatible.unit",
  "CategoryTheory.NatTrans.SquareCompatible.counit",
  "CategoryTheory.Functor.LaxMonoidal.ihomComparison_ev",
]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-change-of-coefficients-maps"]
+++
Let $\Lambda\to\Lambda'$ be one of the maps of coefficient rings listed
above. Extension of scalars sends $D^b_{\mathrm{ctf}}(X,\Lambda)$ into
$D^b_{\mathrm{ctf}}(X,\Lambda')$. For morphisms $f:X\to Y$ of schemes of finite type
over $k$ (separated in the case of $Rf_!$ and $f^!$), the
change-of-coefficients maps of
Definition [definition-change-of-coefficients-maps] and
(7.1) for $f^*$, $Rf_*$, $Rf_!$,
$f^!$, $\otimes^{\mathbf L}$ and $\cHom$ are isomorphisms on objects of
$D^b_{\mathrm{ctf}}(-,\Lambda)$. For a composite $\Lambda\to\Lambda'\to\Lambda''$ of two
such maps, each of these isomorphisms is the composite of the isomorphisms
for $\Lambda\to\Lambda'$ and $\Lambda'\to\Lambda''$. These isomorphisms
are compatible with the composition isomorphisms $(gf)^*\simeq f^*g^*$,
$R(gf)_*\simeq Rg_*Rf_*$, $R(gf)_!\simeq Rg_!Rf_!$ and
$(gf)^!\simeq f^!g^!$ for composable morphisms $f$ and $g$. Under these
isomorphisms, the extensions of scalars of the units and counits of the
adjunctions $f^*\dashv Rf_*$, $Rf_!\dashv f^!$ and
$-\otimes^{\mathbf L}K\dashv\cHom(K,-)$ (the last counit being evaluation)
over $\Lambda$ are the corresponding units and counits over $\Lambda'$.
