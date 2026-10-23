+++
id = "pqf-def-affine-morphism"
kind = "definition"
title = "Affine morphisms"
order = 11
lean = ["AlgebraicGeometry.IsAffineHom", "AlgebraicGeometry.isAffineHom_of_isAffine"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
A morphism of schemes $f:X\to S$ is *affine* if for every affine
open $V\subset S$ the preimage $f^{-1}(V)$ is affine.

Any morphism between affine schemes is affine, and a closed immersion is
affine.
