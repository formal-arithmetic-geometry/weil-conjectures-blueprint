+++
id = "lem-weil-delta-restriction"
kind = "lemma"
title = "The double-dual morphism restricts"
lean = ["AlgebraicGeometry.Etale.isIso_mapDerivedUpperStarLowerStarAdjunction_counit", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_iff_lowerShriek", "AlgebraicGeometry.Etale.isIso_upperStar_map_verdierDualDoubleDual_app_iff_of_isIso", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_mapDerivedCategory_upperStar_iff", "AlgebraicGeometry.Etale.verdierDualLowerShriekIso", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_leftDerivedUpperStar_iff", "AlgebraicGeometry.Etale.isIso_of_forall_isIso_leftDerivedUpperStar_map", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_iff_of_openCover", "CategoryTheory.Adjunction.isIso_map_unit_app_iff_of_iso", "AlgebraicGeometry.Etale.isIso_map_verdierDualDoubleDual_app_iff_lowerShriek", "AlgebraicGeometry.Etale.isIso_map_upperStar_map_verdierDualDoubleDual_app_iff_of_isIso", "AlgebraicGeometry.Etale.isIso_map_verdierDualDoubleDual_app_mapDerivedCategory_upperStar_iff", "AlgebraicGeometry.Etale.isIso_map_verdierDualDoubleDual_app_leftDerivedUpperStar_iff", "CategoryTheory.MonoidalClosed.dualComparison", "CategoryTheory.MonoidalClosed.map_toIhomIhom_comp_dualComparison", "CategoryTheory.MonoidalClosed.mapToIhomIhomArrowIso", "CategoryTheory.MonoidalClosed.isIso_map_toIhomIhom_iff", "AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_of_surjective"]
order = 2827
uses = ["def-weil-derived-pullback-tensor-hom", "lem-amb-etale-adjoint-locality", "lem-weil-duality-pairing"]
+++
Let $j:W\to Y$ be etale between separated finite-type schemes over
a field, with finite coefficients invertible there. For the ambient
etale dualizing objects, the canonical identifications
$j^*\omega_Y=\omega_W$ and $j^*D_Y=D_Wj^*$ identify
$j^*\delta_K$ with $\delta_{j^*K}$. Thus biduality is local
for the etale topology. The same restriction calculation applies
to the finite pro-etale realization.
