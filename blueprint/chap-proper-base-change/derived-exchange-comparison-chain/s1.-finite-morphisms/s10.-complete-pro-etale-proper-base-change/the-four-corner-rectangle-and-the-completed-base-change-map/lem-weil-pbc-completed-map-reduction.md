+++
id = "lem-weil-pbc-completed-map-reduction"
kind = "lemma"
title = "Finite reduction of the completed map"
order = 1902
uses = ["def-weil-pbc-completed-base-change-map-detailed", "lem-weil-pbc-completed-pullback-reduction", "lem-weil-pbc-finite-reduction-reconstruction", "lem-weil-pbc-rectangle-derived-limit"]
+++
For every $n$, reduction of $\Ex^{\mathrm{comp}}_{\square,K}$ of
[def-weil-pbc-completed-base-change-map-detailed] modulo $I^n$, conjugated by
the canonical reduction isomorphisms, is exactly
$$
 \Ex_{\square,K_n}:Lg_n^*Rf_*K_n
 \xrightarrow{\sim}Rf'_*Lg_n'^*K_n.
$$
These reduction squares commute with $n+1\to n$ and with compatible
endomorphisms.

*Source note:* the reduction of the completed pullback is the formula
$Lf^*_{comp}M=\Rlim Lf^*(M\otimes^L_\Lambda\underline{\Lambda/I^n})$ of
Stacks Project, Lemma 61.20.2 ([Tag
099N](https://stacks.math.columbia.edu/tag/099N)), whose $n$-th level is
$Lf_n^*$ of the $n$-th level; Stacks states the formula for the completed
pullback of one object of $D(\mathcal C,\Lambda)$, whereas the displayed
statement reduces the completed base-change exchange map of
[def-weil-pbc-completed-base-change-map-detailed], which the verified entries
do not construct, and the blueprint adds that reduction together with its
compatibility with the transitions and with compatible endomorphisms.

## Proof

Tensoring the defining composite of
[def-weil-pbc-completed-base-change-map-detailed] with $P_n$ and using the
finite-reduction identifications of the reconstruction lemma and of the
completed-pullback reduction collapses it to the $n$-th component of the
rectangle equality of [lem-weil-pbc-rectangle-derived-limit], which is the
finite-level exchange isomorphism; the compatibilities with the transitions
follow from the tower structures.
