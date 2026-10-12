+++
id = "sk-p-readout"
kind = "proposition"
title = "Central scalars and weight readout"
order = 2856
uses = ["sk-d-central", "sk-d-linear", "sk-d-monodromy", "sk-d-tangent", "sk-d-weights", "sk-r-linear-library"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair"]
tags = ["sketch"]
+++
Fix a real weight character $\lambda$,
monodromy data and a
positive central pair $(N,z)$.
Let $Q=S/U\ne0$ be a $W$-subquotient of the
defining representation $V=k^n$ of the datum, with
finite geometric determinant. If $z$ acts on
$Q$ as a scalar $c_Q\in k^\times$, then

$$
\dw_\lambda(Q)=\frac{\lambda(c_Q)}{N}.
$$

The scalar-action hypothesis holds whenever $Q$ is simple and $k$ is
algebraically closed.
The determinant weight is independent of the chosen degree-one lift.
