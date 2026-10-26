+++
id = "sk-prop-sf-rf-shriek-preservation"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 2385
uses = ["sk-def-sf-admissible", "sk-prop-sf-open-closed-triangle", "sk-def-purity-conv", "sk-lem-sf-mate", "sk-prop-sf-existence"]
lean = ["AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isOpenImmersion", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isFinite_of_etale", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isClosedImmersion", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_smoothOfRelativeDimension", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative $\ell$-primary ring. For every separated
finite-type morphism $f:X\to Y$, the right adjoint
$f^!\colon\Loc(\Dctf(Y,A))\to\Loc(\Dctf(X,A))$ of [sk-prop-sf-existence]
satisfies

$$
f^!\bigl(\Dctf(Y,A)\bigr)\subseteq\Dctf(X,A).
$$

Consequently its adjunction restricts to

$$
Rf_!:\Dctf(X,A)\ \rightleftarrows\ \Dctf(Y,A):f^!.
$$

For smooth $f$ of pure relative dimension $d$, the functor
$f^!\colon\Dctf(Y,A)\to\Dctf(X,A)$ is locally on $X$ isomorphic to
$f^*(-)(d)[2d]$. (The canonical global isomorphism for smooth $f$ is
constructed in the smooth-purity chapter.)
