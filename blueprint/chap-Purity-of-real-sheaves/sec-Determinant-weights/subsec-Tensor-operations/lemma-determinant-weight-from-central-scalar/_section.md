+++
id = "lemma-determinant-weight-from-central-scalar"
kind = "lemma"
title = "Determinant weight from a central scalar"
order = 1145
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_detWeight_eq_of_isPositiveCentralPair_of_isIrreducible", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair_of_basis"]
uses = ["lemma-normality-geometric-monodromy"]
+++
In the setting of Proposition [proposition-central-element-arithmetic-monodromy-group], let $Q$
be a nonzero subquotient of a tensor construction on $V$ on which the
element $z$ acts by a scalar $c_Q$. Then

$$
\operatorname{dw}_\iota(Q)=\frac{\lambda_\iota(c_Q)}{N}.
$$
