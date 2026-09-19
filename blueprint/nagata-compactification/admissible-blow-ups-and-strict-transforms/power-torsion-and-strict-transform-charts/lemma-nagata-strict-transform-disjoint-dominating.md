+++
id = "lemma-nagata-strict-transform-disjoint-dominating"
kind = "lemma"
title = "Disjoint strict transforms stay disjoint"
order = 344
uses = ["lemma-nagata-strict-transform-dominating"]
+++
**Status.** Bypassed by the formalized route: composition and domination of
admissible blow-ups are handled by
`AlgebraicGeometry.IsAdmissible.exists_comp`, and the disjointness
that is actually used is
`AlgebraicGeometry.disjoint_range_strictTransformMap_of_disjoint`.

Let $Z_1,Z_2\to X$ be morphisms and let $X''\to X'\to X$ be blow-ups
which are isomorphisms over the same open $U\subseteq X$. If the strict
transforms of $Z_1$ and $Z_2$ in $X'$ are disjoint, their strict transforms
after the further dominating blow-up $X''\to X'$ are disjoint.

## Proof

Each new strict transform is contained in the inverse image of the
corresponding old strict transform. Inverse images of disjoint closed
subschemes are disjoint.
