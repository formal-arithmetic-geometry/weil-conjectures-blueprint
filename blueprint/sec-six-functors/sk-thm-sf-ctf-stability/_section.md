+++
id = "sk-thm-sf-ctf-stability"
kind = "theorem"
title = "Stability of the constructible finite-Tor subcategories"
order = 2506
uses = ["sk-cor-sf-direct-image-ctf", "sk-def-sf-operations", "sk-def-sf-setting", "sk-prop-sf-comparison", "sk-thm-sf-direct-image-tor-amplitude", "sk-thm-sf-hom-ctf"]
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_leftDerivedUpperStar", "AlgebraicGeometry.Etale.constructibleFiniteTor_tensor", "AlgebraicGeometry.Etale.constructibleFiniteTor_rightDerivedLowerStar", "AlgebraicGeometry.Etale.constructibleFiniteTor_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.constructibleFiniteTor_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
For separated finite-type morphisms $f:X\to Y$ of finite-type $k$-schemes
($k=\overline{\mathbf F}_q$ as in [sk-def-sf-setting]; the dimension bounds
below are those of these schemes, which is what justifies the global
amplitude shifts) and complexes in the stated finite-Tor
domains, *each clause being a statement about the functor of
[sk-def-sf-operations] between the small categories written in it*:
(i) the functor $Lf^*:\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$ is defined;
(ii) $-\otimes^L_\Lambda-:\Dctf(Y,\Lambda)\times\Dctf(Y,\Lambda)\to \Dctf(Y,\Lambda)$ and
$\RHom_\Lambda(-,-):\Dctf(Y,\Lambda)^{\mathrm{op}}\times\Dctf(Y,\Lambda)\to \Dctf(Y,\Lambda)$ are defined, with Tor amplitudes
$[a,b]+[c,d]\mapsto[a+c,b+d]$ and, for $\dim Y\le m$,
$[a,b],[c,d]\mapsto[c-b-2m,d-a+2m]$, sharpened to $[c-b,d-a]$ when the first
argument is site-perfect;
(iii) $Rf_*:\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$ is defined;
(iv) $Rf_!:\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$ is defined;
(v) $Rf^!:\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$ is defined for every $f$,
with no admissibility hypothesis ([sk-def-sf-operations](vi),
[sk-prop-sf-rf-shriek-preservation]); (vi) $\mathbb D_X:\Dctf(X,\Lambda)\to \Dctf(X,\Lambda)$ is defined and is a contravariant anti-equivalence with
$\mathbb D_X\mathbb D_X\cong\mathrm{id}$; (vii) each of (i)–(vi) is compatible
with finite reduction and scalar extension, and (i)–(vi) with the pro-étale
realization.
