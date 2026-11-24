+++
id = "prose-14-09"
kind = "hidden"
title = "Finite monodromy (4)"
order = 1112
+++
For a Kummer sheaf on $\mathbf G_{m,k_0}$ the corollary gives weight
$0$, since $\chi(s)$ is then a root of unity. For [$\mathcal B_b$](@proposition-weights-under-usual-operations) it
gives $\lambda_\iota(b)$, the weight found in
Proposition [proposition-weights-under-usual-operations].

Before purity is known, the eigenvalues of a [lisse](@definition-lisse-sheaves) sheaf $\mathcal V$
of rank $r$ at a closed point are not controlled individually. Their
product, however, is controlled, since it is the eigenvalue of the rank-one sheaf
$\det\mathcal V$, whose weight is given by Corollary [corollary-rank-one-weights].
Dividing by $r$ we get the average weight of the eigenvalues, which is the only
candidate for a weight of $\mathcal V$. Indeed, if $\mathcal V$ is [pure](@definition-weights) of
weight $w$, then $\det\mathcal V$ is [pure](@definition-weights) of weight $rw$, and the number
defined below is $w$. For a sheaf that is not [pure](@definition-weights), on the other hand, the number is only an
average. For example, on $\overline{\mathbf Q}_\ell\oplus\href{@definition-tate-twists}{\overline{\mathbf Q}_\ell(-1)}$ the determinant is [$\overline{\mathbf Q}_\ell(-1)$](@definition-tate-twists), of
weight $2$, and the number is $1$, the weight of no eigenvalue. For this
reason we apply it to irreducible constituents:
Proposition [proposition-bound-largest-determinant-weight] bounds the
eigenvalues of a real sheaf by the largest determinant weight of its
constituents, and Theorem [theorem-purity-real-sheaves-curves] then shows that
each irreducible constituent is [pure](@definition-weights) of weight equal to its determinant weight.
