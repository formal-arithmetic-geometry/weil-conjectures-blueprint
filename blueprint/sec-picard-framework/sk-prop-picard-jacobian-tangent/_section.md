+++
id = "sk-prop-picard-jacobian-tangent"
kind = "proposition"
title = "The tangent space of the Jacobian"
order = 852
uses = ["sk-def-av-jacobian", "sk-def-picard-pic", "sk-lem-picard-cech-computes", "sk-prop-picard-degree-decomposition"]
lean = ["AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one"]
tags = ["sketch"]
+++
The tangent space of the group scheme $\underline{\Pic}^0_{C/k}$ of
[sk-prop-picard-degree-decomposition] at the unit is
$k$-linearly isomorphic to $H^1(C,\cO_C)$:

$$
T_e\underline{\Pic}^0_{C/k}\cong H^1(C,\cO_C)\qquad(\text{isomorphism of $k$-vector spaces}),
$$

a $k$-vector space of dimension $g$.
