+++
id = "prop-weil-pbc-separably-closed-extension"
kind = "theorem"
title = "Separably closed extension for proper curves"
order = 1165
lean = ["AlgebraicGeometry.Etale.isIso_cohomologyPullback_of_isProper_dimLEOne_isSepClosed"]
uses = ["prop-weil-pbc-algebraically-closed-extension"]
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

Unresolved dependencies: def:weil-pbc-etale-sheaves, def:weil-pbc-scheme-conventions, thm:weil-pbc-universal-homeomorphism-invariance
