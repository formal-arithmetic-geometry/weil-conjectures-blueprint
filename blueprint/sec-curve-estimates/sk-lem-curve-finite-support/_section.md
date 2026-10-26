+++
id = "sk-lem-curve-finite-support"
kind = "lemma"
title = "Finite-support sheaves and finite maps"
order = 1441
lean = ["AlgebraicGeometry.zero_dimensional_etale_cohomology", "AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_topologicalKrullDim_le_zero", "AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.rightDerivedFunctorLowerStarIsoMapDerivedCategory", "AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite"]
uses = ["sk-prop-sf-comparison"]
tags = ["sketch"]
+++
A classical sheaf supported on finitely many closed points of a curve over an
algebraically closed field has no positive cohomology. Its sections are the
direct sum of its stalks, unchanged under algebraically closed extension. For
a finite morphism $h\colon Y\to C$, the direct image $h_*$ of classical
sheaves is exact, commutes with arbitrary base change, and satisfies
$H^q(C,h_*G)=H^q(Y,G)$.
