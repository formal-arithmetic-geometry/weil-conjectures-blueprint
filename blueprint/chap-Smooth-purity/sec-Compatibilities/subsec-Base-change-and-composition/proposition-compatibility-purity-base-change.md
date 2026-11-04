+++
id = "proposition-compatibility-purity-base-change"
kind = "proposition"
title = "Compatibility of purity with base change"
order = 791
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_baseChange", "AlgebraicGeometry.ProEtale.CondensedRing.map_upperShriekUnitTensorMap_comp_upperShriekBaseChange", "AlgebraicGeometry.Etale.leftDerivedUpperStar_map_comp_smoothPullbackExchange_hom", "AlgebraicGeometry.Etale.smoothPurityTrace_baseChange"]
+++
Let $\Lambda$ be any admissible coefficient ring and let
$K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. Identify the sources by
$g'^{*}f^{*}\simeq(f')^{*}g^{*}$
and the targets by the exceptional base change map of
Definition [definition-exceptional-base-change-map]. Then

$$
g'^{*}\gamma_f(K)
=\gamma_{f'}(g^{*}K)
\quad\text{in }D^b_{\mathrm{ctf}}(X',\Lambda).
$$
