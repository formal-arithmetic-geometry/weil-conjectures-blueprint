+++
id = "prop-weil-pbc-finite-morphisms"
kind = "theorem"
title = "Finite morphisms satisfy proper base change"
order = 1560
uses = ["def-weil-pbc-property-detailed", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-exchange"]
tags = ["latex:proposition"]
+++
Every finite morphism $f$ satisfies $\mathrm{PBC}(f)$ in the sense of
[def-weil-pbc-property-detailed].

## Proof

Finite morphisms and all their base changes are finite, so
[lem-weil-pbc-finite-exchange] supplies the canonical exchange isomorphism for
every base change and every torsion sheaf, which is the definition of
$\mathrm{PBC}(f)$ by [def-weil-pbc-property-detailed].
