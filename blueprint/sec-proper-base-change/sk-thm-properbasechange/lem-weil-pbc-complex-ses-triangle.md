+++
id = "lem-weil-pbc-complex-ses-triangle"
kind = "lemma"
title = "A short exact sequence of complexes gives a distinguished triangle in D(A), functorially"
uses = ["def-weil-abstract-derived-category", "def-weil-triangulated-category"]
lean = ["DerivedCategory.triangleOfSES_distinguished"]
tags = ["sheaf-dag", "mathlib", "stacks-0152"]
+++
Let $\mathcal A$ be an abelian category with derived category $D(\mathcal A)$ and localization functor $Q$ from cochain complexes [def-weil-abstract-derived-category], a triangulated category [def-weil-triangulated-category]. For every short exact sequence of cochain complexes $0\to X_1\xrightarrow{f}X_2\xrightarrow{g}X_3\to0$ (degreewise short exact) there is a morphism $\delta:X_3\to X_1[1 ]$ in $D(\mathcal A)$ such that $X_1\xrightarrow{Q(f)}X_2\xrightarrow{Q(g)}X_3\xrightarrow{\delta}X_1[1 ]$ is a distinguished triangle of $D(\mathcal A)$; and $\delta$ is natural: for a morphism $(u_1,u_2,u_3)$ of short exact sequences of complexes, $(Q(u_1),Q(u_2),Q(u_3))$ is a morphism of the corresponding triangles, i.e. $Q(u_1)[1 ]\circ\delta=\delta'\circ Q(u_3)$.
