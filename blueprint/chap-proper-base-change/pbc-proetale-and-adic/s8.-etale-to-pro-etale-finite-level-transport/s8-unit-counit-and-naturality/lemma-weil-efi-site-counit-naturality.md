+++
id = "lemma-weil-efi-site-counit-naturality"
kind = "lemma"
title = "Naturality equation for the comparison counit"
order = 1795
uses = ["def-weil-pbc-epsilon-unit-counit", "lemma-weil-pbc-epsilon-counit-representative-descent-v1"]
+++
For $\beta:G\to G'$ on $X_{\mathrm{proet}}$,

$$
\beta\varepsilon^X_G
=\varepsilon^X_{G'}(\epsilon_X^{-1}\epsilon_{X,*}\beta).
$$

## Proof

On a representative $(W\xrightarrow a\iota_XU,s)$, each route gives
$\beta_W(G(a)(s))=G'(a)(\beta_{\iota_XU}(s))$. The representative-descent
lemma carries this equality through sheafification.
