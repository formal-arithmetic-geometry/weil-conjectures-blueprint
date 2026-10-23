+++
id = "fix-prop-adjunctions"
kind = "theorem"
title = "Adjunctions of the datum"
lean = ["AlgebraicGeometry.Etale.mapDerivedUpperStarLowerStarAdjunction_comp_eq", "AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible.leftDerivedUpperStar", "AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible.rightDerivedLowerStar", "AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible.leftDerivedUpperStarAdjunction", "AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible.rightDerivedLowerShriek", "AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible.rightDerivedUpperShriek", "AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible.rightDerivedLowerShriekAdjunction", "AlgebraicGeometry.Etale.rightDerivedUpperShriekAdjunctionOfCompactification", "AlgebraicGeometry.Etale.rightDerivedUpperShriekAdjunctionOfCompactification_comparison", "AlgebraicGeometry.Etale.DerivedCategoryFiniteTor.rightDerivedLowerShriekAdjunction", "AlgebraicGeometry.Etale.DerivedCategoryFiniteTor.leftDerivedUpperStarAdjunction", "AlgebraicGeometry.Etale.rightDerivedUpperShriekLowerStarBaseChangeMap", "AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekLowerStarBaseChangeMap"]
order = 2345
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-fix-six-functor-datum", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-pbc-derived-categories", "def-weil-pbc-inverse-image", "def-sp-kinjective-bridge", "fix-lem-exchanges", "lem-weil-derived-direct-image-composition", "lem-weil-derived-tensor-resolution-independent", "thm-sf-comp-composition", "sk-thm-existence", "sk-def-sfb-dc-upper-shriek", "sk-thm-sf-comp-composition"]
+++
In the six-functor datum of
[def-fix-six-functor-datum]:

1. the derived pullback and the derived direct image form an
adjoint pair
$$
Lf^*\dashv Rf_*
$$
on $D^b_c(Y,\Lambda)$ and $D^b_c(X,\Lambda)$, with unit
$\eta_f:\operatorname{id}\to Rf_*Lf^*$ and counit
$\varepsilon_f:Lf^*Rf_*\to\operatorname{id}$, satisfying the
triangle identities
$$
(Rf_*\varepsilon_f)\circ(\eta_fRf_*)=\operatorname{id}_{Rf_*},
\qquad
(\varepsilon_fLf^*)\circ(Lf^*\eta_f)=\operatorname{id}_{Lf^*};
$$
1. if $f$ is
exceptionally
admissible, the compact-support direct image and the exceptional
inverse image form an adjoint pair
$$
Rf_!\dashv Rf^!
$$
on $D^b_c(X,\Lambda)$ and $D^b_c(Y,\Lambda)$, with unit
$\nu_f:\operatorname{id}\to Rf^!Rf_!$ and counit
$\mu_f:Rf_!Rf^!\to\operatorname{id}$ satisfying the two triangle
identities; the units and counits agree for the refinement
comparisons, and the adjunction restricts to an adjunction
$$
Rf_!:D^b_{ctf}(X,\Lambda)\rightleftarrows
D^b_{ctf}(Y,\Lambda):Rf^!;
$$
1. for composable separated finite-type morphisms
$X\xrightarrow{f}Y\xrightarrow{g}Z$, the unit of
$L(gf)^*\dashv R(gf)_*$ is the composite
$Lf^*\eta_gLf^*\circ\eta_f$ and the counit is the composite of the
counits; for the exceptional pair the unit and counit of
$R(gf)_!\dashv R(gf)^!$ are the pasted units and counits of
$Rf_!\dashv Rf^!$ and $Rg_!\dashv Rg^!$ under the composition
law of [thm-sf-comp-composition], i.e. the mate of
the composition isomorphism;
1. the adjunction is compatible with the exchange
transformations: the transpose of $\operatorname{Ex}_!$ is
the corresponding exceptional-inverse-image identification, and
$\operatorname{Ex}_*$ is the transpose of the base-change
composite of [def-exchange-projection].
