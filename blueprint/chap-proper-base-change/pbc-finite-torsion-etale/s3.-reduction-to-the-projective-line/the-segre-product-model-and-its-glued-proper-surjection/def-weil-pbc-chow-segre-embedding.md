+++
id = "def-weil-pbc-chow-segre-embedding"
kind = "definition"
title = "Segre embedding of a product of projective spaces"
order = 1575
uses = ["def-weil-pbc-scheme-conventions"]
+++
For integers $n_1,\dots,n_m\geq0$, let $N=\prod_{i=1}^m(n_i+1)-1$ and let the
coordinates of $\mathbf P^N_Y$ be $X_{e}$, indexed by tuples
$e=(e_1,\dots,e_m)$ with $0\leq e_i\leq n_i$. The *Segre embedding* is the
morphism of $Y$-schemes

$$
 s:\prod_{i=1}^m\mathbf P^{n_i}_Y\longrightarrow\mathbf P^N_Y,
$$

given by the multihomogeneous coordinates

$$
 x\longmapsto\bigl[\prod_{i=1}^m x_{i,e_i}\bigr]_{e},
 \qquad x=(x_{i,0}:\cdots:x_{i,n_i})_{i=1}^m.
$$
