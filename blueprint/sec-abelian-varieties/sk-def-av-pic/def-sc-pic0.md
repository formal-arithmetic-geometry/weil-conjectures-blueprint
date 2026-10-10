+++
id = "def-sc-pic0"
kind = "definition"
title = "Degree and $\\operatorname{Pic}^0$"
lean = ["AlgebraicGeometry.Scheme.Hom.picZero"]
order = 445
uses = ["def-sc-curves", "def-sc-divisor", "def-sc-picard-group"]
+++
Let $C$ be a scheme over a field $k$, and for an $\mathcal O_C$-module
$\mathcal F$ write $\chi(C,\mathcal F)=\sum_i(-1)^i\dim_kH^i(C,\mathcal F)$.
The *degree* of the class of an invertible $\mathcal O_C$-module
$\mathcal L$ in $\operatorname{Pic}(C)$ ([def-sc-picard-group]) is

$$
\deg[\mathcal L]:=\chi(C,\mathcal L)-\chi(C,\mathcal O_C).
$$

Put

$$
\operatorname{Pic}^0(C):=\{[\mathcal L]\in\operatorname{Pic}(C):\deg[\mathcal L]=0\}.
$$

For a proper smooth connected curve $C$ over an algebraically closed
field $k$ ([def-sc-curves]) one has $\deg[\mathcal O(D)]=\deg D$ for
every divisor $D$ ([def-sc-divisor]), and the class of a $k$-rational
point has degree $1$. In that case $\deg$ is a group homomorphism
$\operatorname{Pic}(C)\to\mathbf Z$, the degree of a principal divisor
is $0$, and $\operatorname{Pic}^0(C)=\ker(\deg)$ is a subgroup.
