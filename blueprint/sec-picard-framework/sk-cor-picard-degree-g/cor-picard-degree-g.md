+++
id = "cor-picard-degree-g"
kind = "theorem"
title = "The degree of the dictionary"
order = 752
uses = ["def-pc-degree-line-bundle", "def-pc-euler-characteristic", "def-pc-smooth-projective-curve", "lem-pc-curves-are-sc", "lem-pc-genus-base-change"]
tags = ["latex:corollary"]
lean = ["AlgebraicGeometry.Scheme.degree_eq_genus"]
+++
Let $k$ be a field and $X$ a $k$-scheme which is proper and smooth of
relative dimension $1$ over $k$, such that the canonical map
$k\to H^0(X,\cO_X)$ is bijective (this is needed: for
$X=\mathbf P^1_{\mathbf C}$ over $k=\mathbf R$ and $K=\mathbf C$ the
conclusion fails), and let $g=\dim_kH^1(X,\cO_X)$ be its genus. Let $K/k$
be any field extension and $\cL$ an invertible module on $X_K$ with
$h^0(X_K,\cL)=1$ and $H^q(X_K,\cL)=0$ for $q>0$. Then

$$
\deg(\cL)=\chi(\cL)-\chi(\cO_{X_K})=1-(1-g)=g.
$$
