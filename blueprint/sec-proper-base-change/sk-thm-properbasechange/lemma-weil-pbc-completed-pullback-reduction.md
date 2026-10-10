+++
id = "lemma-weil-pbc-completed-pullback-reduction"
kind = "lemma"
title = "Reduction commutes with completed pullback"
order = 1262
uses = ["def-weil-pbc-completed-pullback", "def-weil-pbc-intrinsic-completion", "lem-weil-pbc-finite-reduction-reconstruction", "lemma-weil-pbc-adic-completion-reduction"]
+++
The object $Lg^*_{\mathrm{comp}}K$ of
[def-weil-pbc-completed-pullback] is derived $I$-complete, and for
every $n$ there is a functorial isomorphism

$$
 (Lg^*_{\mathrm{comp}}K)\otimes_A^LP_n
 \xrightarrow{\sim}Lg_n^*K_n,
$$

compatible with the transition maps and normalization cocycles.

## Proof

Completeness follows from the reconstruction of
[def-weil-pbc-intrinsic-completion] applied to the tower defining
[def-weil-pbc-completed-pullback]. Tensoring the defining derived
limit with $P_n$ and using the finite reduction of
[lem-weil-pbc-finite-reduction-reconstruction] gives the displayed
isomorphism, with the stated compatibilities inherited from the tower
structure.

Derived pullback commutes with derived tensor, so its defining tower is the
reduction tower of $Lg^*K$. Apply finite reduction of adic completion to
this object. Its level $n$ is
$Lg^*K\otimes^L_\Lambda P_n\simeq Lg^*(K\otimes^L_\Lambda P_n)=Lg^*K_n$.
