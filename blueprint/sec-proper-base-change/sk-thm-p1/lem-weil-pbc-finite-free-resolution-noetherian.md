+++
id = "lem-weil-pbc-finite-free-resolution-noetherian"
kind = "lemma"
title = "A finite module over a Noetherian ring has a resolution by finite free modules (Stacks 00LP)"
lean = ["Module.exists_finite_free_resolution"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00LP (lemma-resolution-by-finite-free, line 17411), part (2), with its proof (lines 17428--17436). Tag verified in tags/tags: 00LP,algebra-lemma-resolution-by-finite-free"
+++
Let $R$ be a Noetherian ring `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) and $M$ a finitely generated $R$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)). Then there exist integers $n_0,n_1,n_2,\ldots\ge0$ and $R$-linear maps forming an exact complex $$\cdots\to R^{\oplus n_2}\xrightarrow{d_2}R^{\oplus n_1}\xrightarrow{d_1}R^{\oplus n_0}\xrightarrow{\varepsilon}M\to0,$$ i.e. $\varepsilon$ is surjective, $\ker\varepsilon=\operatorname{im}d_1$ and $\ker d_i=\operatorname{im}d_{i+1}$ for all $i\ge1$; in particular it is a resolution of $M$ by finite free $R$-modules.
