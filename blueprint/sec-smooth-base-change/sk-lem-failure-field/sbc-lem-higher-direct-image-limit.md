+++
id = "sbc-lem-higher-direct-image-limit"
kind = "lemma"
title = "Higher direct images and limits of schemes"
order = 1389
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-scheme-conventions", "sbc-lem-higher-direct-image-presheaf"]
+++
Let $S$ be a scheme and let
$X=\varprojlim_{i\in I}X_i$ be a limit of a directed system of schemes
over $S$ with affine transition morphisms, and assume the structure
morphisms $g_i:X_i\to S$ and $g:X\to S$ are
quasi-compact and
quasi-separated. Let $(\mathcal F_i)$ be a system of abelian sheaves
on $(X_i,f_{i'i})$, with $f_i:X\to X_i$ the projections, and set
$\mathcal F=\varinjlim_if_i^{-1}\mathcal F_i$. Then

$$
\varinjlim_{i\in I}R^pg_{i,*}\mathcal F_i
\xrightarrow{\ \sim\ }R^pg_*\mathcal F
$$

for every $p\geq0$.
