+++
id = "definition-determinant-weight"
kind = "definition"
title = "Determinant weight"
order = 1113
lean = ["AlgebraicGeometry.WeilGroup.detWeight", "AlgebraicGeometry.WeilGroup.HasDetWeight", "AlgebraicGeometry.WeilGroup.detWeightMultiset"]
+++
Let $\mathcal V$ be a nonzero lisse Weil sheaf of rank $r$ on a smooth
geometrically connected curve $U_0$, let $\rho$ be the corresponding
representation of $W(U_0)$, and let $s\in W(U_0)$ be a lift of degree
one. The *determinant weight* of $\mathcal V$ is

$$
\operatorname{dw}_\iota(\mathcal V)
=\frac{\lambda_\iota(\det\rho(s))}{r}
$$

(this does not depend on $s$, Corollary [corollary-determinant-weights]).
For a lisse Weil sheaf $\mathcal V$ we write $\operatorname{DW}(\mathcal V)$
for the set of determinant weights of its irreducible constituents.
