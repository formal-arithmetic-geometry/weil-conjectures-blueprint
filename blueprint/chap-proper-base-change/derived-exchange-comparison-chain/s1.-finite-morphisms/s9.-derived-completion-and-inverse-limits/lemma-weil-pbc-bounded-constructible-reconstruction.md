+++
id = "lemma-weil-pbc-bounded-constructible-reconstruction"
kind = "lemma"
title = "Bounded constructibility survives reconstruction"
order = 840
uses = ["lemma-weil-pbc-adic-completion-reduction", "lemma-weil-pbc-constructible-adic-lim-one-zero", "lemma-weil-pbc-koszul-quotient-limit"]
+++
If the reduction tower $K_\bullet$ attached to $K$ is uniformly bounded
constructible, then
$\widehat K:=R\varprojlim_nK_n$ is intrinsically derived $I$-complete, has
finite reduction $\widehat K\otimes^LP_n\simeq K_n$, and retains the common
cohomological interval $[d_0,d_1]$ on the conservative weakly contractible
basis subordinate to the displayed stratification.

## Proof

Finite reduction is the preceding reduction lemma. Hence the quotient
completion of $\widehat K$ is the limit of the same tower and its completion
map is the identity under the product-cone model. The Koszul–quotient
comparison then makes its intrinsic Koszul unit an isomorphism. The common
cohomological bounds and the absence of a hidden degree from
$\varprojlim{}^1$ are exactly the conclusion of the preceding lemma.
Weakly contractible objects subordinate to a finite stratification form a
conservative basis, so these bounds detect the bounds of $\widehat K$.
