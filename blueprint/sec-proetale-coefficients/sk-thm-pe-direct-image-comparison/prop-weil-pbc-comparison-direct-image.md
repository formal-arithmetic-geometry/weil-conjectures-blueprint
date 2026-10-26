+++
id = "prop-weil-pbc-comparison-direct-image"
kind = "theorem"
title = "Comparison direct image"
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerStarComparisonPlusIso", "AlgebraicGeometry.ProEtale.rightDerivedLowerStarMapDerivedCategoryObjIso", "AlgebraicGeometry.ProEtale.isIso_lowerStarComparisonUpperStarBaseChange", "AlgebraicGeometry.ProEtale.rightAcyclic_lowerStar_comparisonUpperStar_obj_of_injective"]
order = 1011
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-ind-etale-basis", "def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-global-cohomology", "lem-weil-pbc-comparison-pullback", "lem-weil-pbc-comparison-sections", "lem-weil-pbc-derived-cohomology-continuity", "lem-weil-pbc-etale-restriction-injectives", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-proetale-restriction-injectives", "prop-weil-pbc-inverse-image-exact", "lem-sfb-finite-upper-star-exact"]
tags = ["latex:proposition"]
+++
Let $u:U\to V$ be quasi-compact and quasi-separated and let
$L\in\Dplus(U_{\Et},\Lambda)$. There is a natural isomorphism

$$
 \nu_V^*Ru_{\Et,*}L
 \xrightarrow{\sim}
 Ru_{\Proet,*}\nu_U^*L.
$$

It is the base-change morphism of right derived functors induced by the mate
$\nu_V^*u_{\Et,*}\to u_{\Proet,*}\nu_U^*$ of the identification
$\nu_{V,*}u_{\Proet,*}\simeq u_{\Et,*}\nu_{U,*}$.
