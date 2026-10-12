+++
id = "lem-pc-cech-resolution"
kind = "lemma"
title = "The Cech resolution and derived direct image"
order = 676
uses = ["def-pc-derived-direct-image", "def-pc-morphism-conventions", "def-pc-scheme", "lem-pc-affine-morphism-hi", "lem-pc-affine-vanishing"]
+++
Let $S=\operatorname{Spec}(A)$, let $f:X\to S$ be a separated,
quasi-compact morphism, and choose a finite affine open cover
$X=\bigcup_{i=1}^t U_i$. For a quasi-coherent $\mathcal O_X$-module
$\mathcal F$, write $U_J=\bigcap_{j\in J}U_j$ and $j_J:U_J\to X$.
The augmented alternating Cech complex of sheaves

$$
0\longrightarrow\mathcal F\longrightarrow
\prod_i j_{i,*}(\mathcal F|_{U_i})\longrightarrow
\prod_{i<j}j_{ij,*}(\mathcal F|_{U_{ij}})\longrightarrow\cdots
$$

is exact. Its non-augmented terms are $f_*$-acyclic, so applying
$f_*$ to it computes $Rf_*\mathcal F$.
