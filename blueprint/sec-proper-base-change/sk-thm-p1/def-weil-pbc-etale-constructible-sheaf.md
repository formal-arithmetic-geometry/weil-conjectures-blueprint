+++
id = "def-weil-pbc-etale-constructible-sheaf"
kind = "definition"
title = "Constructible sheaf of modules on the small etale site"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-etale-sheaves", "def-constructible-stratification", "def-weil-constructible-subset", "def-weil-pbc-inverse-image", "def-constructible-locally-constant"]
tags = ["sheaf-dag", "stacks-095E"]
+++
Let $T$ be a scheme and $\Lambda$ a finite commutative ring, let $T_{\Et}$ be the small etale site of $T$ [def-weil-pbc-etale-site] and $\Lambda_T$ its constant sheaf of rings, and let $\mathcal F$ be a sheaf of $\Lambda_T$-modules on $T_{\Et}$ [def-weil-pbc-etale-sheaves]. The sheaf $\mathcal F$ is *constructible* if there is a stratification $(\iota_k\colon Z_k\to T)_{k<n}$ of the scheme $T$ [def-constructible-stratification] (a finite partition $T=\coprod_{k<n}T_k$ of the underlying space into pairwise disjoint locally closed subsets, a partition in the sense of Stacks 09XZ with no condition on closures of strata, together with immersions $\iota_k$ of schemes $Z_k$ with set-theoretic image $T_k$) such that
(a) every stratum $T_k$ is a constructible subset of the underlying space of $T$ [def-weil-constructible-subset], and
(b) for every $k$ the inverse image $\iota_k^{-1}\mathcal F$ [def-weil-pbc-inverse-image], a sheaf of $\Lambda_{Z_k}$-modules on $(Z_k)_{\Et}$, is *finite locally constant as a sheaf of $\Lambda$-modules* (Stacks 03RU): it is locally constant as a sheaf of $\Lambda$-modules [def-constructible-locally-constant] with finite values, i.e. there are an etale covering $\{U_i\to Z_k\}_{i\in I}$ and finite $\Lambda$-modules $M_i$ (finite as sets; $\Lambda$ being finite, equivalently finitely generated) such that $(\iota_k^{-1}\mathcal F)|_{U_i}\cong\underline{M_i}$, the constant sheaf of $\Lambda_{U_i}$-modules with value $M_i$, for every $i$.
The schemes $Z_k$ are part of the data; one may take $Z_k=T_k$ with its reduced induced structure (Stacks, paragraph before 03RW).
