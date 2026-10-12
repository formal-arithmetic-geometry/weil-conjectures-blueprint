+++
id = "lem-weil-pbc-conjugate-iso-unit-equation"
kind = "lemma"
title = "An isomorphism of right adjoints determines a unique isomorphism of left adjoints compatible with the units"
order = 1054
lean = ["CategoryTheory.unit_conjugateEquiv_symm"]
tags = ["sheaf-dag", "mathlib", "stacks-0B65"]
+++
Let $\mathcal C,\mathcal D$ be categories, $L_1\dashv R_1$ and $L_2\dashv R_2$ two adjunctions with $L_i:\mathcal C\to\mathcal D$, $R_i:\mathcal D\to\mathcal C$ and units $\eta_1:\mathrm{id}\to R_1L_1$, $\eta_2:\mathrm{id}\to R_2L_2$, and let $\delta:R_2\xrightarrow{\sim}R_1$ be a natural isomorphism. Then there is a unique natural transformation $c:L_1\to L_2$ such that $R_1(c_X)\circ\eta_{1,X}=\delta_{L_2X}\circ\eta_{2,X}:X\to R_1L_2X$ for every object $X$ of $\mathcal C$, and $c$ is a natural isomorphism. (In particular, for $R_1=R_2$ and $\delta=\mathrm{id}$: two left adjoints of one functor are isomorphic by a unique isomorphism carrying the one unit to the other.)
