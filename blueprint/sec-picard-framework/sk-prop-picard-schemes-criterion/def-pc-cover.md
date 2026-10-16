+++
id = "def-pc-cover"
kind = "definition"
title = "Covers of a functor"
lean = ["AlgebraicGeometry.ZariskiCovers"]
order = 786
uses = ["def-pc-scheme", "def-pc-subfunctor"]
+++
Let $F:(\mathit{Sch})^{\mathrm{op}}\to\textit{Sets}$ be a functor and
let $(H_i)_{i\in I}$ be a family of
subfunctors of $F$. The family
*covers* $F$ if for every $\xi\in F(T)$ there is an open covering
$T=\bigcup_{i\in I}U_i$ with $\xi|_{U_i}\in H_i(U_i)$.
