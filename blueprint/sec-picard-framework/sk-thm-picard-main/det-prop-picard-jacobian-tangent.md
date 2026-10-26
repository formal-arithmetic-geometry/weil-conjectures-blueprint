+++
id = "det-prop-picard-jacobian-tangent"
kind = "proposition"
title = "The tangent space of the Jacobian"
order = 824
uses = ["def-pc-picard-functor", "det-lem-picard-cech-computes", "det-prop-picard-degree-decomposition"]
lean = ["AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one"]
+++
The tangent space of the group scheme $\underline{\Pic}^0_{C/k}$ of
[det-prop-picard-degree-decomposition] at the unit is
$k$-linearly isomorphic to $H^1(C,\cO_C)$:

$$
T_e\underline{\Pic}^0_{C/k}\cong H^1(C,\cO_C)\qquad(\text{isomorphism of $k$-vector spaces}),
$$

a $k$-vector space of dimension $g$.
