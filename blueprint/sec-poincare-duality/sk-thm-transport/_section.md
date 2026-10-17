+++
id = "sk-thm-transport"
kind = "proposition"
title = "Duality and change of coefficients"
lean = ["AlgebraicGeometry.Etale.isPerfectPairing_poincarePairing_reductionModIdeal", "AlgebraicGeometry.Etale.derivedCompleteIntegral_rightDerivedLowerStar", "AlgebraicGeometry.Etale.derivedCompleteIntegral_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.derivedCompleteIntegral_coefficientDual"]
order = 2752
uses = ["sk-cor-trace", "sk-def-ops", "sk-def-set", "sk-thm-derived-duality", "sk-thm-frobenius", "sk-thm-sf-identification", "sk-thm-sf-package", "sk-prop-scalar-six"]
tags = ["sketch"]
+++
Verdier duality, its double-dual morphism, the two global dualities, the
Poincaré pairing and the top trace commute with every coefficient map listed in
Proposition [sk-prop-scalar-six], including arbitrary maps of finite admissible
rings: the comparison maps of that proposition carry each of them over
$\Lambda$, after extension of scalars, to the corresponding one over
$\Lambda'$. When Weil structures are present, these comparisons are
equivariant.
