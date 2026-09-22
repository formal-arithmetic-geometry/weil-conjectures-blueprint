+++
id = "pqf-lem-proper-basic"
kind = "lemma"
title = "Basic consequences of properness"
order = 3208
lean = ["AlgebraicGeometry.IsProper.isSeparated", "AlgebraicGeometry.IsProper.universallyClosed", "AlgebraicGeometry.IsProper.quasiCompact"]
+++
Let $f:X\to S$ be a proper morphism of schemes. Then $f$ is separated,
universally closed, of finite type, quasi-compact and quasi-separated. In
particular, if $S$ is affine then $X$ is separated and quasi-compact.

## Proof

The first three assertions are part of the definition of properness in the
scheme conventions; quasi-compactness is part of the finiteness condition
there, and quasi-separatedness follows from separatedness (the diagonal is
an affine closed immersion, hence quasi-compact). If $S$ is affine then $X$
is quasi-compact and separated because $f$ is quasi-compact and separated.

Unresolved dependencies: def:weil-pbc-scheme-conventions
