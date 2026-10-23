+++
id = "def-weil-pbc-etale-sheaf-of-sets"
kind = "definition"
title = "Sheaves of sets on the small etale site"
uses = ["def-weil-pbc-etale-site", "def-pc-fibre-product"]
lean = ["CategoryTheory.Sheaf", "AlgebraicGeometry.Scheme.smallEtaleTopology"]
order = 1299
tags = ["mathlib", "stacks-00VM"]
+++
Let $T$ be a scheme and $T_{\Et}$ its small etale site [def-weil-pbc-etale-site] (objects the etale morphisms $W\to T$, morphisms the $T$-morphisms, coverings the jointly surjective families $\{W_i\to W\}_{i\in I}$ of etale morphisms; fibre products $W_i\times_WW_j$ are the scheme-theoretic fibre products [def-pc-fibre-product]). A *presheaf of sets* on $T_{\Et}$ is a contravariant functor $\mathcal F$ from $T_{\Et}$ to sets; for $g:W'\to W$ write $s\mapsto s|_{W'}=\mathcal F(g)(s)$. A presheaf of sets $\mathcal F$ is a *sheaf of sets* if for every object $W$ and every covering $\{g_i:W_i\to W\}_{i\in I}$ of $T_{\Et}$ the diagram $\mathcal F(W)\to\prod_{i}\mathcal F(W_i)\rightrightarrows\prod_{i,j}\mathcal F(W_i\times_WW_j)$, the first map $s\mapsto(s|_{W_i})_i$, the two others $(s_i)_i\mapsto(s_i|_{W_i\times_WW_j})_{i,j}$ and $(s_i)_i\mapsto(s_j|_{W_i\times_WW_j})_{i,j}$ (restriction along the first, resp. second projection), is an equalizer diagram of sets. Sheaves of sets on $T_{\Et}$, with natural transformations as morphisms, form the full subcategory $\Sh(T_{\Et})$ of the category of presheaves of sets.
