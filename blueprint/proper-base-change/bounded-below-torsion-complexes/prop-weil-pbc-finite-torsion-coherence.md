+++
id = "prop-weil-pbc-finite-torsion-coherence"
kind = "theorem"
title = "Coherence of the finite-torsion exchange"
order = 1189
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_naturality", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
uses = ["thm-weil-pbc-finite-torsion", "def-weil-pbc-derived-exchange"]
+++
The exchange morphism $\Ex_{\square,F}$ of [thm-weil-pbc-finite-torsion] is
natural in $F$, is the identity for identity squares, and satisfies horizontal
and vertical pasting after inserting the canonical associativity isomorphisms
for inverse and derived direct images.

## Proof

Naturality is built into the unit--pullback-constraint--counit construction of
[def-weil-pbc-derived-exchange], and the identity and pasting laws are the
coherence equations of the exchange morphism.

Unresolved dependencies: lem:weil-pbc-exchange-identity-pasting
