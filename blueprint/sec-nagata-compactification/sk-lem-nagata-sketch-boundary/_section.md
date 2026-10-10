+++
id = "sk-lem-nagata-sketch-boundary"
kind = "section"
title = "Separating boundary closures"
order = 244
uses = ["sk-lem-nagata-sketch-blowups"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_disjoint_closures"]
+++
*Lemma (sketch).*

Let $X$ be a qcqs scheme, let $V\subseteq X$ be a quasi-compact open, and
let $T_1,T_2\subseteq V$ be disjoint closed subsets whose complements in $V$
are quasi-compact (that is, constructible closed subsets of $V$). Then there
is a $V$-admissible blow-up $\pi\colon X'\to X$ such that the closures of
$\pi^{-1}(T_1)$ and $\pi^{-1}(T_2)$ in $X'$ are disjoint.

## Proof

Represent the two subsets by finite-type ideals on $V$, extend the
ideals to $X$, and apply the closed-boundary separation blow-up.
The strict-transform chart calculation separates their closures.
Disjointness persists under any further blow-up preserving $V$.
