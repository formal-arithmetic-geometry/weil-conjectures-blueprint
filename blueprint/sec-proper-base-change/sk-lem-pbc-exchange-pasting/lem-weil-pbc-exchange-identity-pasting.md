+++
id = "lem-weil-pbc-exchange-identity-pasting"
kind = "lemma"
title = "Identity and pasting equations for exchange"
order = 1510
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "lemma-weil-pbc-derived-exchange-replacement"]
+++
The transformation $\Ex_{\square}$ of the derived exchange morphism
[def-weil-pbc-derived-exchange] is the identity for an identity
square, modulo the identity isomorphisms $\mathrm{id}^{-1}\cong\mathrm{id}$ of
the inverse images. For horizontally or vertically pasted commutative squares
(for instance cartesian squares [def-weil-pbc-cartesian-square]), the exchange morphism of the outer
rectangle equals the composite of the exchange morphisms of the two inner
squares after inserting the canonical associativity isomorphisms for inverse
and derived direct images.
