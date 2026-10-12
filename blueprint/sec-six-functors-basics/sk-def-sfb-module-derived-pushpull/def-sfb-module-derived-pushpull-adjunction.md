+++
id = "def-sfb-module-derived-pushpull-adjunction"
kind = "definition"
title = "The derived adjunction $Lf^*\\dashv Rf_*$ on module objects"
order = 1685
uses = ["def-sfb-module-upper-lower-adjunction", "lem-sfb-module-upper-star-kflat-quasi-iso", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The adjunction $f^*\dashv f_*$ on module objects
([def-sfb-module-upper-lower-adjunction]) induces an adjunction

$$
Lf^*\dashv Rf_*
$$

between the total left derived functor of $f^*$, computed on K-flat resolutions in
$\Mod_{\Lambda_Y}$ ([lem-sfb-module-upper-star-kflat-quasi-iso]), and the total right
derived functor of $f_*$, computed on K-injective resolutions in $\Mod_{\Lambda_X}$
([sk-def-sfb-derived-categories]).
