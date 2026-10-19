+++
id = "sk-thm-sf-tensor-hom"
kind = "lemma"
title = "Internal adjunction and the formal exchanges"
order = 2386
uses = ["sk-def-ops", "sk-def-sf-exchanges", "sk-def-sf-operations", "sk-lem-sf-mate", "sk-prop-sf-comparison", "sk-prop-sf-existence", "sk-rem-sf-pf-done", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_derivedHom_rightDerivedLowerShriek"]
tags = ["sketch"]
+++
Let $\Lambda$ be an admissible coefficient ring, and let $\omega$, $\mathbb D$
and $\delta$ be as in [sk-def-ops].

Let $f:X\to Y$ be a morphism, $K\in\Dctf(X,\Lambda)$ and
$L\in\Dctf(Y,\Lambda)$. The maps built from the adjunctions
$Rf_!\dashv f^!$, $f^*\dashv Rf_*$, tensor–Hom adjunction and
the projection formula are isomorphisms in
$D(Y_{\mathrm{pro\acute et}},\Lambda)$ (the first two) and in
$D(X_{\mathrm{pro\acute et}},\Lambda)$ (the third)

$$
 \cHom_Y(Rf_!K,L)\simeq
 Rf_*\cHom_X(K,f^!L),\tag{1}
$$

$$
 \mathbb D_YRf_!K\simeq Rf_*\mathbb D_XK,\tag{2}
$$

$$
 f^!\mathbb D_YL\simeq\mathbb D_Xf^*L.\tag{3}
$$

These isomorphisms preserve evaluation. In particular, for proper
$f$, the two applications of (2) identify
$Rf_*\delta_K$ with $\delta_{Rf_*K}$.

*Complement.* Here $f$ is a separated finite-type morphism of finite-type
$k$-schemes and $f^!=Rf^!$ is the constructible exceptional adjoint of
[sk-def-sf-operations] (vi); no admissibility datum is assumed. The
isomorphism (1) is natural in $K$ and $L$ and compatible with finite
reduction, scalar extension and shifts.
