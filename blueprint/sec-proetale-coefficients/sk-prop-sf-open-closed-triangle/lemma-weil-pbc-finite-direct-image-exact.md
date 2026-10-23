+++
id = "lemma-weil-pbc-finite-direct-image-exact"
kind = "lemma"
title = "Exactness of finite direct image"
order = 1096
lean = ["AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.rightDerivedFunctorLowerStarIsoMapDerivedCategory"]
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $f:X\to Y$ be a finite morphism of schemes and let $\mathcal A$ be a
Grothendieck abelian coefficient category for which presheaves on small etale
sites can be sheafified, which is concrete over sets with a forgetful functor
that reflects isomorphisms, preserves filtered colimits and is compatible with
the sheaf condition on $Y_{\Et}$ (for instance $\mathcal A=\Mod_\Lambda$).
Then the direct image $f_*:\shv{X_{\Et},\mathcal A}\to\shv{Y_{\Et},\mathcal A}$
is exact. Consequently, whenever the derived categories of $\mathcal A$-valued
etale sheaves on $X$ and $Y$ exist and every complex of sheaves on $X$ has a
K-injective resolution, the total right derived functor $Rf_*$ is isomorphic
to $f_*$ applied termwise to complexes; in particular $R^qf_*=0$ for $q>0$.
