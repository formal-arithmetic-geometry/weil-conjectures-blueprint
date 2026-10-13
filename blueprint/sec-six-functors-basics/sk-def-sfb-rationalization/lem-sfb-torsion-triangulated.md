+++
id = "lem-sfb-torsion-triangulated"
kind = "lemma"
title = "Torsion objects form a triangulated subcategory"
order = 1632
uses = ["def-sfb-torsion-objects"]
lean = ["CategoryTheory.Rationalization.instIsTriangulatedTorsion"]
+++
Let $\mathcal T$ be a pretriangulated category that is linear over a commutative ring $R$,
with $R$-linear shift functors, and let $M\subseteq R$ be a submonoid. The $M$-torsion
objects [def-sfb-torsion-objects] form a triangulated subcategory: they contain $0$, are
stable under shifts, and in a distinguished triangle
$X_1\to X_2\to X_3\to X_1[1]$, if $m_1$ kills $X_1$ and $m_3$ kills $X_3$, then
$m_1m_3$ kills $X_2$.
