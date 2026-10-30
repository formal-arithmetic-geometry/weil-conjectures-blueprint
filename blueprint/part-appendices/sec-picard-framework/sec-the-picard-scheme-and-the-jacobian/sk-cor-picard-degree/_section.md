+++
id = "sk-cor-picard-degree"
kind = "corollary"
title = "Degree and the Jacobian"
order = 898
lean = ["AlgebraicGeometry.Scheme.picDegreeHom", "AlgebraicGeometry.Scheme.surjective_picDegreeHom", "AlgebraicGeometry.Scheme.coe_ker_picDegreeHom", "AlgebraicGeometry.Scheme.exists_mulEquiv_prod_ker_picDegreeHom", "AlgebraicGeometry.exists_jacobian"]
uses = ["sk-thm-picard-main", "sec-abelian-varieties", "sk-def-picard-pic"]
tags = ["sketch"]
+++
Let $C$ be a smooth proper connected curve over an algebraically closed
field $k$. There is an exact sequence

$$
0\longrightarrow J(C)(k)
\longrightarrow\operatorname{Pic}(C)
\xrightarrow{\deg}\mathbf Z\longrightarrow0,
$$

and a point $P\in C(k)$ splits it by $d\mapsto\mathcal O_C(dP)$.
