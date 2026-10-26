+++
id = "lem-weil-pbc-curve-constructible-sub-quotient"
kind = "lemma"
title = "Subsheaves and quotients of a constructible sheaf on a curve are constructible"
uses = ["def-weil-algebraic-closure", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-etale-sheaves", "def-weil-pbc-curve-setting"]
lean = ["AlgebraicGeometry.CurveCoefficientPair.constructible_sub_quotient"]
order = 1918
tags = ["stacks-09BH"]
+++
Let $k$ be an algebraically closed field [def-weil-algebraic-closure], let $C$ be a separated scheme of finite type over $k$ with $\dim C\le1$, and let $0\to F_1\xrightarrow{\alpha}F\xrightarrow{\beta}F_2\to0$ be a short exact sequence in the abelian category $\Ab(C_{\Et})$ of abelian sheaves on the small etale site [def-weil-pbc-abelian-etale-sheaves] whose three terms are torsion [def-weil-pbc-etale-sheaves], so that $(C,F_1)$, $(C,F)$, $(C,F_2)$ are curve coefficient pairs [def-weil-pbc-curve-setting]. If the underlying sheaf of sets of $F$ is constructible in the sense of [def-weil-pbc-etale-sheaves] (a finite partition of $C$ into locally closed constructible subschemes on each of which its inverse image is finite locally constant), then the underlying sheaves of sets of $F_1$ and $F_2$ are constructible in the same sense.
