+++
id = "lem-weil-pbc-finite-open-cover-degree-sum"
kind = "lemma"
title = "A scheme over a field covered by finitely many finite open pieces is finite, of degree at most the sum"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.finite_open_cover_degree_sum"]
order = 1891
+++
Let $k$ be a field, let $T$ be a scheme [def-pc-scheme] with a morphism $t:T\to\operatorname{Spec}k$, and let $T=W_1\cup\dots\cup W_m$ ($m\ge0$) be a covering of $T$ by finitely many open subschemes. Suppose that for each $i$ the scheme $W_i$, over $k$ through $t|_{W_i}$, is finite over $k$ (so $W_i$ is affine and $\Gamma(W_i,\mathcal O_{W_i})$ is a finite-dimensional $k$-algebra) with $\dim_k\Gamma(W_i,\mathcal O_{W_i})\le n_i$ for an integer $n_i\ge0$. Then $T$ is finite over $k$ and $\dim_k\Gamma(T,\mathcal O_T)\le n_1+\dots+n_m$.
