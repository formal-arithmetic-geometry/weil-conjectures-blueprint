+++
id = "sk-thm-picard-main"
kind = "theorem"
title = "The Picard scheme and Jacobian of a geometric curve"
order = 610
uses = ["sk-def-av-jacobian", "sk-def-picard-pic", "sk-prop-picard-pic-split", "sk-thm-picard-f-representable", "sk-thm-picard-twist", "sk-thm-picard-criterion"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctor"]
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

(Representability by a group scheme holds more generally for $k$
separably closed and $C$ smooth, proper and geometrically integral over
$k$; this is the form proved by the detailed node
`thm-pc-picard-representable`.)
