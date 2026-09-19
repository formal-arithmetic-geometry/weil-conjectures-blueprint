+++
id = "def-weil-frobenius"
kind = "definition"
title = "Arithmetic and geometric Frobenius"
order = 5
uses = ["def-weil-base-field"]
+++
The arithmetic Frobenius of $k$ is

$$
\varphi_q:k\longrightarrow k,
\qquad z\longmapsto z^q.
$$

The geometric Frobenius element is
$\gamma=\operatorname{Frob}_q=\varphi_q^{-1}$. If
$Y=Y_0\times_{k_0}k$, the associated semilinear automorphism is

$$
g_Y=\operatorname{id}_{Y_0}\times\Spec(\gamma):Y\longrightarrow Y.
$$

It is distinct from the absolute $q$-power morphism of the scheme $Y$.
Every Frobenius operator below is induced by $g_Y$ and is geometric.
