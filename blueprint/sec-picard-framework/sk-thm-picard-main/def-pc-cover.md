+++
id = "def-pc-cover"
kind = "definition"
title = "Covers of a functor"
lean = ["AlgebraicGeometry.ZariskiCovers"]
order = 786
uses = ["def-pc-scheme", "def-pc-subfunctor"]
+++
Let $S$ be a scheme, let
$F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ be a functor and
let $(H_i)_{i\in I}$ be a family of
subfunctors of $F$. The family
*covers* $F$ if for every $S$-scheme $T$, every $\xi\in F(T)$ and every
point $t\in T$ there are an index $i\in I$ and an open neighbourhood
$U\subseteq T$ of $t$ with $\xi|_U\in H_i(U)$; equivalently, there are an
open covering $T=\bigcup_aU_a$ and indices $i_a\in I$ with
$\xi|_{U_a}\in H_{i_a}(U_a)$.
