+++
id = "pqf-lem-affine-local-target"
kind = "lemma"
title = "Affineness is local on the target"
order = 3222
lean = ["AlgebraicGeometry.isAffineHom_iff_exists_affine_cover"]
uses = ["pqf-def-affine-morphism"]
+++
A morphism of schemes $f:X\to S$ is affine [pqf-def-affine-morphism] if and
only if for every affine open $V\subset S$ the preimage $f^{-1}(V)$ is
affine, if and only if there exists an affine open covering
$S=\bigcup_jV_j$ such that each $f^{-1}(V_j)$ is affine.

*Stacks Project, Morphisms of Schemes, Lemma 29.11.3, [Tag
01S8](https://stacks.math.columbia.edu/tag/01S8).*

## Proof

This is the recorded classical input named in the statement, Stacks
Project, Morphisms of Schemes, Lemma 29.11.3 ([Tag
01S8](https://stacks.math.columbia.edu/tag/01S8)): affineness of a morphism
is local on the target in the stated sense. No separate proof is given.

*Recorded classical input OBL-PQF-03.* Decomposition status: kept as a
recorded input; the proof needs the affineness criterion via sections (the
canonical map to $\operatorname{Spec}\Gamma$) and the reference chain of
loc. cit. — note in particular that pairwise intersections are affine on a
separated scheme, whereas quasi-separatedness alone only makes them
quasi-compact.
