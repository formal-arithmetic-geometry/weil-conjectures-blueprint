+++
id = "lem-weil-pbc-lift-to-injective-unique-up-to-homotopy"
kind = "lemma"
title = "Lifts along a quasi-isomorphism into a bounded below complex of injectives are unique up to homotopy"
uses = ["def-sp-abelian", "def-sp-injective-resolutions", "def-weil-abstract-derived-category"]
lean = ["CochainComplex.homotopy_of_comp_quasiIso_of_injective"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] and let $K^\bullet$, $L^\bullet$, $I^\bullet$ be cochain complexes of $\mathcal A$ [def-weil-abstract-derived-category], where $I^\bullet$ is bounded below ($I^n=0$ for $n\ll0$) and every $I^n$ is an injective object [def-sp-injective-resolutions]. Let $\alpha:K^\bullet\to L^\bullet$ be a quasi-isomorphism and $\beta_1,\beta_2:L^\bullet\to I^\bullet$ morphisms of complexes such that $\beta_1\circ\alpha$ and $\beta_2\circ\alpha$ are chain-homotopic (for instance equal). Then $\beta_1$ and $\beta_2$ are chain-homotopic: there are morphisms $k^n:L^n\to I^{n-1}$ with $\beta_1^n-\beta_2^n=d_I^{n-1}k^n+k^{n+1}d_L^n$ for all $n$.
