+++
id = "fin4-thm-smooth-projective-curve-reduction"
kind = "theorem"
title = "Reduction to smooth projective curve families"
order = 5219
lean = ["AlgebraicGeometry.Etale.smoothProjectiveCurve_reduction"]
uses = ["sbc-def-coefficient-conventions", "def-sbc-smooth-morphisms", "def-sbc-normal-dominant-galois", "fin4-lem-domination-trick", "fin4-thm-finite-morphisms-constructible", "thm-fin-proper-case"]
+++
Assume that $P$ (the assertion of [fin4-lem-domination-trick]) holds for
every projective morphism $X\to S$ which is a smooth proper
[def-sbc-smooth-morphisms] curve family with geometrically connected
[def-sbc-normal-dominant-galois] fibres, for the constant torsion sheaves
$\underline{\mathbf Z/(l)}$ ($l$ a prime). Then $P$ holds for every
projective morphism all of whose fibres have dimension at most one, with the
constructible $\Lambda$-sheaves of [sbc-def-coefficient-conventions].

## Proof

The conclusion, including its bound for the actual geometric fibre
dimension, is the already proved proper theorem [thm-fin-proper-case]. A
projective morphism in the statement is proper. Thus the asserted
implication holds; its conclusion is now available without its preliminary
hypothesis.

The independent proof given earlier in this chapter obtains constructibility
by the projective-line and finite-cover reductions and then obtains the
bound from geometric fibres, so there is no circular use of this older
reduction node.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-direct-image, def:weil-pbc-constructible-complexes, cor:pqf-proper-quasifinite-finite, pqf-lem-locqf-fibre-discrete, thm:weil-pbc-universal-homeomorphism-invariance
