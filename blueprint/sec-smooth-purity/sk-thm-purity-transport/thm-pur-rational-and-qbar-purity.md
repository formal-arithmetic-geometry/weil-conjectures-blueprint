+++
id = "thm-pur-rational-and-qbar-purity"
kind = "theorem"
title = "Rational and $\\Qlb$ purity"
lean = ["AlgebraicGeometry.Etale.exists_iso_fromIntegral_realization_twistShiftPullbackLevel"]
order = 2370
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-pbc-proetale-site", "def-weil-pbc-qbar-category", "def-weil-pbc-rational-category", "def-weil-scheme-morphism-properties", "prop-pur-rational-purity-transitivity-summands", "prop-weil-pbc-rational-transport", "thm-pur-adic-reconstruction"]
+++
Work in the purity conventions of [def-pur-conventions], let
$f:X\to Y$ be smooth separated of relative dimension $d$ over a
separated finite-type $k$-scheme, and let $K$ lie in the $E$-coefficient
category of [def-weil-pbc-rational-category], respectively the
$\Qlb$-coefficient category of [def-weil-pbc-qbar-category], presented
by a normalized integral system (a lattice) as in
[def-weil-pbc-rational-category]. Then

$$
\gamma_{f,K}:Lf^*K(d)[2d]\xrightarrow{\ \sim\ }Rf^!K
$$

is an isomorphism in the corresponding category: rationalization along
[prop-weil-pbc-rational-transport] and finite extension of coefficient
fields carry the adic purity isomorphism of
[thm-pur-adic-reconstruction] to the $E$- and $\Qlb$-purity
isomorphisms.
