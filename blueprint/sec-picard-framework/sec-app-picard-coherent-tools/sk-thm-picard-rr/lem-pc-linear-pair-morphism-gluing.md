+++
id = "lem-pc-linear-pair-morphism-gluing"
kind = "lemma"
title = "Gluing of the morphism determined by two linear forms"
lean = ["AlgebraicGeometry.Proj.linearChartHom_compatible"]
order = 672
uses = ["def-pc-linear-pair-morphism", "def-pc-proj", "def-pc-scheme", "def-pc-standard-graded-algebra", "def-sc-p1-standard"]
+++
Let $S$ be a standard graded
$k$-algebra, and let $l_0,l_1\in S_1$ satisfy
$D_+(l_0)\cup D_+(l_1)=\operatorname{Proj}(S)$. Then the two affine
descriptions of [def-pc-linear-pair-morphism] agree on the overlap
$D_+(l_0)\cap D_+(l_1)$ and glue to a morphism
$\pi_{l_0,l_1}:\operatorname{Proj}(S)\to\mathbf P^1_k$.
