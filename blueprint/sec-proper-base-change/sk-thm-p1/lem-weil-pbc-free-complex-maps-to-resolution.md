+++
id = "lem-weil-pbc-free-complex-maps-to-resolution"
kind = "lemma"
title = "A complex of free modules over M maps to any resolution of N over a map M -> N"
lean = ["free_complex_maps_to_resolution"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00LS (lemma-compare-resolutions, line 17500), part (1), with its proof (lines 17525--17535). Tag verified in tags/tags: 00LS,algebra-lemma-compare-resolutions"
+++
Let $R$ be a commutative ring and $\varphi:M\to N$ a homomorphism of $R$-modules. Let $\cdots\to N_2\xrightarrow{\partial_2}N_1\xrightarrow{\partial_1}N_0\xrightarrow{\eta}N\to0$ be an exact sequence of $R$-modules `CategoryTheory.ShortComplex.Exact` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/ShortComplex/Exact.lean)) (a resolution of $N$; finitely many $N_i$ may be nonzero). Let $\cdots\to F_2\xrightarrow{\delta_2}F_1\xrightarrow{\delta_1}F_0\xrightarrow{\pi}M$ be $R$-linear maps with $\delta_{i-1}\circ\delta_i=0$ for $i\ge2$ and $\pi\circ\delta_1=0$ (a complex over $M$, not necessarily exact), every $F_i$ being a free $R$-module `Module.Free` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/FreeModule/Basic.lean)). Then there are $R$-linear maps $\alpha_i:F_i\to N_i$ ($i\ge0$) with $\eta\circ\alpha_0=\varphi\circ\pi$ and $\partial_i\circ\alpha_i=\alpha_{i-1}\circ\delta_i$ for all $i\ge1$.
