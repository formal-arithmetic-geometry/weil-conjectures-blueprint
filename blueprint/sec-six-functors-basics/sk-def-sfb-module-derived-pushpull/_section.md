+++
id = "sk-def-sfb-module-derived-pushpull"
kind = "definition"
title = "Derived pushforward and pullback of module objects"
order = 1685
uses = ["sk-def-sfb-derived-categories"]
lean = ["CategoryTheory.Functor.rightDerivedFunctorPlus", "AlgebraicGeometry.ProEtale.CondensedRing.preservesKFlatQuasiIso_upperStar", "CategoryTheory.Adjunction.derivedAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes, with the functors $f_*=\operatorname{Res}_{\eta_f}\circ
\operatorname{mapMod}(f^{\Ab}_*)$ and $f^*=\operatorname{Ext}_{\alpha_f}\circ
\operatorname{mapMod}(f^*_{\Ab})$ on module objects
([sk-def-sfb-module-pushforward-pullback]). The derived pushforward and pullback are
the *total derived functors of these composites* ([sk-def-sfb-derived-categories]):

$$
Rf_*:=R\bigl(\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f^{\Ab}_*)\bigr)
\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y}),
$$

computed on K-injective resolutions in $\Mod_{\Lambda_X}$, with bounded below version
$R^+f_*\colon D^+(\Mod_{\Lambda_X})\to D^+(\Mod_{\Lambda_Y})$, and

$$
Lf^*:=L\bigl(\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*_{\Ab})\bigr)
\colon D(\Mod_{\Lambda_Y})\to D(\Mod_{\Lambda_X}),
$$

computed on K-flat resolutions in $\Mod_{\Lambda_Y}$: for a K-flat resolution
$P\to M$ one has $Lf^*M\cong\Lambda_X\otimes_{f^*\Lambda_Y}f^*_{\Ab}P$. They are the general
derived functors applied to the underived functors, not separate constructions; in
particular they are not built from the derived functors of abelian sheaves. The
adjunction $f^*\dashv f_*$ derives to an adjunction

$$
Lf^*\dashv Rf_* .
$$

The composite is derived, rather than the factors, because the derived adjunction is
then obtained directly from $f^*\dashv f_*$ (a composite of derived functors would
require composing two derived adjunctions through an intermediate category), and
because the universal property of derived functors then applies to the functor one
cares about. The factorizations of $Rf_*$ and $Lf^*$ through the factors are kept as
theorems, proved below.
