+++
id = "pqf-lem-semicontinuity-fibre-dimension"
kind = "lemma"
title = "Upper semicontinuity of the fibre dimension"
order = 3211
lean = ["AlgebraicGeometry.isClosed_fiberDim_ge_of_isProper"]
+++
Let $f:X\to Y$ be a proper morphism of schemes. For every $d\geq0$ the set
of points $y\in Y$ such that the fibre $X_y$ has dimension at least $d$ is
closed in $Y$.

*Stacks Project, More on Morphisms, Lemma 37.30.5, [Tag
0D4I](https://stacks.math.columbia.edu/tag/0D4I).*

## Proof

This is the recorded classical input named in the statement, Stacks
Project, More on Morphisms, Lemma 37.30.5, [Tag
0D4I](https://stacks.math.columbia.edu/tag/0D4I) (Section 37.30, Dimension
of fibres): for a proper morphism the function $y\mapsto\dim X_y$ is upper
semi-continuous, so the locus of points whose fibre has dimension at least
a given bound is closed. No separate proof is given.

*Recorded classical input OBL-PQF-01.* The source records that the tag 02FZ
cited in earlier revisions is Morphisms of Schemes, Lemma 29.29.4, an
openness statement on $X$ for a locally finite type morphism, and is not
this input. Decomposition status: kept as a recorded input for now — its
proof is a reference-grade chain (generic flatness / Chevalley-type
constructibility arguments); it is used in the constructibility chapter.

Unresolved dependencies: def:weil-pbc-scheme-conventions
