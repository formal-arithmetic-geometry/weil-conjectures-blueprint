+++
id = "lemma-inverse-image-coefficient-sheaves"
kind = "lemma"
title = "Inverse image of the coefficient sheaves"
order = 187
lean = ["AlgebraicGeometry.ProEtale.isMonHom_condensedPullbackHom", "AlgebraicGeometry.ProEtale.isIso_condensedPullbackHom", "AlgebraicGeometry.Etale.leftDerivedUpperStarTateTwistObjectIso", "AlgebraicGeometry.ProEtale.CondensedRing.exists_comap_regular_iso_finiteFree"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "prose-02-50", "prose-02-51", "definition-tate-twists"]
+++
Let $f:X\to Y$ be a morphism of schemes.

1. For every admissible $\Lambda$, the canonical map
   $$
   f^{-1}\Lambda_Y\longrightarrow\Lambda_X
   $$
   is an isomorphism of sheaves of rings. The same holds for its Tate
   twists, including the twists of a finite ring $A$.
2. If $E\subset E'$ is a finite extension, then $\mathcal O_{E',X}$ is a
   finite free $\mathcal O_{E,X}$-module and $E'_X$ is a finite free
   $E_X$-module.
