+++
id = "def-weil-determinant-constants"
kind = "definition"
title = "Determinant constants and Euler characteristic"
lean = ["AlgebraicGeometry.Scheme.map_weilDeterminantConstant_eq_det", "AlgebraicGeometry.weilDeterminantConstant", "AlgebraicGeometry.weilDeterminantScalar", "AlgebraicGeometry.weilDeterminantConstant_ne_zero", "AlgebraicGeometry.weilDeterminantScalar_ne_zero"]
order = 3875
uses = ["def-weil-betti-numbers", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-integral-frobenius-factor", "def-weil-ordinary-compact-cohomology", "def-weil-smooth-proper-cohomological-family"]
+++
Let $p$ be prime, let $a\in\mathbf Z_{\geq1}$, put $q=p^a$, and set
$k_0=\Fq$; let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Fix a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, and fix an
indeterminate $T$. Let
$X_0/k_0$ be smooth and proper of pure dimension
$d\in\mathbf Z_{\geq0}$, and put $X=X_0\times_{k_0}k$. Let $F$ be
geometric Frobenius. For each integer $i$
with $0\leq i\leq2d$, let

$$
V_{i,\ell}=H^i(X,\Ql),\qquad
F_{i,\ell}=F\vert_{V_{i,\ell}},\qquad
P_{i,\ell}(T)=\det(1-TF_{i,\ell}\mid V_{i,\ell}).
$$

These data form the
smooth-proper
cohomological family, where $H^i(X,\Ql)$ is
ordinary cohomology. Define the Betti numbers, the Euler characteristic and
the determinant constant

$$
b_i=\dim_{\Ql}V_{i,\ell},\qquad
\chi=\sum_{i=0}^{2d}(-1)^ib_i,\qquad
D=\prod_{i=0}^{2d}\det(F_{i,\ell})^{(-1)^i}\in\Ql^\times,
$$

the operators $F_{i,\ell}$ being invertible.

In terms of integral factors (the form used in the zeta chapter): if
$P_i(T)\in\mathbf Z[T]$ is an
integral Frobenius factor
with $P_i(0)=1$ and $P_i^{(\ell)}(T)=P_{i,\ell}(T)$, where
$P^{(\ell)}(T)=\sum_r(c_r\cdot1_{\Ql})T^r$ for $P(T)=\sum_rc_rT^r\in\mathbf Z[T]$,
then $b_i=\deg P_i$ is the
Betti number of the integral factors, and with
$[T^m]P(T)=c_m$ for the coefficient of $T^m$ one puts

$$
D_i=(-1)^{b_i}[T^{b_i}]P_i(T)\in\mathbf Z\setminus\{0\},\qquad
\Delta=\prod_{i=0}^{2d}D_i^{(-1)^i}\in\mathbf Q^\times;
$$

the image of $D_i$ in $\Ql$ is
$\det(F_{i,\ell}\mid H^i(X,\Ql))$, so the image of $\Delta$ in $\Ql$ is $D$.
