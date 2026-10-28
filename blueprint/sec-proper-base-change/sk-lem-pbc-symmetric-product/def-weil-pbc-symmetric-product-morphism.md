+++
id = "def-weil-pbc-symmetric-product-morphism"
kind = "definition"
title = "Symmetric-product coordinate morphism"
lean = ["AlgebraicGeometry.ProjectiveSpace.symmetricProduct"]
order = 2054
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-symmetric-product-properties"]
+++
For $n\geq0$ and a scheme $S$, write $(\mathbf P^1_S)^n$ for the $n$-fold fibre
power of $\mathbf P^1_S$ over $S$ (for $n=0$ this is $S$), and define polynomials
$F_0,\dots,F_n$ by

$$
 \prod_{i=1}^n(x_it+y_i)=\sum_{j=0}^nF_jt^j.
$$

Each $F_j$ is multihomogeneous of degree one in every pair $(x_i,y_i)$. The
*symmetric-product morphism* is the $S$-morphism

$$
 \sigma_n:(\mathbf P^1_S)^n\longrightarrow\mathbf P^n_S,\qquad
 ((x_1:y_1),\dots,(x_n:y_n))\longmapsto[F_0:\cdots:F_n].
$$

It is defined by induction on $n$: $\sigma_0$ is the identification
$S\cong\mathbf P^0_S$, and $\sigma_{n+1}$ is the composite of the base change
$\mathbf P^1_{\sigma_n}:\mathbf P^1_{(\mathbf P^1_S)^n}\to\mathbf P^1_{\mathbf P^n_S}$
with the *multiplication morphism*
$\mu:\mathbf P^1_{\mathbf P^n_S}\to\mathbf P^{n+1}_S$, which sends a linear form
$(x:y)$ and a form $\sum_jG_jt^j$ of degree at most $n$ to their product
$(xt+y)\sum_jG_jt^j$ (well defined by
[lem-weil-pbc-symmetric-product-properties]).
