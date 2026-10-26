+++
id = "lem-weil-pbc-truncation-cohomology"
kind = "lemma"
title = "Cohomology of the canonical truncation"
uses = ["def-weil-abstract-derived-category", "def-sbc-standard-tstructure-derived-category"]
lean = ["CochainComplex.quasiIsoAt_ιTruncLE", "CochainComplex.exactAt_of_isLE", "DerivedCategory.truncation_triangle"]
order = 2005
tags = ["mathlib", "stacks-0118"]
+++
Let $\mathcal A$ be an abelian category, $K$ a cochain complex of $\mathcal A$ with cohomology objects $H^i(K)=\Ker(d^i)/\Im(d^{i-1})$ [def-weil-abstract-derived-category], and $n\in\mathbf Z$. Let $\tau_{\leq n}K$ be the canonical truncation, the subcomplex $\cdots\to K^{n-2}\to K^{n-1}\to\Ker(d^n_K)\to0\to0\to\cdots$ of $K$ [def-sbc-standard-tstructure-derived-category], and $c_n:\tau_{\leq n}K\to K$ the inclusion. Then $H^i(c_n):H^i(\tau_{\leq n}K)\to H^i(K)$ is an isomorphism for every $i\leq n$, and $H^i(\tau_{\leq n}K)=0$ for every $i>n$. Consequently, in the derived category $D(\mathcal A)$, the cohomology functors $H^i$ applied to the image of $c_n$ give the same statements; and if $K$ is bounded below, so is $\tau_{\leq n}K$.
