+++
id = "lem-weil-pbc-symmetric-product-properties"
kind = "lemma"
title = "No common zero of the product coefficients"
lean = ["AlgebraicGeometry.ProjectiveSpace.span_range_bilinearChartSection_mulForm"]
order = 1952
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $n\geq0$ and consider, over $\mathbf Z$, the product $\mathbf P^1\times\mathbf P^n$
with homogeneous coordinates $(a_0:a_1)$ and $(b_0:\cdots:b_n)$. The
coefficients

$$
 c_m=a_0b_{m-1}+a_1b_m\qquad(0\leq m\leq n+1,\ b_{-1}=b_{n+1}=0)
$$

of the product $(a_0t+a_1)\sum_jb_jt^j$ have no common zero: on every standard
chart $D_+(a_i)\times D_+(b_j)$ the dehomogenized coefficients generate the unit
ideal. Hence, after base change to any scheme $S$, they define a morphism
$\mu:\mathbf P^1_{\mathbf P^n_S}\to\mathbf P^{n+1}_S$ over $S$, the
multiplication morphism.
