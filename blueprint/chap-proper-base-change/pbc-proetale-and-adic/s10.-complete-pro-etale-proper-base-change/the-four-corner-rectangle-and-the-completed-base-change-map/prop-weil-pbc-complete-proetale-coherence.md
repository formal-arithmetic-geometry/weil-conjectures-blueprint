+++
id = "prop-weil-pbc-complete-proetale-coherence"
kind = "theorem"
title = "Coherence of the complete pro-etale exchange"
order = 1909
uses = ["def-weil-pbc-completed-base-change-map-detailed", "thm-weil-pbc-complete-proetale", "thm-weil-pbc-finite-level-proetale"]
tags = ["latex:proposition"]
+++
The exchange morphism $\Ex^{\mathrm{comp}}_{\square,K}$ of
[thm-weil-pbc-complete-proetale] is natural in $K$ and coherent for
identities and pasted squares.

*Source note:* no Stacks Project entry states this coherence: Theorem
61.30.1 ([Tag 09C9](https://stacks.math.columbia.edu/tag/09C9)) supplies the
isomorphism and states no naturality or pasting for it, the base change map
itself being the canonical map of Remark 21.19.3 ([Tag
07A7](https://stacks.math.columbia.edu/tag/07A7)), whose only recorded
coherence is its commutativity with the projection formula in Remark 21.50.2
([Tag 0E48](https://stacks.math.columbia.edu/tag/0E48)). The blueprint adds
both naturality in $K$ and coherence for identities and pasted squares, over
the tower-level form of [thm-weil-pbc-complete-proetale].

## Proof

The naturality and the identity and pasting coherence are those of the
finite-level maps of [def-weil-pbc-completed-base-change-map-detailed] and of
their derived limits, each being the finite-level coherence of
[thm-weil-pbc-finite-level-proetale].
