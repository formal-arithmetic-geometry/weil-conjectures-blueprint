+++
id = "proposition-compatibility-purity-base-change"
kind = "proposition"
title = "Compatibility of purity with base change"
order = 797
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_baseChange"]
uses = ["definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients"]
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
