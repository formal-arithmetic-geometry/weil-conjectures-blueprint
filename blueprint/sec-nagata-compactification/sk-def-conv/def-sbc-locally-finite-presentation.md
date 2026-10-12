+++
id = "def-sbc-locally-finite-presentation"
kind = "definition"
title = "Morphisms locally of finite presentation"
order = 4
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.LocallyOfFinitePresentation"]
tags = ["mathlib", "stacks-01TP"]
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme]. $f$ is *of finite presentation at* a point $x\in X$ if there exist an affine open neighbourhood $U=\operatorname{Spec}(A)\subset X$ of $x$ and an affine open $V=\operatorname{Spec}(R)\subset S$ with $f(U)\subset V$ such that the induced ring map $R\to A$ is of finite presentation, i.e. $A$ is isomorphic as an $R$-algebra to $R[x_1,\ldots,x_n]/(f_1,\ldots,f_m)$ for some $n,m\geq0$ and polynomials $f_j$. $f$ is *locally of finite presentation* if it is of finite presentation at every point of $X$. (For comparison: $f$ is *of finite presentation* if it is locally of finite presentation, quasi-compact and quasi-separated.)
