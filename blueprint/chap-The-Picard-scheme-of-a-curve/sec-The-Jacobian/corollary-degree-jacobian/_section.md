+++
id = "corollary-degree-jacobian"
kind = "corollary"
title = "Degree and the Jacobian"
order = 1552
lean = ["AlgebraicGeometry.Scheme.picDegreeHom", "AlgebraicGeometry.Scheme.exists_jacobian_addEquiv_prod"]
uses = ["definition-relative-picard-functor"]
+++
Let $C$ be a smooth proper connected curve over an algebraically closed
field $k$. There is an exact sequence

$$
0\longrightarrow J(C)(k)
\longrightarrow\operatorname{Pic}(C)
\xrightarrow{\deg}\mathbf Z\longrightarrow0,
$$

and a point $P\in C(k)$ splits it by $d\mapsto\mathcal O_C(dP)$.
