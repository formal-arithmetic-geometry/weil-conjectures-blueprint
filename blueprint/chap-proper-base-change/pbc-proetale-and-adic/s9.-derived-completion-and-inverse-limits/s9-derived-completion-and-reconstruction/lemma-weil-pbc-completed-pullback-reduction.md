+++
id = "lemma-weil-pbc-completed-pullback-reduction"
kind = "lemma"
title = "Reduction commutes with completed pullback"
order = 1846
uses = ["def-weil-pbc-completed-pullback", "lemma-weil-pbc-adic-completion-reduction"]
+++
For every $n$,

$$
(Lg^*_{\mathrm{comp}}K)\otimes^L_\Lambda\Lambda/I^n
\xrightarrow{\sim}Lg^*K_n.
$$

## Proof

Derived pullback commutes with derived tensor, so its defining tower is the
reduction tower of $Lg^*K$. Apply finite reduction of adic completion to
this object. Its level $n$ is
$Lg^*K\otimes^L_\Lambda P_n\simeq Lg^*(K\otimes^L_\Lambda P_n)=Lg^*K_n$.
