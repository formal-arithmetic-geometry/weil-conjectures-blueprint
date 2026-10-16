+++
id = "lem-wf-solvable-common-eigenvector"
kind = "lemma"
title = "Common eigenvector for a solvable Lie algebra"
lean = ["LieModule.exists_ne_zero_forall_lie_eq_smul_of_isSolvable"]
order = 2817
+++
Let a finite-dimensional solvable Lie algebra $\mathfrak r$ over
$\Qlb$ act on a nonzero finite-dimensional vector space $M$.
Then there are $0\ne v\in M$ and a linear form
$\lambda:\mathfrak r\to\Qlb$ such that

$$
Xv=\lambda(X)v\quad(X\in\mathfrak r),
\qquad \lambda([\mathfrak r,\mathfrak r])=0.
$$
