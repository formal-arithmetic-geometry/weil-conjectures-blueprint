+++
id = "prop-weil-pbc-separably-closed-extension"
kind = "theorem"
title = "Separably closed extension for proper curves"
order = 1723
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-algebraically-closed-extension", "thm-weil-pbc-universal-homeomorphism-invariance"]
tags = ["latex:proposition"]
+++
Let $k\subset k'$ be separably closed, let $C$ be proper of dimension at most
one over $k$, and let $F$ be torsion. The same canonical restriction map is an
isomorphism in every degree.

## Proof

Pass to compatible algebraic closures: the isomorphism of
[prop-weil-pbc-algebraically-closed-extension] holds for the two algebraically
closed extensions, and the two purely inseparable extensions identify the
sites by invariance under universal homeomorphisms, so the separably closed
case is obtained by composing the isomorphisms.
