+++
id = "sk-prop-sp-orientation"
kind = "proposition"
title = "The relative dualizing complex"
order = 1817
uses = ["sk-def-sp-dualizing", "sk-prop-cohsm", "sk-thm-dnc", "sk-prop-an", "sk-lem-diag-reg"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. There is a
canonical isomorphism in $\Dctf(X_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$

$$
\omega_{f}\xrightarrow{\ \sim\ }(\mathbf Z/\ell^n\mathbf Z)_{X}(d)[2d],
$$

the *orientation* of $f$, where $\omega_f=f^!(\mathbf Z/\ell^n\mathbf Z)_Y$ is
the relative dualizing complex of [sk-def-sp-dualizing].

Here $p_1,p_2:X\times_YX\to X$ are the projections and
$\Delta:X\to X\times_YX$ is the diagonal. Since $f$ is separated, $\Delta$ is a
closed immersion, and it is a section of the smooth morphism $p_1$. Its
conormal sheaf is $\Omega^1_{X/Y}$, so its normal bundle is the relative
tangent bundle $T_{X/Y}$; $\pi:T_{X/Y}\to X$ denotes its projection and
$z:X\to T_{X/Y}$ its zero section.
