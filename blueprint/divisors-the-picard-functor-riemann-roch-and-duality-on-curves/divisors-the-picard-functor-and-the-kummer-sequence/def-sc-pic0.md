+++
id = "def-sc-pic0"
kind = "definition"
title = "Degree and Pic^0"
order = 3604
lean = ["AlgebraicGeometry.Curve.degreeHom", "AlgebraicGeometry.Curve.Pic0"]
uses = ["def-sc-divisor", "lem-sc-divisor-class-curve", "lem-sc-deg-principal-zero"]
+++
Let $C$ be a proper smooth curve over algebraically closed $k$. The
*degree* is the homomorphism
$$
 \deg:\operatorname{Pic}(C)\to\mathbf Z,\qquad
 \deg[\mathcal O(D)]=\deg D,
$$
of the divisor class group of [def-sc-divisor], transported across the
identification $\operatorname{Cl}(C)\cong\operatorname{Pic}(C)$ of
[lem-sc-divisor-class-curve]; it sends the class of a $k$-rational point to
$1$. That it is well defined, i.e. that it vanishes on principal divisors,
is [lem-sc-deg-principal-zero], and it is not part of the definition. Put
$$
 \operatorname{Pic}^0(C):=\ker(\deg).
$$

Unresolved dependencies: def:sc-curves, def:sc-picard-group
