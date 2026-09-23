+++
id = "lemma-weil-efi-site-adjunction-hom-left-inverse"
kind = "lemma"
title = "Left inverse equation for the comparison Hom maps"
order = 1769
uses = ["def-weil-efi-site-adjunction-hom-backward", "def-weil-efi-site-adjunction-hom-forward"]
+++
For every $\alpha:\epsilon_X^{-1}F\to G$,

$$
\Psi(\Phi(\alpha))=\alpha.
$$

## Proof

On a representative $(W\xrightarrow a\iota_XU,s)$, the left side is
$G(a)(\alpha_{\iota_XU}[(1,s)])$. Naturality of $\alpha$ identifies this
with $\alpha_W[(a,s)]$. Representatives are locally exhaustive after
sheafification, so the sheaf maps agree.
