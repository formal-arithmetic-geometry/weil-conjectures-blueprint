+++
id = "prop-weil-pbc-finite-extension-coherence"
kind = "theorem"
title = "Independence and coherence of the rational proper base change"
order = 2778
lean = ["AlgebraicGeometry.Proetale.exchange_finiteExtension_coherence"]
uses = ["thm-weil-pbc-finite-extension", "prop-weil-pbc-rational-transport", "cor-weil-pbc-constructible-complete"]
tags = ["latex:proposition"]
+++
The isomorphism of [thm-weil-pbc-finite-extension] is independent of an
integral lattice, and is natural and coherent for identities and pasted
squares.

## Proof

The isomorphism is the transport along [prop-weil-pbc-rational-transport] of
the integral isomorphism of [cor-weil-pbc-constructible-complete], whose
independence from the lattice and whose identity and pasting coherence are
inherited from the integral level.
