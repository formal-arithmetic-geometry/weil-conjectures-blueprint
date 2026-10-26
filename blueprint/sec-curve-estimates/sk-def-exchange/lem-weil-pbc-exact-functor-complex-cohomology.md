+++
id = "lem-weil-pbc-exact-functor-complex-cohomology"
kind = "lemma"
title = "An exact functor commutes with cohomology of cochain complexes"
uses = ["def-sp-abelian", "def-weil-abstract-derived-category"]
lean = ["CategoryTheory.Functor.mapHomologicalComplexHomologyIso"]
order = 1299
tags = ["mathlib", "stacks-010N"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories [def-sp-abelian] and $F:\mathcal A\to\mathcal B$ an exact functor (additive, preserving finite limits and finite colimits). For a cochain complex $K=(K^r,d^r)$ of $\mathcal A$ let $F(K)=(F(K^r),F(d^r))$ be the complex obtained by applying $F$ termwise, and let $H^r(K)=\ker d^r/\operatorname{im}d^{r-1}$ be its $r$-th cohomology object [def-weil-abstract-derived-category]. Then for every $r\in\mathbf Z$ there is an isomorphism $c^r_K:H^r(F(K))\xrightarrow{\sim}F(H^r(K))$, natural in the complex $K$ (i.e. an isomorphism of functors $H^r\circ F\cong F\circ H^r$ from cochain complexes of $\mathcal A$ to $\mathcal B$); $c^r_K$ is induced by the identifications $\ker F(d^r)=F(\ker d^r)$ and $\operatorname{im}F(d^{r-1})=F(\operatorname{im}d^{r-1})$ as subobjects of $F(K^r)$, so it is compatible with the inclusions of cycles and the projections onto cohomology.
