+++
id = "thm-weil-final-betti"
kind = "theorem"
title = "Weil conjectures IV: Betti symmetry"
order = 2935
uses = ["def-weil-betti-numbers", "def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-integral-frobenius-factor", "def-weil-ordinary-compact-cohomology", "prop-endpoints", "prop-integral-recovery", "prop-poincare-pairing", "prop-weil-betti-comparison", "thm-weil-final-integrality", "thm-weil-final-rh", "thm-weil-poincare-duality", "thm-weil-six-operations"]
+++
Fix a finite field
$k_0=\mathbf F_q$ of characteristic $p$, with algebraic closure
$k=\overline{\mathbf F}_q$.
Let $X_0/k_0$ be
smooth, proper and geometrically
connected of pure dimension $d\geq0$, and put $X=X_0\times_{k_0}k$.
Let $P_i\in\mathbf Z[T]$, $0\leq i\leq2d$, be the
integral Frobenius factors
provided by [thm-weil-final-integrality]: $P_i(0)=1$, and for
every $\ell\neq p$,

$$
P_i^{(\ell)}(T)=\det(1-TF_{i,\ell}\mid H^i(X,\mathbf Q_\ell)),
$$

where $F_{i,\ell}$ is
geometric Frobenius
on ordinary cohomology,
and $P_i^{(\ell)}$ means coefficientwise extension
$\mathbf Z\to\mathbf Q_\ell$.
For every integer $i$ with $0\leq i\leq2d$, set
$b_i=\deg P_i$; these are the
Betti numbers. Then

$$
b_i=\dim_{\Ql}H^i(X,\Ql)
\quad\text{for every prime }\ell\neq p,
\qquad b_i=b_{2d-i},
\qquad b_0=b_{2d}=1,
$$

where $H^i(X,\Ql)$ is the
ordinary cohomology group;
so the first dimension is independent of $\ell$. Moreover

$$
P_0(T)=1-T,
\qquad
P_{2d}(T)=1-q^dT.
$$

In particular, the rational function
$Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}\in\mathbf Q(T)$ of
[thm-weil-final-integrality] has a pole of order exactly $1$ at $T=1$
and, if $d\geq1$, a pole of order exactly $1$ at $T=q^{-d}$.
