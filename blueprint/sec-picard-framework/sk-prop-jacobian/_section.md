+++
id = "sk-prop-jacobian"
kind = "proposition"
title = "The Jacobian is an abelian variety"
order = 740
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-def-picard-f", "sk-lem-picard-f-open", "sk-lem-picard-zero-dictionary", "sk-prop-picard-degree-decomposition", "sk-prop-picard-jacobian-tangent", "sk-prop-picard-pic-split", "sk-thm-picard-f-representable", "sk-thm-picard-hilb-curves", "sk-thm-picard-rr", "sk-thm-picard-twist"]
lean = ["AlgebraicGeometry.exists_jacobian"]
tags = ["sketch"]
+++
Let $k$ be separably closed and $C$ a $k$-scheme which is proper, smooth
of relative dimension $1$ and geometrically integral over $k$, of genus
$g=\dim_kH^1(C,\cO_C)$. Then $\underline{\Pic}^0_{C/k}$ is a proper, smooth, connected, commutative
group scheme of dimension $g$ over $k$, that is, an abelian variety, with
$T_e\underline{\Pic}^0_{C/k}\cong H^1(C,\cO_C)$. Hence
$J(C)=\underline{\Pic}^0_{C/k}$, with its representing isomorphism, is the
Jacobian of [sk-def-av-jacobian], and

$$
\Pic^0(C)=\{\cL\in\Pic(C):\deg\cL=0\}\;\cong\;J(C)(k),
$$

where $\deg\cL=\chi(\cL)-\chi(\cO_C)$, equivalently (by
Riemann–Roch [sk-thm-picard-rr]) the divisor degree $\deg D$ of any $D$ with
$\cL\cong\cO_C(D)$; and the formation of $J(C)$ commutes with algebraically closed base extension:
$J(C_{k'})=J(C)\times_kk'$ for $k\subseteq k'$ algebraically closed.
