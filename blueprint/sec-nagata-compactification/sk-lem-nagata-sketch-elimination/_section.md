+++
id = "sk-lem-nagata-sketch-elimination"
kind = "theorem"
title = "Elimination of indeterminacy"
order = 194
uses = ["sk-lem-nagata-sketch-blowups", "sk-def-nagata-admissible", "sk-lem-nagata-boundary-divisor", "thm-nagata-conrad-elimination"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap"]
tags = ["sketch"]
+++
Let $T$ be qcqs, let $U\subseteq T$ be quasi-compact open, and let $W\to T$
be separated and of finite type, with $W_U\to U$ an isomorphism. There is a
$U$-admissible blow-up $T'\to T$ ([sk-def-nagata-admissible]) whose strict
transform $W'\to T'$ is an open immersion.

This is Stacks 081S, proved here without flattening by blow-up. A first
$U$-admissible blow-up makes $U$ schematically dense
([sk-lem-nagata-boundary-divisor]). The inverse of $W_U\to U$ is a section
of $W\to T$ over $U$; by Conrad's account of Deligne's proof (Conrad,
*Deligne's notes on Nagata compactifications*, Theorem 2.4), which rests on
Zariski's Main Theorem, it extends after a further admissible blow-up to an
open containing the preimage of $U$, with closed graph
([thm-nagata-conrad-elimination]). The composite blow-up is $U$-admissible
([sk-lem-nagata-sketch-blowups]), and the closed graph, containing the graph
over $U$ schematically densely, is the strict transform. So the strict
transform is isomorphic to an open of $T'$.
