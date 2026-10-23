+++
id = "lem-weil-pbc-locally-constant-maps-gluing-exists"
kind = "lemma"
title = "Compatible locally constant maps admit a gluing"
lean = ["TopCat.locallyConstantMaps_gluing_exists"]
order = 1890
+++
Let $X$ be a topological space, $R$ a set, $(U_i)_{i\in I}$ a family of open subsets of $X$, and for each $i$ a locally constant map $s_i:U_i\to R$, such that $s_i$ and $s_j$ agree on $U_i\cap U_j$ for all $i,j$. Then there is a locally constant map $s:\bigcup_iU_i\to R$ with $s|_{U_i}=s_i$ for every $i$.
