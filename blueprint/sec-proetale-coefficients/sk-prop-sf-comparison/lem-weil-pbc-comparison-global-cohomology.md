+++
id = "lem-weil-pbc-comparison-global-cohomology"
kind = "lemma"
title = "Comparison of global cohomology"
order = 1046
lean = ["AlgebraicGeometry.ProEtale.comparisonLowerStarCompRightDerivedGlobalSectionsIso", "AlgebraicGeometry.ProEtale.isIso_derivedComparisonAdjunction_unit_app", "AlgebraicGeometry.ProEtale.rightDerivedGlobalSectionsFunctorComparisonUpperStarObjIso"]
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-etale-cohomology", "def-weil-pbc-site-comparison-morphism", "prop-weil-pbc-site-comparison-finite-level", "thm-weil-pbc-site-comparison"]
+++
For a ring $\Lambda$ and $K\in\Dplus(T_{\Et},\Lambda)$, the derived unit
induces a natural isomorphism

$$
 R\Gamma(T_{\Et},K)\xrightarrow{\sim}
 R\Gamma(T_{\Proet},\nu_T^*K).
$$

Both functors are ordinary derived sections.
