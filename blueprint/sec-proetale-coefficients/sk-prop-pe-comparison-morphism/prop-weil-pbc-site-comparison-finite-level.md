+++
id = "prop-weil-pbc-site-comparison-finite-level"
kind = "theorem"
title = "Exactness and full faithfulness at finite level"
lean = ["AlgebraicGeometry.ProEtale.preservesFiniteLimits_comparisonUpperStar", "AlgebraicGeometry.ProEtale.preservesFiniteColimits_comparisonUpperStar", "AlgebraicGeometry.ProEtale.isIso_comparisonAdjunction_unit", "AlgebraicGeometry.ProEtale.rightAcyclic_comparisonUpperStar_obj_of_injective"]
order = 994
uses = ["def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-injective-acyclicity", "lem-weil-pbc-comparison-sections", "lem-weil-pbc-ind-etale-basis"]
tags = ["latex:proposition"]
+++
Let $T$ be a scheme and $\Lambda$ a ring. On sheaves of $\Lambda$-modules,
$\nu_T^*$ is exact, its unit

$$
 F\longrightarrow\nu_{T,*}\nu_T^*F
$$

is an isomorphism for every etale $\Lambda$-module sheaf, and

$$
 R^q\nu_{T,*}\nu_T^*I=0\qquad(q>0)
$$

for every injective etale $\Lambda$-module sheaf $I$.
