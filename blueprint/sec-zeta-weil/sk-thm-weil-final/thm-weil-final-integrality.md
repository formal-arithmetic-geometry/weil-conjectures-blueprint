+++
id = "thm-weil-final-integrality"
kind = "theorem"
title = "Weil conjectures II: integral Frobenius factors"
order = 4386
lean = ["AlgebraicGeometry.IsWeilFactorization", "AlgebraicGeometry.Scheme.weil_conjectures", "AlgebraicGeometry.Scheme.weil_integral_factors"]
uses = ["def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-integral-frobenius-factor", "def-weil-ordinary-compact-cohomology", "def-weil-point-counts-zeta", "prop-galois-weight-strata-identification", "prop-galois-weight-strata-integrality", "prop-integral-recovery", "prop-weight-purity-roots", "prop-weight-separation", "prop-weil-zeta-normalized-presentation", "thm-weil-realization-independence"]
+++
Fix a finite field
$k_0=\mathbf F_q$ of characteristic $p$, with algebraic closure
$k=\overline{\mathbf F}_q$.
Let $X_0/k_0$ be
smooth, proper and geometrically
connected of pure dimension $d\geq0$, and put $X=X_0\times_{k_0}k$.
For every prime $\ell\neq p$, let $F_{i,\ell}$ be the
geometric Frobenius
on the cohomology
$H^i(X,\mathbf Q_\ell)$.
Let $Z(X_0,T)$ be the
point-count zeta series.
Then, for every integer $i$ with
$0\leq i\leq2d$, there is a
unique polynomial

$$
P_i(T)\in\mathbf Z[T]
$$

with $P_i(0)=1$ such that, for every prime $\ell\neq p$, its
coefficientwise extension $P_i^{(\ell)}(T)\in\Ql[T]$ satisfies

$$
P_i^{(\ell)}(T)=
\det(1-TF_{i,\ell}\mid H^i(X,\Ql)).
$$

Call these the
integral Frobenius factors and
retain this
coefficientwise-extension notation.
They give the rational factorization

$$
Z(X_0,T)=
\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}},
$$

and this factorization is independent of the chosen $\ell$.
