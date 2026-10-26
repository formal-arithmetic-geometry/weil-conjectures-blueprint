+++
id = "def-mg-determinant-line"
kind = "definition"
title = "Determinant line"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.det", "Matrix.GeneralLinearGroup.detGL", "Matrix.GeneralLinearGroup.exists_algHom_comp_eq_evalAlgHom_detGL"]
order = 3729
uses = ["d-monodromy"]
+++
Let $\rho:W\to\operatorname{GL}(V)$ be a Weil representation of rank $r$
of a degree datum ([d-monodromy]). Its *determinant line* is the
rank-one Weil representation

$$
\det(V):=\bigwedge\nolimits^r V,
\qquad
\det(\rho)(g)=\det(\rho(g)).
$$

With the same degree datum it is again a represented degree datum. The
determinant $\det:\operatorname{GL}_r\to\operatorname{GL}_1$ is a
homomorphism of algebraic groups, given by a polynomial in the matrix
entries, and $\det(\rho)$ is the composite of $\rho$ with it.
