+++
id = "sk-lem-nagata-sketch-elimination"
kind = "theorem"
title = "Elimination of indeterminacy"
order = 10
uses = ["sk-lem-nagata-sketch-blowups", "sk-def-nagata-admissible", "sk-lem-nagata-boundary-divisor"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap"]
tags = ["sketch"]
+++
Let $T$ be qcqs, let $U\subseteq T$ be quasi-compact open, and let $W\to T$
be separated and of finite type, with $W_U\to U$ an isomorphism. There is a
$U$-admissible blow-up $T'\to T$ ([sk-def-nagata-admissible]) whose strict
transform $W'\to T'$ is an open immersion. The modification can first be
chosen so that $U$ is schematically dense in $T'$.

This is Stacks 081S. Its main ingredient is flattening by blow-up
(Stacks 081R): if $W\to T$ is of finite type and quasi-separated and is flat
and locally of finite presentation over $U$, then its strict transform under
a suitable $U$-admissible blow-up is flat and of finite presentation. After
[sk-lem-nagata-boundary-divisor], this strict transform contains the inverse
image of $U$ schematically densely and is the identity there, so it is an
open immersion. Conrad's account of Deligne's proof (Conrad, *Deligne's notes
on Nagata compactifications*, Theorem 2.4) reaches the same conclusions
through partial sections ([sk-thm-nagata-sketch-conrad]).
