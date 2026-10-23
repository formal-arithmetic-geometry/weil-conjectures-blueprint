+++
id = "thm-amb-etale-exceptional-adjoint"
kind = "theorem"
title = "The ordinary ambient exceptional adjoint"
lean = ["CategoryTheory.Functor.isLeftAdjoint_of_compactGenerators", "CategoryTheory.Functor.isLeftAdjoint_of_isLeftAdjoint_comp", "DerivedCategory.isLeftAdjoint_of_preservesCoproducts", "AlgebraicGeometry.Etale.isLeftAdjoint_rightDerivedLowerShriekOfCompactification", "AlgebraicGeometry.Etale.isLeftAdjoint_rightDerivedLowerShriek"]
order = 2696
uses = ["def-amb-etale-compact-support", "def-weil-compactifications-refinements", "def-weil-pbc-derived-categories", "lem-amb-etale-compact-comparisons", "lem-amb-proper-coproducts"]
+++
Let $f:X\to S$ admit a compactification
$X\xrightarrow{j}\overline X\xrightarrow{r}S$ between
Noetherian schemes, with $j$ open and $r$ proper of finite
type. The ambient functor $Rf_!=Rr_*j_!$ on ordinary derived
categories of etale $A$-module sheaves has a right adjoint,
denoted $f^\times$. No restriction to a constructible
subcategory is made in this assertion.
