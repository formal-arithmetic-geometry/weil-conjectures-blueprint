+++
id = "lem-weil-pbc-finite-exchange"
kind = "lemma"
title = "Finite exchange"
order = 1547
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange-detailed", "lem-weil-pbc-finite-direct-image-exact", "lem-weil-pbc-finite-stalk-formula"]
+++
In a cartesian square with $f$ finite, the underived exchange map is the
bijection obtained by base changing the finite geometric fiber:

$$
 g^{-1}f_*F\xrightarrow{\sim}f'_*g'^{-1}F.
$$

The isomorphism is compatible with the stalk formula on both sides, and the
derived exchange morphism [def-weil-pbc-derived-exchange-detailed] is an isomorphism.

## Proof

At a geometric point $\bar y'\to Y'$, the two underived sides identify, via
[lem-weil-pbc-finite-stalk-formula], with the same finite direct sum of stalks
indexed by the geometric points of the finite fibre; expanding the
unit--$\theta_\square$--counit composite of
[def-weil-pbc-underived-exchange-detailed] shows that the induced map is the identity
on every summand, hence an isomorphism. By
[lem-weil-pbc-finite-direct-image-exact] both direct images are exact, so the
same degreewise comparison computes the derived exchange morphism.
