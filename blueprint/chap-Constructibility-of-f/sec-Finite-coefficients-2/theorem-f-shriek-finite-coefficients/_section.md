+++
id = "theorem-f-shriek-finite-coefficients"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 593
lean = ["AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedUpperShriek", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.DerivedCategoryFiniteTor.rightDerivedLowerShriekAdjunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "proposition-composition-open-restriction-compactifications-f", "definition-compactification-refinement"]
+++
For every separated morphism $f:X\to Y$ of finite type, the right adjoint
$f^!:\Loc(D^b_{\mathrm{ctf}}(Y,A))\to\Loc(D^b_{\mathrm{ctf}}(X,A))$ of
Theorem [theorem-existence-exceptional-inverse-image] maps $D^b_{\mathrm{ctf}}(Y,A)$ into $D^b_{\mathrm{ctf}}(X,A)$.
Consequently, its adjunction restricts to

$$
Rf_!:D^b_{\mathrm{ctf}}(X,A)\ \rightleftarrows\ D^b_{\mathrm{ctf}}(Y,A):f^!.
$$
