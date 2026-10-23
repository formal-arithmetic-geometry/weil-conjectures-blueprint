+++
id = "def-mg-determinant-line"
kind = "definition"
title = "Determinant line"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.det", "Matrix.GeneralLinearGroup.detGL", "Matrix.GeneralLinearGroup.exists_algHom_comp_eq_evalAlgHom_detGL"]
order = 3751
uses = ["def-weil-weil-sheaf-complex", "def-wf-fundamental-representation", "sk-lem-coefficient-heart"]
+++
If $\mathcal V$ is a rank-$r$ lisse
Weil sheaf with
fundamental representation
$V$, its *determinant line* is the rank-one Weil representation

$$
\det(V):=\bigwedge\nolimits^r V,
\qquad
\det(\rho)(g)=\det(\rho(g)).
$$

The corresponding rank-one Weil sheaf is denoted $\det(\mathcal V)$.
