+++
id = "sk-def-sfb-dc-restricted-functors"
kind = "lemma"
title = "Inverse image and tensor product"
order = 1584
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_leftDerivedUpperStar_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStar", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerStar", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_openImmersionLowerShriek_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_derivedTensor_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_derivedHom_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleTensor", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleHom", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleTensorHomAdjunction"]
uses = ["sk-def-sfb-dc-setting", "sk-def-sfb-derived-tensor-hom", "sk-thm-sfb-rationalization-comparison", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-int-integral-heart"]
tags = ["sketch"]
+++
Inverse image $g^*\colon\D(Y_{\mathrm{proét}},\mathcal O_E)\to\D(X_{\mathrm{proét}},\mathcal O_E)$ along a morphism $g\colon X\to Y$
preserves $\Dbc(-,\mathcal O_E)$, and on these categories it agrees, after restriction of scalars to
$\underline{\mathcal O_E}$, with the completed inverse image of the Stacks Project. For
$K,L\in\Dbc(X,\mathcal O_E)$, the tensor product $K\otimes_{\mathcal O_{E,X}}^{\mathbf L}L\in\D(X_{\mathrm{proét}},\mathcal O_E)$,
without completion, lies in $\Dbc(X,\mathcal O_E)$. Extension by zero along a quasi-compact open immersion and
direct image along a closed immersion preserve $\Dbc(-,\mathcal O_E)$.

Arguments by dévissage along a stratification need inverse image, tensor products and extension by zero
along strata to preserve integral constructible complexes; these are the statements above.
