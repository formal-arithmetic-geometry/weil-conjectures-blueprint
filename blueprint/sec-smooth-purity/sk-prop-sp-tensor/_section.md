+++
id = "sk-prop-sp-tensor"
kind = "proposition"
title = "The tensor formula"
order = 1826
uses = ["sk-prop-cohsm", "sk-lem-sp-finite-existence", "sk-def-sp-dualizing"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and
$K\in\Dctf(Y_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$. The projection formula and the
counit $Rf_!\omega_f\to(\mathbf Z/\ell^n\mathbf Z)_Y$ give
$Rf_!(f^*K\otimes^{\mathbf L}\omega_f)\simeq K\otimes^{\mathbf L}Rf_!\omega_f\to K$, and
its adjoint is the *tensor map*, a natural transformation of functors
$\Dctf(Y_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)\to\Dctf(X_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$

$$
f^*K\otimes^{\mathbf L}_{(\mathbf Z/\ell^n\mathbf Z)_X}\omega_f\longrightarrow f^!K.
$$

**Proposition.** For $K\in\Dctf(Y_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$, the tensor map
is an isomorphism. On a chart $f|_U=p_d\circ e$ as in
[sk-lem-sp-finite-existence], $\omega_f|_U\simeq(\mathbf Z/\ell^n\mathbf Z)_U(d)[2d]$, so
$\omega_f[-2d]$ is a locally constant sheaf of free $\mathbf Z/\ell^n\mathbf Z$-modules of
rank one.
