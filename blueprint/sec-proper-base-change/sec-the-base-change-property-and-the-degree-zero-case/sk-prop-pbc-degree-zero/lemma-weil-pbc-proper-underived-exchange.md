+++
id = "lemma-weil-pbc-proper-underived-exchange"
kind = "lemma"
title = "Underived proper exchange is an isomorphism"
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isProper", "AlgebraicGeometry.Etale.bijective_stalkToFibreSections_of_isProper"]
order = 1655
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange", "lemma-weil-pbc-affine-neighbourhood-cofinal", "def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-geometric-stalk-conservative", "lemma-weil-pbc-proper-strict-henselian-h0", "lemma-weil-pbc-underived-exchange-naturality"]
+++
Let $\Lambda$ be a commutative ring. For a cartesian square
[def-weil-pbc-cartesian-square] with $f$ proper
[def-weil-pbc-scheme-conventions] and every etale sheaf $F$ of
$\Lambda$-modules on $X_{\Et}$ (in particular every etale abelian sheaf
[def-weil-pbc-etale-sheaves]), the map

$$
 \Ex^0_{\square,F}:g^{-1}f_*F\xrightarrow{\sim}f'_*g'^{-1}F
$$

of [def-weil-pbc-underived-exchange] is an isomorphism. Moreover, for an
abelian sheaf $F$ and a geometric point $\bar y:\operatorname{Spec}\Omega\to Y$
with geometric fibre $X_{\bar y}=X\times_Y\operatorname{Spec}\Omega$, the map

$$
 (f_*F)_{\bar y}\xrightarrow{\sim}\Gamma(X_{\bar y},F|_{X_{\bar y}}),
$$

sending a germ represented by a section of $F$ over $X\times_YV$ to its
restriction to the fibre, is bijective.
