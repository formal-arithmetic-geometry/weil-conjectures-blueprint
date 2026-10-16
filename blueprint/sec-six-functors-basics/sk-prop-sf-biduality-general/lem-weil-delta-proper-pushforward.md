+++
id = "lem-weil-delta-proper-pushforward"
kind = "lemma"
title = "The double-dual morphism under a proper push-forward"
lean = ["AlgebraicGeometry.Etale.map_verdierDualDoubleDual_app_comp_mateEquiv", "AlgebraicGeometry.Etale.verdierDualRightDerivedLowerStarSquare", "AlgebraicGeometry.Etale.isIso_verdierDualRightDerivedLowerStarSquare_app", "AlgebraicGeometry.Etale.isIso_map_verdierDualDoubleDual_app_iff_of_isIso_mateEquiv", "CategoryTheory.Adjunction.rightAdjointLaxBraidedOf\u03b4", "CategoryTheory.Adjunction.whiskerLeft_unit_comp_rightAdjointLaxMonoidal_\u03bc", "CategoryTheory.Adjunction.isIso_dualComparison_of_isIso_projection", "CategoryTheory.Adjunction.isIso_map_toIhomIhom_iff_of_isIso_projection", "CategoryTheory.Adjunction.nonempty_arrowIso_map_toIhomIhom_of_isIso_projection", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStar_map_verdierDualDoubleDual_app_iff", "AlgebraicGeometry.Etale.nonempty_arrowIso_rightDerivedLowerStar_map_verdierDualDoubleDual", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStar_map_verdierDualDoubleDual_app_iff_of_finite", "CategoryTheory.MonoidalClosed.isIso_pre_app"]
order = 2467
uses = ["lem-amb-proper-coproducts-projection", "lem-weil-duality-pairing", "prop-asd-internal-adjunction", "thm-amb-etale-exceptional-adjoint"]
+++
Let $f:X\to Y$ be a proper morphism of separated finite-type
schemes over a field, and use finite coefficients invertible there.
On the ambient etale derived categories let
$\omega_T=Ra_T^{\times}A$ and
$D_T=R\mathcal Hom_A(-,\omega_T)$. For every complex $K$,
the ambient exchange $D_YRf_*\cong Rf_*D_X$ identifies
$Rf_*\delta_K$ with $\delta_{Rf_*K}$. In particular, if the
latter is an isomorphism then so is the former.
Neither exceptional-adjoint admissibility on a constructible
subcategory nor geometric biduality is assumed.
