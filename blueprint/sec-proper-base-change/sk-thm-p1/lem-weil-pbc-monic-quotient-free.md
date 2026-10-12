+++
id = "lem-weil-pbc-monic-quotient-free"
kind = "lemma"
title = "The quotient of a polynomial ring by a monic polynomial is free with the power basis"
lean = ["AdjoinRoot.powerBasis'"]
tags = ["sheaf-dag", "mathlib", "stacks-04GG"]
+++
Let $R$ be a commutative ring and $f\in R[T ]$ monic of degree $n$. Then $R[T ]/(f)$ is a free $R$-module with basis the classes of $1,T,\dots,T^{n-1}$; in particular it is a finite $R$-algebra, and for every ideal $I\subset R$ one has $(R[T ]/(f))/I(R[T ]/(f))\cong(R/I)[T ]/(\overline f)$.
