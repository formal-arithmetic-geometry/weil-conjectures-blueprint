+++
id = "lemma-weil-pbc-epsilon-direct-image-higher-sheaves"
kind = "lemma"
title = "Higher direct-image comparison on finite sheaves"
order = 822
uses = ["lemma-weil-pbc-epsilon-derived-unit", "lemma-weil-pbc-epsilon-direct-image-site-comparison"]
+++
Let $A$ be finite, let $f:X\to Y$ be quasi-compact and quasi-separated, and
let $F$ be a constructible $A$-module sheaf on $X_{\mathrm{et}}$. For every
$r\geq0$, the canonical map

$$
\epsilon_Y^{-1}R^rf_{\mathrm{et},*}F
\longrightarrow R^rf_{\mathrm{proet},*}\epsilon_X^{-1}F
$$

is an isomorphism.

## Proof

The assertion is Zariski local on $Y$, so take $Y$ affine and use the basis
$W=\varprojlim_iW_i$ from Lemma
[lemma-weil-pbc-epsilon-direct-image-site-comparison]. The left side at
$W$ is

$$
\varinjlim_iH^r_{\mathrm{et}}(X_i,F).
$$

For the right side, apply Lemma [lemma-weil-pbc-epsilon-derived-unit] on
$X_W$ to $g_{\mathrm{et}}^{-1}F$. It identifies its value at $W$ with

$$
H^r_{\mathrm{proet}}(X_W,\epsilon_{X_W}^{-1}g_{\mathrm{et}}^{-1}F)
=H^r_{\mathrm{et}}(X_W,g_{\mathrm{et}}^{-1}F).
$$

Because $f$ is quasi-compact and quasi-separated, $X_W$ is the inverse limit
of the $X_i$ with affine transition maps and etale cohomology is continuous
for this system. Hence

$$
\varinjlim_iH^r_{\mathrm{et}}(X_i,F)
\xrightarrow{\sim}H^r_{\mathrm{et}}(X_W,g_{\mathrm{et}}^{-1}F).
$$

The component description in the preceding lemma identifies this
isomorphism with the canonical comparison map. The basis evaluations are
conservative, proving the sheaf assertion.
