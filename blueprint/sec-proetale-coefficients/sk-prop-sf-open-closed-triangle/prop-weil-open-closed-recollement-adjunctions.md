+++
id = "prop-weil-open-closed-recollement-adjunctions"
kind = "theorem"
title = "Adjunctions of the open-closed recollement"
lean = ["AlgebraicGeometry.ProEtale.derivedOpenImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.isIso_openImmersionLowerShriekAdjunction_unit", "CategoryTheory.Adjunction.isIso_mapDerivedCategoryAdjunction_unit", "AlgebraicGeometry.ProEtale.mapDerivedUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.full_rightDerivedFunctor_lowerStar", "AlgebraicGeometry.ProEtale.faithful_rightDerivedFunctor_lowerStar"]
order = 1172
uses = ["def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-extension-by-zero", "def-weil-open-closed-recollement", "def-weil-pbc-proetale-operations", "def-weil-scheme-morphism-properties", "lem-exc-proetale-closed-fully-faithful", "lem-exc-proetale-open-unit", "lem-weil-extension-by-zero-adjunction", "lem-weil-extension-by-zero-exact", "prop-weil-pbc-kinjective-resolutions-exist", "lem-sfb-finite-upper-star-exact"]
tags = ["latex:proposition"]
+++
Let $R$ be a commutative ring, for instance a finite one. For complementary
open and closed immersions $j:U\hookrightarrow X$, $i:Z\hookrightarrow X$ as
in the open-closed recollement, one has $j_!\dashv j^*$ and $i^*\dashv Ri_*$
on the unbounded derived categories of pro-etale sheaves of $R$-modules, the
exact functors $j_!$, $j^*$, $i^*$ being applied termwise. The open unit and
the closed counit are isomorphisms
$$
 \operatorname{id}\xrightarrow{\sim}j^*j_!,\qquad
 i^*Ri_*\xrightarrow{\sim}\operatorname{id};
$$
equivalently $j_!$ and $Ri_*$ are fully faithful.
The operations are those of extension by zero, derived direct image, and
derived pullback, tensor and hom.
