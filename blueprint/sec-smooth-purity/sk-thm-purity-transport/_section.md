+++
id = "sk-thm-purity-transport"
kind = "theorem"
title = "Smooth purity for all admissible coefficients"
order = 2862
uses = ["sk-def-purity-conv", "sk-lem-sf-flat-model", "sk-prop-a1", "sk-prop-cohsm", "sk-thm-smooth-purity", "sk-prop-sf-existence", "sk-thm-existence", "sk-prop-sp-integral-adjunction", "sk-prop-sp-rational", "sk-thm-sp-qbar", "sk-prop-sp-unique-adjoint"]
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

Moreover, $K\mapsto f_\Lambda^*K(d)[2d]$ is a right adjoint of
$Rf_{!,\Lambda}:\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$, with counit normalized by
integration on the affine line, and $\gamma_{f,\Lambda}$ is the *unique*
isomorphism of functors $f_\Lambda^*(-)(d)[2d]\xrightarrow{\sim}f_\Lambda^!$ on
$\Dctf(Y,\Lambda)$ compatible with the counits of the two adjunctions.

For étale $f$ we have $d=0$, and the theorem says $f_\Lambda^!\simeq f_\Lambda^*$
for every admissible $\Lambda$. For a smooth curve $C$ with structure map
$a:C\to\operatorname{Spec}k$ it gives
$a_{\Zl}^!\mathbf Z_{\ell,\operatorname{Spec}k}\simeq\mathbf Z_{\ell,C}(1)[2]$, a
single sheaf in degree $-2$.
