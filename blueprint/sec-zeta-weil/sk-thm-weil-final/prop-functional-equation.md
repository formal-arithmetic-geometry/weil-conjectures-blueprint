+++
id = "prop-functional-equation"
kind = "theorem"
title = "Functional equation"
lean = ["AlgebraicGeometry.WeilFunctionalEquation.prod_determinant_sq", "AlgebraicGeometry.weilSign_eq_one_or_eq_neg_one", "AlgebraicGeometry.WeilFunctionalEquation.alternatingProdEval_eq_prod_determinant", "AlgebraicGeometry.WeilFunctionalEquation.alternatingProdEval_eq"]
order = 4160
tags = ["latex:proposition"]
uses = ["def-weil-determinant-constants", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-functional-equation-sign", "def-weil-geometric-hypotheses", "def-weil-integral-frobenius-factor", "def-weil-ordinary-compact-cohomology", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "prop-duality-reciprocity", "prop-trace-determinant"]
+++
Let $p$ be prime, let $a\in\mathbf Z_{\geq1}$, put $q=p^a$, and set
$k_0=\Fq$; let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Fix a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, and fix an
indeterminate $T$. For $P(T)=\sum_r c_rT^r\in\mathbf Z[T]$, write
$P^{(\ell)}(T)=\sum_r(c_r\cdot1_{\Ql})T^r$ for coefficientwise extension.
Let $X_0/k_0$ be a
smooth, proper and geometrically connected scheme of pure dimension
$d\in\mathbf Z_{\geq0}$; put $X=X_0\times_{k_0}k$. Let $F$ be
geometric Frobenius. For every integer $i$
with $0\leq i\leq2d$, put

$$
V_{i,\ell}=H^i(X,\Ql),
\qquad
F_{i,\ell}=F\vert_{V_{i,\ell}},
\qquad
P_{i,\ell}(T)=\det(1-TF_{i,\ell}\mid V_{i,\ell}).
$$

Here $H^i(X,\Ql)$ is the
ordinary cohomology group.
These data form the
smooth-proper
cohomological family. Let $P_i(T)\in\mathbf Z[T]$ be the
integral Frobenius factor
with $P_i(0)=1$ and $P_i^{(\ell)}=P_{i,\ell}$. Put
$b_i=\deg P_i$ and define the
determinant constant
$D_i=(-1)^{b_i}[T^{b_i}]P_i(T)$. Define

$$
\chi=\sum_{i=0}^{2d}(-1)^ib_i,
\qquad
\Delta=\prod_{i=0}^{2d}D_i^{(-1)^i},
\qquad
\varepsilon=(-1)^\chi q^{-d\chi/2}\Delta.
$$

Thus $\varepsilon$ is the
normalized functional-equation
sign. Define the point-count zeta
series by

$$
Z(X_0,T)=\exp\left(\sum_{n\geq1}
\#X_0(\mathbf F_{q^n})\frac{T^n}{n}\right).
$$

The alternating determinant scalar satisfies

$$
\Delta^2=q^{d\chi}.
$$

The normalized sign satisfies

$$
\varepsilon^2=1,\qquad \varepsilon\in\{1,-1\},
$$

and the zeta function satisfies

$$
Z(X_0,q^{-d}T^{-1})
=\varepsilon q^{d\chi/2}T^\chi Z(X_0,T)
\quad\text{in }\mathbf Q(T).
$$

Equivalently, the determinant-constant form of the functional equation is

$$
Z(X_0,q^{-d}T^{-1})
=(-1)^\chi T^\chi
\left(\prod_{i=0}^{2d}D_i^{(-1)^i}\right)Z(X_0,T).
$$
