+++
id = "corollary-point-counting-zeta-function--5"
kind = "corollary"
title = "Cohomological determinant product"
order = 1039006
aliases = ["bp-r318-5"]
lean = ["TraceDatum.zeta_mul_prod_even_eq_prod_odd", "TraceDatum.map_zetaSeries"]
uses = ["corollary-point-counting-zeta-function--3", "definition-weil-structure", "definition-frobenius-operator"]
+++
Let $L$ be a field of characteristic zero. A trace datum consists of
finite-dimensional $L$-vector spaces $V_0,\ldots,V_r$, endomorphisms
$F_i$ of $V_i$, and integers $N_m$ such that, for every $m\geq1$,

$$
N_m=\sum_{i=0}^r(-1)^i\operatorname{Tr}(F_i^m\mid V_i).
$$

Put $P_i(T)=\det(1-TF_i\mid V_i)$ and
$Z_D(T)=\exp(\sum_{m\geq1}N_mT^m/m)$. Then, in $L[[T]]$,

$$
Z_D(T)\prod_{\substack{0\leq i\leq r\\i\text{ even}}}P_i(T)
=\prod_{\substack{0\leq i\leq r\\i\text{ odd}}}P_i(T).
$$

If $N_m$ is the point-count sequence of $X_0$ used in
[corollary-point-counting-zeta-function--3], the image of $Z(X_0,T)$
under $\mathbf Q[[T]]\longrightarrow L[[T]]$ equals $Z_D(T)$.
For the separated $X_0$ above, take $L=\Lambda=\overline{\mathbf Q}_\ell$
and the finite family of compactly supported cohomology groups with
their Frobenius operators. This gives

$$
Z(X_0,T)=\prod_{i\in\mathbf Z}
\det(1-T\operatorname{Frob}_{X,\Lambda_X}\mid
H_c^i(X_{\mathrm{pro}\acute{e}t},\Lambda_X))^{(-1)^{i+1}}
\quad\text{in }\Lambda[[T]].
$$
