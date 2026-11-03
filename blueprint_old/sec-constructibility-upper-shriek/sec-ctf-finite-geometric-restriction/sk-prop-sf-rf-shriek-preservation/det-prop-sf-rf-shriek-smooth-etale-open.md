+++
id = "det-prop-sf-rf-shriek-smooth-etale-open"
kind = "proposition"
title = "$f^!$ for open immersions, finite étale and smooth morphisms"
order = 2717
uses = ["lem-amb-etale-adjoint-locality", "prop-exc-finite-etale-adjoint", "thm-asd-smooth-tensor", "lem-sf-flat-model"]
lean = ["AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isOpenImmersion", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_isFinite_of_etale", "AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedUpperShriek_of_smoothOfRelativeDimension"]
+++
Let $A$ be a finite commutative ring whose exponent is invertible on the schemes
involved, and let $K$ be a bounded constructible $A$-complex on $Y$ with Tor
amplitude in $[a,b]$.

1. If $f:X\to Y$ is an open immersion, or a finite étale morphism, then
   $f^!\simeq f^*$, and $f^!K$ is bounded constructible with Tor amplitude in
   $[a,b]$.
2. If $f:X\to Y$ is smooth of pure relative dimension $d$, then
   $f^!K\simeq f^*K\otimes^{\mathbf L}_A\omega_f$ with $\omega_f[-2d]$ a
   locally constant sheaf of free rank-one $A$-modules, so that locally on $X$
   the functor $f^!$ is isomorphic to $f^*(-)(d)[2d]$; in particular $f^!K$ is
   bounded constructible with Tor amplitude in $[a-2d,b-2d]$.

(The canonical global isomorphism $f^!\simeq f^*(d)[2d]$ for smooth $f$ is
constructed in the smooth-purity chapter.)
