+++
id = "lemma-weil-pbc-adic-reconstruction-compatibility"
kind = "lemma"
title = "Reconstruction preserves operators and base change"
order = 1835
uses = ["def-weil-pbc-adic-operator-base-change-datum", "lemma-weil-pbc-adic-completion-reduction"]
+++
An adic operator and base-change datum induces maps

$$
\widehat\phi=R\varprojlim_n\phi_n,\quad
\widehat\psi=R\varprojlim_n\psi_n,\quad
\widehat{Lg^*\phi}=R\varprojlim_nLg^*\phi_n,\quad
\widehat b=R\varprojlim_nb_n:
Lg^*_{\mathrm{comp}}K\longrightarrow\widehat L
$$

satisfying
$\widehat b\,\widehat{Lg^*\phi} =\widehat\psi\widehat b$. Under the canonical finite-reduction
isomorphisms, reduction modulo $I^n$ gives exactly
$\phi_n,\psi_n,b_n$. If $K$ and $L$ are intrinsically derived complete,
the reconstruction isomorphisms identify these with operators and a
base-change map on $K$ and $L$ themselves.

## Proof

Compatibility with transitions makes the three families maps of towers.
They therefore give maps between the two product-cone diagrams. The
levelwise equations give an equality on both product terms, hence on their
fibres, proving the displayed completed equation. The finite-reduction
lemma identifies projection to the $n$th factor with reduction modulo
$I^n$, so the reduced maps are precisely the named level maps. Finally,
conjugate by the functorial reconstruction isomorphisms for complete $K$
and $L$; the same equality survives conjugation.
