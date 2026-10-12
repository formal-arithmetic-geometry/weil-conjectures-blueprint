+++
id = "lem-weil-pbc-cauchy-binet"
kind = "lemma"
title = "The Cauchy–Binet formula"
lean = ["Matrix.cauchy_binet"]
source = "literature/stacks-project/algebra.tex, Algebra, Section Tag 00AR (section-rings-basic), list item Tag 0F0K (item-cauchy-binet, line 282), stated there without proof as a basic fact"
+++
Let $R$ be a commutative ring, $m,n\ge0$ integers, $A=(a_{ij})$ an $m\times n$ matrix and $B=(b_{jk})$ an $n\times m$ matrix with entries in $R$ `Matrix` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Matrix/Defs.lean)), and $AB$ their product, the $m\times m$ matrix with entries $(AB)_{ik}=\sum_{j=1}^n a_{ij}b_{jk}$. For a subset $S\subseteq\{1,\dots,n\}$ with $|S|=m$, let $A^{S}$ be the $m\times m$ submatrix `Matrix.submatrix` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Matrix/Defs.lean)) of $A$ formed by the columns with indices in $S$ and $B_S$ the $m\times m$ submatrix of $B$ formed by the rows with indices in $S$, both taken in increasing order of the indices. Then, with $\det$ the determinant of a square matrix `Matrix.det` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean)), $$\det(AB)=\sum_{S\subseteq\{1,\dots,n\},\ |S|=m}\det(A^{S})\det(B_S)$$ in $R$. (For $n<m$ the sum is empty and $\det(AB)=0$; for $m=0$ both sides are $1$.)
