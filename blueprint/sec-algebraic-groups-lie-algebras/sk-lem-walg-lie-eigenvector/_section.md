+++
id = "sk-lem-walg-lie-eigenvector"
kind = "lemma"
title = "Lie's eigenvector theorem"
lean = ["LieModule.exists_ne_zero_forall_lie_eq_smul_of_isSolvable"]
order = 3696
tags = ["sketch"]
+++
The derived series of a Lie algebra is $D^0\mathfrak l=\mathfrak l$,
$D^{n+1}\mathfrak l=[D^n\mathfrak l,D^n\mathfrak l]$. The Lie algebra
$\mathfrak l$ is solvable if this series reaches zero.

A solvable Lie algebra acting on a nonzero vector space $M$ has a common
eigenvector. Equivalently, there are $v\ne0$ and a linear functional
$\lambda$ such that $av=\lambda(a)v$ for every $a$.
