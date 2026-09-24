+++
id = "thm-weil-pbc-etale-cohomology-continuity"
kind = "theorem"
title = "Etale cohomology continuity"
order = 1262
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-finite-hypercover-descent", "lem-weil-pbc-hypercover-refinement", "thm-weil-pbc-hypercover-cohomology"]
+++
Let $(X_i)_{i\in I}$ be a cofiltered inverse system of quasi-compact
quasi-separated schemes [def-weil-pbc-scheme-conventions] with affine
transition maps and limit $X$. Let $F_i$ be a torsion sheaf
[def-weil-pbc-etale-sheaves] on $X_i$, and write $F_j$ and $F$ for its
pullbacks to later stages and to $X$. Then

$$
 \varinjlim_{j\geq i}H^q(X_j,F_j)
 \xrightarrow{\sim}H^q(X,F)
 \qquad(q\geq0).
$$

## Proof

Let a class in $H^q(X,F)$ be given. By
[thm-weil-pbc-hypercover-cohomology], it is represented by a cocycle in
$C^q(U,F)$ on a hypercover finite in each degree. Descend the truncation
through degree $q+1$ using [lem-weil-pbc-finite-hypercover-descent]. By
[lem-weil-pbc-etale-section-continuity], its cocycle descends to a section at
a later stage, and the equation $\delta z=0$ holds at a further stage. That
cocycle represents a class in $H^q(X_j,F_j)$. This proves surjectivity of the
comparison.

For injectivity, represent a stagewise class by a hypercover cocycle, again
using [thm-weil-pbc-hypercover-cohomology]. If its pullback vanishes on $X$,
that theorem and [lem-weil-pbc-hypercover-refinement] give a refinement of
the pulled-back hypercover on which the cocycle is a boundary. Descend the
truncation of the refinement, its map to the original hypercover, its
primitive, and the boundary equation, using the same two descent lemmas. The
class is then zero at a later stage. For degree zero, replace the primitive
by the assertion that the section is zero; section continuity applies
directly. All the maps are pullbacks of sections, so the isomorphism is the
canonical restriction map in the statement and is natural in the sheaf and in
the inverse system.
