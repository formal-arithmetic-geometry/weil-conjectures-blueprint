+++
id = "lem-weil-pbc-underived-proper-exchange"
kind = "lemma"
title = "Underived proper exchange"
order = 2117
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isProper"]
uses = ["def-weil-pbc-underived-exchange-detailed", "def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-scheme-conventions", "def-weil-pbc-etale-sheaves", "prop-weil-pbc-strict-henselization-stalk-formula-detailed", "lem-weil-pbc-degree-zero-strict-henselian", "lem-weil-pbc-geometric-stalk-conservative"]
+++
For a cartesian square [def-weil-pbc-cartesian-square-detailed] with $f$
proper [def-weil-pbc-scheme-conventions] and every torsion etale sheaf
[def-weil-pbc-etale-sheaves] $F$ on $X_{\Et}$, the map

$$
 \Ex^0_{\square,F}:g^{-1}f_*F\xrightarrow{\sim}f'_*g'^{-1}F
$$

of [def-weil-pbc-underived-exchange-detailed] is an isomorphism.

## Proof

Fix a geometric point $\bar y'=\operatorname{Spec}\Omega\to Y'$ and let $\bar
y$ be its composite with $Y'\to Y$. By
[prop-weil-pbc-strict-henselization-stalk-formula-detailed], the stalks of
both sides at $\bar y'$ are computed by sections on the fibres over the
strict henselizations of the two residue fields, and
[lem-weil-pbc-degree-zero-strict-henselian] identifies those sections with
sections on the corresponding closed geometric fibres. The chosen
identification of [def-weil-pbc-cartesian-square-detailed] identifies these
two fibres and the two coefficient sheaves, and expanding the
unit--$\theta_\square$--counit composite of
[def-weil-pbc-underived-exchange-detailed] shows that the induced stalk map
is the identity under these identifications. Geometric stalks are
conservative by [lem-weil-pbc-geometric-stalk-conservative], so the map is an
isomorphism.
