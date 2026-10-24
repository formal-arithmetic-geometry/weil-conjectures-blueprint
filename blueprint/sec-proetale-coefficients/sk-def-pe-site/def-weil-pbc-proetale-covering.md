+++
id = "def-weil-pbc-proetale-covering"
kind = "definition"
title = "Pro-etale covering of a scheme"
uses = ["def-pc-scheme", "def-weil-weakly-etale-morphism", "def-weil-pbc-fpqc-covering"]
lean = ["AlgebraicGeometry.Scheme.proetalePrecoverage"]
order = 909
tags = ["mathlib"]
+++
Let $U$ be a scheme [def-pc-scheme]. A family of morphisms of schemes $\{f_i:U_i\to U\}_{i\in I}$ is a *pro-etale covering* if every $f_i$ is weakly etale [def-weil-weakly-etale-morphism] and the family is an fpqc covering [def-weil-pbc-fpqc-covering]: for every affine open $V\subset U$ there are finitely many indices $i_1,\dots,i_n$ and affine opens $V_j\subset U_{i_j}$ with $\bigcup_j f_{i_j}(V_j)=V$.
