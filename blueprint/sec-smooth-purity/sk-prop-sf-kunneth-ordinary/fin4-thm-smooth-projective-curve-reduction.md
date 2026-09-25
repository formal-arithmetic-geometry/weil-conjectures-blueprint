+++
id = "fin4-thm-smooth-projective-curve-reduction"
kind = "theorem"
title = "Reduction to smooth projective curve families"
order = 1818
uses = ["cor-pqf-proper-quasifinite-finite", "def-sbc-normal-dominant-galois", "def-sbc-smooth-morphisms", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "fin4-lem-domination-trick", "fin4-thm-finite-morphisms-constructible", "pqf-lem-locqf-fibre-discrete", "sbc-def-coefficient-conventions", "thm-fin-proper-case", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Assume that $P$ (the assertion of
[fin4-lem-domination-trick]) holds for every projective morphism
$X\to S$ which is an smooth
proper curve family with
geometrically connected
fibres, for the constant torsion sheaves
$\underline{\mathbf Z/(l)}$ ($l$ a prime). Then $P$ holds for every
projective morphism all
of whose fibres have dimension at most one, with the constructible
$\Lambda$-sheaves of [sbc-def-coefficient-conventions] and the
direct image of [def-weil-pbc-direct-image].

## Proof

The conclusion, including its bound for the actual geometric
fibre dimension, is the already proved proper theorem
[thm-fin-proper-case]. A projective morphism in the statement
is proper. Thus the asserted implication holds; its conclusion is
now available without its preliminary hypothesis.
The independent proof above obtains constructibility by the
projective-line and finite-cover reductions and then obtains the
bound from geometric fibres, so there is no circular use of this
older reduction node.
