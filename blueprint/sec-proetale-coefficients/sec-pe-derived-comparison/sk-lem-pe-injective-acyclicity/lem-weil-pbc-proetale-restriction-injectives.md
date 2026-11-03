+++
id = "lem-weil-pbc-proetale-restriction-injectives"
kind = "lemma"
title = "Pro-etale localization preserves injectives"
order = 1016
lean = ["AlgebraicGeometry.ProEtale.localizationRestriction", "AlgebraicGeometry.ProEtale.upperStarIsoLocalizationRestriction", "AlgebraicGeometry.ProEtale.preservesInjectiveObjects_localizationRestriction", "AlgebraicGeometry.ProEtale.injective_upperStar_obj_of_weaklyEtale", "CategoryTheory.Functor.rightDerivedCompIsoOfExact", "AlgebraicGeometry.ProEtale.isZero_rightDerived_sectionsFunctor_of_upperStar"]
uses = ["def-weil-pbc-etale-sum-extension", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "def-weil-pbc-proetale-site", "lem-weil-pbc-ind-etale-stability", "lem-sfb-finite-upper-star-exact"]
+++
For a weakly etale $v:W\to X$, the site $W_{\Proet}$ is the slice of
$X_{\Proet}$ over $W$. The restriction functor on constant-coefficient module
sheaves is exact and preserves injectives. Consequently derived evaluation on
$W$, computed in sheaves on $X_{\Proet}$, agrees with derived global sections
on $W_{\Proet}$.
