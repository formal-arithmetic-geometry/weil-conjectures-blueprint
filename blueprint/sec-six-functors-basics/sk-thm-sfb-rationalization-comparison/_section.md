+++
id = "sk-thm-sfb-rationalization-comparison"
kind = "proposition"
title = "Inverting $\\ell$"
order = 2316
uses = ["sk-prop-sfb-qlbar-colimit-x", "sk-def-sfb-constructible"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersRingObjToContinuousMapRingObj", "AlgebraicGeometry.ProEtale.padicIntegersToPadicSubfield", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_obj", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalarsCompatibility", "AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso", "CategoryTheory.Rationalization.tensorHomEquiv"]
tags = ["sketch"]
+++
Assume that the underlying topological space of $X$ is Noetherian (for
instance, $X$ of finite type over a field). A complex in
$\Dbc(X,\cO_E)$ ([sk-def-sfb-constructible]) that is killed by inverting $\ell$ is killed by a
fixed power of $\ell$, and extension of scalars ([sk-prop-sfb-qlbar-colimit-x])
induces an equivalence

$$
 \Dbc(X,\cO_E)[\ell^{-1}]\xrightarrow{\ \sim\ }\Dbc(X,E),
$$

where the source category has the objects of $\Dbc(X,\cO_E)$ and
Hom groups tensored with $E$.
