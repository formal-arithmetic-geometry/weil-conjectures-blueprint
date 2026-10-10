+++
kind  = "proof"
of    = "lem-sc-fixed-points-finite"
+++
$V^F=\ker(F-1)$, and $F-1$ is $\mathbf F_p$-linear, so $V^F$
is an $\mathbf F_p$-vector space. If $v_1,\dots,v_r\in V^F$ are
$\mathbf F_p$-linearly independent and
$\sum_i\lambda_iv_i=0$ is a shortest $k$-linear dependence
($r\geq2$, $\lambda_1\neq0$), then applying $F$ gives
$\sum_i\lambda_i^pv_i=0$; dividing by $\lambda_1$ and subtracting
the two relations yields

$$
\sum_{i=2}^r\bigl((\lambda_i/\lambda_1)-(\lambda_i/\lambda_1)^p\bigr)v_i=0,
$$

a shorter dependence, so by minimality
$\lambda_i/\lambda_1\in\mathbf F_p$ for all $i$, and then
$\sum_i(\lambda_i/\lambda_1)v_i=0$ is an $\mathbf F_p$-linear
dependence, contradicting independence. Hence
$r\leq\dim_kV$.
