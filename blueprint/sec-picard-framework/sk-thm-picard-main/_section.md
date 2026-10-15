+++
id = "sk-thm-picard-main"
kind = "theorem"
title = "The Picard scheme and Jacobian of a geometric curve"
order = 610
uses = ["sk-def-av-jacobian", "sk-def-picard-pic", "sk-prop-picard-pic-split", "sk-thm-picard-f-representable", "sk-thm-picard-twist", "sk-thm-picard-criterion", "sk-def-av-pic", "sk-def-picard-f", "sk-lem-picard-f-open", "sk-lem-picard-zero-dictionary", "sk-thm-picard-hilb-curves", "sk-thm-picard-rr"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctor", "AlgebraicGeometry.exists_jacobian"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed and let $C/k$ be a smooth proper
connected curve of genus $g$. The fppf Picard functor is represented by a
smooth separated group scheme, locally of finite type over $k$, with a
decomposition

$$
\operatorname{Pic}_{C/k}=\coprod_{d\in\Z}\operatorname{Pic}^d_{C/k}.
$$

Each component is a smooth proper geometrically connected variety of
dimension $g$, parametrizing invertible sheaves of degree $d$. The
identity component $J(C)=\operatorname{Pic}^0_{C/k}$ is an abelian
variety, and

$$
J(C)(k)=\operatorname{Pic}^0(C),
\qquad T_0J(C)=H^1(C,\cO_C).
$$

The formation of this representing functor, its degree components and
$J(C)$ commutes with extension of the ground field.

*Complement (separably closed ground field).* More generally, let $k$ be
separably closed and $C$ a $k$-scheme which is proper, smooth of relative
dimension $1$ and geometrically integral over $k$, of genus
$g=\dim_kH^1(C,\cO_C)$. Then $\underline{\Pic}^0_{C/k}$ is a proper, smooth,
connected, commutative group scheme of dimension $g$ over $k$, that is, an
abelian variety, with $T_e\underline{\Pic}^0_{C/k}\cong H^1(C,\cO_C)$. Hence
$J(C)=\underline{\Pic}^0_{C/k}$, with its representing isomorphism, is the
Jacobian of [sk-def-av-jacobian], and

$$
\Pic^0(C)=\{\cL\in\Pic(C):\deg\cL=0\}\;\cong\;J(C)(k),
$$

where $\deg\cL=\chi(\cL)-\chi(\cO_C)$, equivalently (by Riemann–Roch
[sk-thm-picard-rr]) the divisor degree $\deg D$ of any $D$ with
$\cL\cong\cO_C(D)$; and the formation of $J(C)$ commutes with algebraically
closed base extension: $J(C_{k'})=J(C)\times_kk'$ for $k\subseteq k'$
algebraically closed. (Representability by a group scheme in this
generality is the form proved by the detailed node
`thm-pc-picard-representable`.)
