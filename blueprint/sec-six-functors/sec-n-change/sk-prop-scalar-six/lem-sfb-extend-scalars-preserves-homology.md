+++
id = "lem-sfb-extend-scalars-preserves-homology"
kind = "lemma"
title = "A flat change of coefficients is exact"
order = 2829
uses = ["det-def-sfb-coefficient-change", "det-def-sfb-change-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesHomology_extendScalars_coefficientMap"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings such that for every
scheme $X$ the extension of scalars $\operatorname{Ext}_{a_X}$ along the coefficient change
([det-def-sfb-coefficient-change]) preserves finite limits. Then each
$\operatorname{Ext}_{a_X}$ preserves homology (of complexes of $\Lambda_X$-modules).
