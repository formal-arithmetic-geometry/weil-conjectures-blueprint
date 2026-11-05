+++
id = "corollary-point-counting-zeta-function--2"
kind = "corollary"
title = "Alternating point-counting trace over a field"
order = 1039003
aliases = ["bp-r318-2"]
lean = ["AlgebraicGeometry.WeilSheaf.pointCount_eq_finsum_trace_compactlySupportedCohomology"]
uses = ["definition-small-pro-etale-site", "definition-weil-structure", "definition-frobenius-operator"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and let $\ell$ be a
prime with $\ell\nmid q$. Give the constant sheaf
$\Lambda_X$, where $\Lambda=\overline{\mathbf Q}_\ell$, its canonical
Weil structure. For every $m\geq1$, in $\Lambda$,

$$
\#X_0(\mathbf F_{q^m})=\sum_i(-1)^i\operatorname{Tr}(\operatorname{Frob}_{X,\Lambda_X}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},\Lambda_X)).
$$

The sum is over $i\in\mathbf Z$ and has finite support.
