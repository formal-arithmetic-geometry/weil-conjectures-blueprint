+++
id = "prop-duality-reciprocity"
kind = "theorem"
title = "Duality reciprocity"
lean = ["AlgebraicGeometry.Scheme.duality_reciprocity"]
order = 3547
tags = ["latex:proposition"]
uses = ["def-coefficient-twists-detailed", "def-weil-betti-numbers", "def-weil-determinant-constants", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-integral-frobenius-factor", "def-weil-ordinary-compact-cohomology", "def-weil-poincare-trace-cup", "def-weil-smooth-proper-cohomological-family", "lem-weil-alternating-form-dimension", "prop-poincare-pairing", "thm-pod-degreewise-perfectness-over-a-field", "cor-pod-reciprocal-eigenvalues"]
+++
Let $p$ be prime, let $a\in\mathbf Z_{\geq1}$, put $q=p^a$, and set
$k_0=\Fq$; let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Fix a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, and for
$P(T)=\sum_r c_rT^r\in\mathbf Z[T]$ write
$P^{(\ell)}(T)=\sum_r(c_r\cdot1_{\Ql})T^r$ for coefficientwise extension.
Let
$X_0/k_0$ be smooth,
proper, and geometrically connected of pure dimension
$d\in\mathbf Z_{\geq0}$, let $X=X_0\times_{k_0}k$, and let $F$ be the
geometric Frobenius. Fix an indeterminate
$T$. For every integer $i$ with $0\leq i\leq2d$, put
$V_{i,\ell}=H^i(X,\Ql)$, where $H^i(X,\Ql)$ denotes the
ordinary cohomology group,
and set $P_{i,\ell}(T)=\det(1-TF\mid V_{i,\ell})$. Let
$P_i(T)\in\mathbf Z[T]$ be the
normalized integral factor
with $P_i^{(\ell)}=P_{i,\ell}$; these determinant data are the
smooth-proper
cohomological family. Put
$b_i=\deg P_i$, and set

$$
D_i=(-1)^{b_i}[T^{b_i}]P_i(T).
$$

Let $\langle-,-\rangle_i$ be the
trace–cup-product pairing. Poincare
duality identifies
the multiset of
Frobenius eigenvalues in degree $2d-i$ with

$$
\left\{\frac{q^d}{\alpha}:\alpha
\text{ is an eigenvalue in degree }i\right\},
$$

including algebraic multiplicity. Moreover,

$$
b_i=b_{2d-i},
\qquad
D_iD_{2d-i}=q^{db_i},
$$

and the integral factors satisfy the Laurent-polynomial identity

$$
P_{2d-i}(q^{-d}T^{-1})
=(-1)^{b_i}T^{-b_i}D_i^{-1}P_i(T)
\quad\text{in }\mathbf Q[T,T^{-1}].
$$

For the middle degree $i=d$, the pairing is $(-1)^d$-symmetric. In particular,
if $d$ is odd, then $b_d$ is even.
