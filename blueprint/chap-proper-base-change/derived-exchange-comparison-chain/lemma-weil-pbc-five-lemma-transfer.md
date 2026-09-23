+++
id = "lemma-weil-pbc-five-lemma-transfer"
kind = "lemma"
title = "Five-lemma transfer for exchange"
order = 1438
uses = ["def-weil-pbc-derived-exchange", "lemma-weil-pbc-prime-factor-induction"]
+++
In a short exact sequence of torsion sheaves, if two of the three derived
exchange maps are isomorphisms, then the third is an isomorphism.

## Proof

Apply $g^{-1}Rf_*$ and $Rf'_*g'^{-1}$ to the short exact sequence and write
the natural long exact cohomology sequences. Naturality of the exchange map
gives a morphism between these sequences. In each degree the five-lemma
applies to the five adjacent terms, with the boundary maps identified by the
connecting-homomorphism construction from an injective resolution. Thus the
middle exchange map is an isomorphism in every degree.
