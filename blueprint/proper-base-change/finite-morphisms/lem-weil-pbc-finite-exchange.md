+++
id = "lem-weil-pbc-finite-exchange"
kind = "lemma"
title = "Finite exchange"
order = 1073
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite", "AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_of_isFinite"]
uses = ["lem-weil-pbc-finite-stalk-formula", "lem-weil-pbc-finite-direct-image-exact", "def-weil-pbc-underived-exchange", "def-weil-pbc-derived-exchange", "def-weil-pbc-cartesian-square"]
+++
In a cartesian square with $f$ finite, the underived exchange map is the
bijection obtained by base changing the finite geometric fiber:

$$
 g^{-1}f_*F\xrightarrow{\sim}f'_*g'^{-1}F.
$$

The isomorphism is compatible with the stalk formula on both sides, and the
derived exchange morphism [def-weil-pbc-derived-exchange] is an isomorphism.

## Proof

At a geometric point $\bar y'\to Y'$, the two underived sides identify, via
[lem-weil-pbc-finite-stalk-formula], with the same finite direct sum of stalks
indexed by the geometric points of the finite fibre; expanding the
unit--$\theta_\square$--counit composite of
[def-weil-pbc-underived-exchange] shows that the induced map is the identity
on every summand, hence an isomorphism. By
[lem-weil-pbc-finite-direct-image-exact] both direct images are exact, so the
same degreewise comparison computes the derived exchange morphism.

Unresolved dependencies: def:weil-pbc-scheme-conventions
