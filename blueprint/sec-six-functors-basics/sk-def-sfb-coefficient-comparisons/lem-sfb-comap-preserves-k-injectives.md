+++
id = "lem-sfb-comap-preserves-k-injectives"
kind = "lemma"
title = "Flat restriction of scalars preserves K-injectives"
order = 2594
uses = ["sk-def-sfb-coefficient-change", "det-def-sfb-change-of-scalars", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesKInjectiveComplexes_comap_coefficientMap"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings such that for every
scheme $X$ the extension of scalars $\operatorname{Ext}_{a_X}$ preserves finite limits
([sk-def-sfb-coefficient-change]). Then for every scheme $X$ the restriction of scalars
$\operatorname{Res}_{a_X}\colon\Mod_{\Lambda'_X}\to\Mod_{\Lambda_X}$ sends K-injective complexes
([det-def-sfb-derived-categories]) to K-injective complexes.
