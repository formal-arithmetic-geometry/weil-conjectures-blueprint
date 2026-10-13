+++
id = "lem-sfb-module-upper-star-kflat-quasi-iso"
kind = "lemma"
title = "The pullback of module objects preserves K-flat quasi-isomorphisms"
order = 1701
uses = ["sk-def-sfb-module-pushforward-pullback", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesKFlatQuasiIso_upperStar"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The pullback $f^*\colon\Mod_{\Lambda_Y}\to\Mod_{\Lambda_X}$ of module objects
([sk-def-sfb-module-pushforward-pullback]), applied termwise, sends quasi-isomorphisms
between K-flat complexes of $\Lambda_Y$-modules to quasi-isomorphisms
([sk-def-sfb-derived-categories]).
