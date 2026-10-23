+++
id = "pqf-lem-affine-local-target"
kind = "lemma"
title = "Affineness is local on the target"
lean = ["AlgebraicGeometry.isAffineHom_tfae"]
order = 302
uses = ["pqf-def-affine-morphism"]
+++
A morphism of schemes $f:X\to S$ is
affine if and only if for every
affine open $V\subset S$ the preimage $f^{-1}(V)$ is affine, if and
only if there exists an affine open covering $S=\bigcup_jV_j$ such that
each $f^{-1}(V_j)$ is affine.
