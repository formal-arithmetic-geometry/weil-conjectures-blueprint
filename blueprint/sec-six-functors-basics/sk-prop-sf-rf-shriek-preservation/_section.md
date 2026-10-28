+++
id = "sk-prop-sf-rf-shriek-preservation"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 2712
uses = ["sk-prop-sf-existence", "sk-def-localizing-closure", "sk-def-sfb-constructible"]
lean = ["AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isClosedImmersion", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative $\ell$-primary ring. For every separated
morphism $f:X\to Y$ of finite type, the right adjoint
$f^!\colon\Loc(\Dctf(Y,A))\to\Loc(\Dctf(X,A))$ ([sk-def-localizing-closure],
[sk-def-sfb-constructible]) of [sk-prop-sf-existence] maps $\Dctf(Y,A)$ into
$\Dctf(X,A)$. Consequently, its adjunction restricts to

$$
Rf_!:\Dctf(X,A)\ \rightleftarrows\ \Dctf(Y,A):f^!.
$$
