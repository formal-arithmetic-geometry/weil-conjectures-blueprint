+++
id = "lem-weil-pbc-constructible-stratification-intersection"
kind = "lemma"
title = "Common refinement of two stratifications with constructible strata"
uses = ["def-constructible-stratification", "def-weil-constructible-subset", "def-pc-fibre-product", "def-constructible-refines"]
refines = "proof/thm-constructible-serre"
tags = ["sheaf-dag", "stacks-03RZ"]
+++
Let $X$ be a scheme and let $(\iota_k\colon Z_k\to X)_{k<n}$ and $(\kappa_l\colon W_l\to X)_{l<m}$ be two stratifications of the scheme $X$ [def-constructible-stratification], with strata $T_k=\iota_k(Z_k)$ and $T'_l=\kappa_l(W_l)$, such that every $T_k$ and every $T'_l$ is a constructible subset of the underlying space of $X$ [def-weil-constructible-subset]. For every pair $(k,l)$ let $V_{k,l}=Z_k\times_XW_l$ [def-pc-fibre-product] and $\mu_{k,l}=\iota_k\circ\mathrm{pr}_1\colon V_{k,l}\to X$. Then $(\mu_{k,l}\colon V_{k,l}\to X)_{(k,l)\in\{0,\dots,n-1\}\times\{0,\dots,m-1\}}$ is a stratification of the scheme $X$ whose strata are the sets $\mu_{k,l}(V_{k,l})=T_k\cap T'_l$; every stratum $T_k\cap T'_l$ is a constructible subset of $X$; and this stratification refines both $(\iota_k)_k$ and $(\kappa_l)_l$ [def-constructible-refines] ($T_k\cap T'_l\subseteq T_k$ and $T_k\cap T'_l\subseteq T'_l$).
