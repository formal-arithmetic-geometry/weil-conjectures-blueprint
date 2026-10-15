+++
id = "sk-thm-purity-transport"
kind = "theorem"
title = "Smooth purity for all admissible coefficients"
order = 1810
uses = ["sk-def-purity-conv", "sk-lem-sf-flat-model", "sk-prop-a1", "sk-prop-cohsm", "sk-thm-smooth-purity", "sk-prop-sf-existence"]
lean = ["AlgebraicGeometry.Etale.derivedCompleteIntegral_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $\Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\Qlb\}$ be any admissible coefficient
ring and let $f:X\to Y$ be smooth of pure relative dimension $d$. There is an
isomorphism of functors $\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$, given at
$K\in\Dctf(Y,\Lambda)$ by a canonical isomorphism in $\Dctf(X,\Lambda)$

$$
\gamma_{f,\Lambda}(K):\ f_\Lambda^*K(d)[2d]\xrightarrow{\ \sim\ }f_\Lambda^!K.
$$

Here $f^!_\Lambda$ is the restriction of the right adjoint from
[sk-prop-sf-existence]. The isomorphism is compatible with change of
coefficients, base change and composition, with the normalization given by
integration on the affine line.

For étale $f$ we have $d=0$, and the theorem says $f_\Lambda^!\simeq f_\Lambda^*$
for every admissible $\Lambda$. For a smooth curve $C$ with structure map
$a:C\to\operatorname{Spec}k$ it gives
$a_{\Zl}^!\mathbf Z_{\ell,\operatorname{Spec}k}\simeq\mathbf Z_{\ell,C}(1)[2]$, a
single sheaf in degree $-2$.
