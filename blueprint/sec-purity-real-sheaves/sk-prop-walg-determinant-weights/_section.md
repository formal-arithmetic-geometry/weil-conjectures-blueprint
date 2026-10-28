+++
id = "sk-prop-walg-determinant-weights"
kind = "proposition"
title = "Determinant weights of tensor operations"
lean = ["Representation.exists_detWeight_eq_add_of_subquotient_tprod", "Representation.exists_isIrreducible_subquotient_tprod_detWeight_eq_add", "Representation.CompositionSeries.exteriorPower_detWeight", "AlgebraicGeometry.WeilGroup.detWeight_subquotient_exteriorPower"]
order = 4068
uses = ["sk-d-real-detweights", "sk-d-real-weil", "sk-d-weights", "sk-i-restriction", "sk-p-central", "sk-p-readout", "sk-r-linear-library", "sk-r-real-linear"]
tags = ["sketch"]
+++
Let $U_0$ be a geometrically connected smooth curve over $k_0$, with Weil
group $W(U_0)$ and geometric fundamental group $\pi_1(U)$ as in
[sk-d-real-weil], and let $s\in W(U_0)$ be a lift of geometric Frobenius. A
*Weil representation* is a finite-dimensional
$\overline{\mathbf Q}_\ell$-representation of $W(U_0)$ whose restriction to
$\pi_1(U)$ is continuous; these are the lisse Weil
$\overline{\mathbf Q}_\ell$-sheaves on $U_0$. By [sk-d-real-detweights],
$\pi_1(U)$ acts through a finite group on the determinant of every Weil
representation.

Let $V$ and $V'$ be nonzero Weil representations, let $A_1,\ldots,A_t$ be
the composition factors of $V$, and put $\gamma_a=\dw_\iota(A_a)$
([sk-d-weights]).

1. $\operatorname{DW}(V\otimes V')=\operatorname{DW}(V)+\operatorname{DW}(V')$.
2. $\operatorname{DW}(\bigwedge^rV)=\bigl\{\sum_an_a\gamma_a :
   0\le n_a\le\dim A_a,\ \sum_an_a=r\bigr\}$ for $0\le r\le\dim V$.
