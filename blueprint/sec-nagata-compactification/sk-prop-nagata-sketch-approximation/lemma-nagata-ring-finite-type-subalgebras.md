+++
id = "lemma-nagata-ring-finite-type-subalgebras"
kind = "lemma"
title = "A ring is the filtered colimit of its finite-type $\\mathbf Z$-subalgebras"
order = 330
lean = ["CommRingCat.isColimitFgSubalgebraCocone"]
+++
For every ring $A$, its finitely generated $\mathbf Z$-subalgebras form a
directed system and the canonical map

$$
\varinjlim_{A_0\subseteq A,\;A_0/\mathbf Z\ \mathrm{finite\ type}}A_0
\longrightarrow A
$$

is an isomorphism. In particular every finite set of elements of $A$ is
contained in one such subalgebra.
