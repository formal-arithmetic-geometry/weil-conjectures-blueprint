+++
id = "def-nagata-rees-polynomial-map"
kind = "definition"
title = "Homogeneous polynomial map to the Rees algebra"
order = 242
lean = ["AlgebraicGeometry.reesGradedPresentation"]
uses = ["def-nagata-rees-algebra"]
+++
Let $A$ be a ring, let $I\subseteq A$ be an ideal, and fix generators
$I=(f_0,\ldots,f_r)$. Define the $A$-algebra map

$$
\rho_I\colon A[T_0,\ldots,T_r]\longrightarrow\mathcal R_A(I)
$$

by $\rho_I(T_i)=f_it$, with each $T_i$ placed in degree one.
