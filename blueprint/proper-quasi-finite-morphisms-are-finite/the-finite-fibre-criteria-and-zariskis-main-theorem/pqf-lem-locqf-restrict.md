+++
id = "pqf-lem-locqf-restrict"
kind = "lemma"
title = "Restriction of locally quasi-finite morphisms"
order = 3244
lean = ["AlgebraicGeometry.LocallyQuasiFinite.restrict"]
uses = ["pqf-def-quasifinite"]
+++
If $f:X\to S$ is locally quasi-finite, then for any open subschemes
$U\subset X$, $V\subset S$ with $f(U)\subset V$ the restriction
$f|_U:U\to V$ is locally quasi-finite.

## Proof

Quasi-finiteness at a point is a property of the local situation (affine
neighbourhoods inside the source and target), by [pqf-def-quasifinite];
restricting to opens does not change the local ring situation at a point of
$U$, so the property is preserved.
