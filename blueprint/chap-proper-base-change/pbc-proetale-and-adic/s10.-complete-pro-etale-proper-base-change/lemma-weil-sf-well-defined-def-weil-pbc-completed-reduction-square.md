+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-completed-reduction-square"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-completed-reduction-square"
order = 1890
uses = ["def-weil-pbc-completed-reduction-square", "lemma-weil-pbc-completed-pullback-reduction", "lemma-weil-pbc-completed-tensor-reduction", "lemma-weil-pbc-direct-image-derived-completion", "lemma-weil-sf-well-defined-def-weil-pbc-completed-base-change-map", "lemma-weil-sf-well-defined-def-weil-pbc-level-map-arrows"]
+++
For $n\geq1$, $\sigma_n:S\otimes^LP_n\to A_n$ and
$\tau_n:T\otimes^LP_n\to C_n$ are isomorphisms, while

$$
(\alpha_n,\delta_n,\overline\xi_n)\in
\operatorname{Hom}(S\otimes^LP_n,B_n)\times
\operatorname{Hom}(T\otimes^LP_n,D_n)\times
\operatorname{Hom}(S\otimes^LP_n,T\otimes^LP_n).
$$

The first two components of this triple are isomorphisms. No commutativity
claim for the reduction square is part of this certificate.

## Proof

Finite reduction of completed pullback gives $\sigma_n$ with the stated
source and target. Direct-image completion gives
$\widehat{Rf'_*E}\xrightarrow{\sim}Rf'_*(\widehat E)=T$; tensoring its
inverse with $P_n$ and applying finite reduction of completed tensor gives
$\tau_n:T\otimes^LP_n\xrightarrow{\sim}C_n$.

The level-arrow certificate makes $h_n:A_n\to B_n$ and
$h'_n:C_n\to D_n$ isomorphisms. Hence
$\alpha_n=h_n\sigma_n$ and $\delta_n=h'_n\tau_n$ have the asserted types
and are invertible. Finally the completed-map certificate gives
$\operatorname{Ex}^{\mathrm{comp}}_{\square,K}:S\to T$, so derived tensor
with $1_{P_n}$ gives the asserted type of $\overline\xi_n$. The next lemma
contains the square's commutativity and its compatibility fields.
