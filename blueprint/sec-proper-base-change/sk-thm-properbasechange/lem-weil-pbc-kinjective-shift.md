+++
id = "lem-weil-pbc-kinjective-shift"
kind = "lemma"
title = "A shift of a K-injective complex is K-injective"
uses = ["def-sp-kinjective-bridge", "def-weil-abstract-derived-category"]
lean = ["CochainComplex.IsKInjective", "CochainComplex.isKInjective_shift_iff", "CochainComplex.quasiIso_shift_iff"]
order = 2018
tags = ["mathlib", "stacks-070H"]
+++
Let $\mathcal A$ be an abelian category and $I$ a cochain complex of $\mathcal A$ which is K-injective, i.e. $\operatorname{Hom}_{K(\mathcal A)}(M,I)=0$ in the homotopy category for every acyclic complex $M$ [def-sp-kinjective-bridge], [def-weil-abstract-derived-category]. For $n\in\mathbf Z$ let $I[n ]$ be the shifted complex, $(I[n ])^r=I^{r+n}$, $d_{I[n ]}=(-1)^nd_I$. Then $I[n ]$ is K-injective for every $n\in\mathbf Z$ (and conversely, $I$ is K-injective if $I[n ]$ is). Moreover, if $s:K\to I$ is a K-injective resolution (a quasi-isomorphism into a K-injective complex), then $s[n ]:K[n ]\to I[n ]$, $(s[n ])^r=s^{r+n}$, is a K-injective resolution of $K[n ]$.
