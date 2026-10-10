+++
id = "lem-zl-composition-weight-bound"
kind = "lemma"
title = "Composition preserves the direct-image weight bound"
order = 2821
lean = ["AlgebraicGeometry.HasDirectImageWeightBound.comp"]
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-weil-pbc-qbar-category", "def-weil-punctual-weights", "lem-a1-mixed-direct-summand", "lem-zl-shriek-composition", "lemma-weil-pbc-hypercohomology-convergence"]
+++
Let $h:X_0\to Z_0$ and $g:Z_0\to Y_0$ be separated finite-type
morphisms of $k_0$-schemes, where $Z_0$ and $Y_0$ are quasi-separated
$k_0$-schemes of finite type. Suppose the
direct-image weight assertion holds for $h$ and for $g$: for every
real $v$, every $\iota$-mixed Weil sheaf of weights at most $v$ on the
source has its $i$th higher direct image with compact support
$\iota$-mixed of weights at most $v+i$, for every $i$. Then the same
assertion holds for $gh$: if $\mathcal F$ is an $\iota$-mixed Weil
sheaf on $X_0$ of weights at most $w$, then $R^n(gh)_!\mathcal F$ is
$\iota$-mixed of weights at most $w+n$ for every $n$.
