+++
id = "prop-weil-pbc-finite-morphisms"
kind = "theorem"
title = "Finite morphisms satisfy proper base change"
order = 1074
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
uses = ["lem-weil-pbc-finite-exchange", "def-weil-pbc-property"]
+++
Every finite morphism $f$ satisfies $\mathrm{PBC}(f)$ in the sense of
[def-weil-pbc-property].

## Proof

Finite morphisms and all their base changes are finite, so
[lem-weil-pbc-finite-exchange] supplies the canonical exchange isomorphism for
every base change and every torsion sheaf, which is the definition of
$\mathrm{PBC}(f)$ by [def-weil-pbc-property].

Unresolved dependencies: def:weil-pbc-scheme-conventions
