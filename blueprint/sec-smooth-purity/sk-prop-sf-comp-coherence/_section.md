+++
id = "sk-prop-sf-comp-coherence"
kind = "proposition"
title = "Coherence of the compactification comparisons"
order = 1872
uses = ["sk-def-sf-operations", "sk-prop-nagata-sketch-comp-category", "sk-thm-properbasechange"]
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_id", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_comp"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be separated of finite type and let $u:c_1\to c_2$ be a
refinement in $\operatorname{Comp}(f)$. Then the canonical map

$$
\alpha_u:\ j_{2!}K\ \xrightarrow{\ \sim\ }\ Ru_*j_{1!}K
$$

is an isomorphism for every étale-origin $K$; it is the identity for the
identity refinement and is transitive under composition of refinements.
Consequently the induced comparison of candidates

$$
R\bar f_{1*}j_{1!}\ \xrightarrow{\ \sim\ }\ R\bar f_{2*}j_{2!}
$$

is an isomorphism with the same two properties, and comparison through a
common refinement gives, for any two $c_1,c_2\in\operatorname{Comp}(f)$, a
natural isomorphism $Rf_!^{c_1}\cong Rf_!^{c_2}$ which is independent of the
chosen common refinement and satisfies the cocycle condition for triples. In
this sense $Rf_!$ of [sk-def-sf-operations] (iv) is well defined.
