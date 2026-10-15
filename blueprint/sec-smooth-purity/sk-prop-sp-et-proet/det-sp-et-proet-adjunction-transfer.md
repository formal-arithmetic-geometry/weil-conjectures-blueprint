+++
id = "det-sp-et-proet-adjunction-transfer"
kind = "lemma"
title = "Transfer of adjunctions from étale to pro-étale finite coefficients"
uses = ["thm-weil-pbc-site-comparison", "thm-sf-ambient-adjoint-class"]
+++
Let $A$ be a finite admissible ring and $f:X\to Y$ separated of finite type.
Write $\nu^*$ for the comparison functors, which restrict to equivalences
$\nu^*:\Dctf(T_{\mathrm{ét}},A)\xrightarrow{\sim}\Dctf(T,A)$ for $T=X,Y$, and let
$c_f:\nu_Y^*Rf^{\mathrm{ét}}_!\xrightarrow{\sim}Rf_!\nu_X^*$ be the compact-support
comparison on $\Dctf(X_{\mathrm{ét}},A)$. Suppose
$G:\Dctf(Y_{\mathrm{ét}},A)\to\Dctf(X_{\mathrm{ét}},A)$ is a right adjoint of
$Rf^{\mathrm{ét}}_!$ with counit $\varepsilon^{\mathrm{ét}}$. Then
$G^{\mathrm{pro}}=\nu_X^*\circ G\circ(\nu_Y^*)^{-1}$ is right adjoint to
$Rf_!$ on $\Dctf(-_{\mathrm{proét}},A)$, with counit
$\varepsilon_{\nu_Y^*N}=\nu_Y^*(\varepsilon^{\mathrm{ét}}_N)\circ c_f^{-1}$, and the
unique counit-preserving isomorphism identifies $G^{\mathrm{pro}}$ with the
restriction of the Brown adjoint $f^!$ of [sk-prop-sf-existence].
