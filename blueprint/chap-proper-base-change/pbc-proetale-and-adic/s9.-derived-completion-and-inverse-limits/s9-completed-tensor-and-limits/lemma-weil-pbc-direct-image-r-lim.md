+++
id = "lemma-weil-pbc-direct-image-r-lim"
kind = "lemma"
title = "Direct image commutes with sequential homotopy limits"
order = 1852
uses = ["def-weil-pbc-adic-derived-inverse-limit"]
+++
For an inverse tower $M_n$ on $X_{\mathrm{proet}}$,

$$
Rf_*R\varprojlim_nM_n\xrightarrow{\sim}
R\varprojlim_nRf_*M_n.
$$

## Proof

Use the product/equalizer model

$$
R\varprojlim M_n\longrightarrow\prod_nM_n
\xrightarrow{1-\mathrm{shift}}\prod_nM_n
$$

as a distinguished triangle. Since $Rf_*$ is a right adjoint, it commutes
with products. Applying it to the triangle gives the product/equalizer model
for the right-hand limit, and the identity maps on the two products give the
isomorphism of fibres.
