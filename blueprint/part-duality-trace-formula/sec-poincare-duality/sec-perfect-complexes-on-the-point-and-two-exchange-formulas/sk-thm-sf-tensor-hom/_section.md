+++
id = "sk-thm-sf-tensor-hom"
kind = "lemma"
title = "Internal adjunction and two exchange formulas"
order = 505
uses = ["sk-def-ops", "sk-prop-cohsm", "sk-prop-sf-open-closed-triangle", "sk-prop-sf-comparison", "sk-prop-sf-existence", "sk-rem-sf-pf-done", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-proetale", "sk-thm-sbc-coefficients"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be a morphism, $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and
$L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. The maps built from the adjunctions
$Rf_!\dashv f^!$, $f^*\dashv Rf_*$, tensor–Hom adjunction and
the projection formula are isomorphisms

$$
\begin{aligned}
\cHom_Y(Rf_!K,L)&\simeq
Rf_*\cHom_X(K,f^!L),\\
\mathbb D_YRf_!K&\simeq Rf_*\mathbb D_XK,
\\
f^!\mathbb D_YL&\simeq\mathbb D_Xf^*L.
\end{aligned}
\tag{11.1, 11.2, 11.3}
$$

These isomorphisms preserve evaluation. In particular, for proper
$f$, the two applications of (11.2) identify
$Rf_*\delta_K$ with $\delta_{Rf_*K}$.

*Complement.* Here $f$ is a separated finite-type morphism of finite-type
$k$-schemes and $f^!=Rf^!$ is the constructible exceptional adjoint of
[det-def-sf-operations] (vi); no admissibility datum is assumed. The
isomorphism (1) is natural in $K$ and $L$ and compatible with finite
reduction, scalar extension and shifts.
