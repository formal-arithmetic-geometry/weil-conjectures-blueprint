+++
id = "sk-prop-sf-rf-shriek-preservation"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 352
lean = ["AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isClosedImmersion", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek"]
uses = ["sk-prop-sf-existence", "sk-def-localizing-closure", "sk-def-sfb-constructible"]
tags = ["sketch"]
+++
For every separated morphism $f:X\to Y$ of finite type, the right adjoint
$f^!:\Loc(D^b_{\mathrm{ctf}}(Y,A))\to\Loc(D^b_{\mathrm{ctf}}(X,A))$ of
Theorem [sk-prop-sf-existence] maps $D^b_{\mathrm{ctf}}(Y,A)$ into $D^b_{\mathrm{ctf}}(X,A)$.
Consequently, its adjunction restricts to

$$
Rf_!:D^b_{\mathrm{ctf}}(X,A)\ \rightleftarrows\ D^b_{\mathrm{ctf}}(Y,A):f^!.
$$
