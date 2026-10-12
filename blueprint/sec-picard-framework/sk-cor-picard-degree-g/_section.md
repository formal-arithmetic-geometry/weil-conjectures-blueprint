+++
id = "sk-cor-picard-degree-g"
kind = "corollary"
title = "The degree of the dictionary"
order = 751
uses = ["sec-abelian-varieties", "sk-def-av-jacobian"]
lean = ["AlgebraicGeometry.Scheme.degree_eq_genus"]
tags = ["sketch"]
+++
Let $X$ be a proper smooth curve over a field $k$ (smooth of relative
dimension $1$) with $H^0(X,\cO_X)=k$ (e.g. $X$ geometrically integral;
without it the statement fails: $\mathbf P^1_{\mathbf C}$ over
$k=\mathbf R$, $K=\mathbf C$), of genus $g=\dim_kH^1(X,\cO_X)$, and $\cL$
a line bundle on $X_K$ ($K/k$ any field extension) with
$h^0(X_K,\cL)=1$ and $H^q(X_K,\cL)=0$ for $q>0$. Then

$$
\deg(\cL)=\chi(\cL)-\chi(\cO_{X_K})=1-(1-g)=g.
$$
