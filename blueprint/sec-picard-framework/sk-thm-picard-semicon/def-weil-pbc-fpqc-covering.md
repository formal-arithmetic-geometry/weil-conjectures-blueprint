+++
id = "def-weil-pbc-fpqc-covering"
kind = "definition"
title = "fpqc covering of a scheme"
uses = ["def-pc-scheme", "def-weil-flat-morphism"]
lean = ["AlgebraicGeometry.Scheme.fpqcPrecoverage"]
tags = ["sheaf-dag", "mathlib", "stacks-022B"]
+++
Let $T$ be a scheme [def-pc-scheme]. A family of morphisms of schemes $\{f_i:T_i\to T\}_{i\in I}$ is an *fpqc covering* of $T$ if every $f_i$ is flat [def-weil-flat-morphism] and for every affine open $V\subset T$ there are $n\ge0$, indices $i_1,\dots,i_n\in I$ and affine opens $V_j\subset T_{i_j}$ with $\bigcup_{j=1}^n f_{i_j}(V_j)=V$. (Then $T=\bigcup_i f_i(T_i)$, since $T$ is covered by affine opens.)
