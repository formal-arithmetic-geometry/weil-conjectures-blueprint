+++
id = "prop-weight-separation"
kind = "theorem"
title = "Weight separation"
lean = ["AlgebraicGeometry.Scheme.isCoprime_frobeniusCharpolyRev", "AlgebraicGeometry.Scheme.isCoprime_oddFrobeniusProduct_evenFrobeniusProduct", "AlgebraicGeometry.Scheme.coeff_zero_oddFrobeniusProduct", "AlgebraicGeometry.Scheme.coeff_zero_evenFrobeniusProduct", "AlgebraicGeometry.Scheme.roots_map_frobeniusCharpolyRev_eq_filter"]
order = 4130
tags = ["latex:proposition"]
uses = ["def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-ordinary-reciprocal-roots", "def-weil-parity-products", "def-weil-point-counts-zeta", "def-weil-punctual-weights", "def-weil-smooth-proper-cohomological-family"]
+++
Fix a prime $p$, an integer $a\in\mathbf Z_{\geq1}$, put $q=p^a$,
$k_0=\Fq$, and let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Fix a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, choose an algebraic
closure $\Qlb$ of $\Ql$, and fix a field embedding
$\iota:\Qlb\hookrightarrow\mathbf C$ and an indeterminate $T$. Let
$X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension
$d\in\mathbf Z_{\geq0}$, put $X=X_0\times_{k_0}k$, and let
$(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family.
Interpret ordinary and reciprocal roots by the
root convention, and use the
absolute-value weight condition. Assume
that, for every integer $i$ with $0\leq i\leq2d$, every reciprocal root
$\alpha$ of $P_{i,\ell}$ satisfies

$$
|\iota(\alpha)|=q^{i/2}.
$$

Let $Z(X_0,T)$ be the
point-count zeta series. Assume the
trace-to-determinant identity

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}
\quad\text{in }\Ql(T).
$$

For all integers $0\leq i,j\leq2d$ with
$i\neq j$, the polynomials $P_{i,\ell}$ and $P_{j,\ell}$ have no common
ordinary root in $\Qlb$ and are coprime in $\Qlb[T]$. Define the
odd and even parity products by

$$
N_\ell(T)=\prod_{\substack{0\leq i\leq2d\\ i\text{ odd}}}
P_{i,\ell}(T),
\qquad
D_\ell(T)=\prod_{\substack{0\leq i\leq2d\\ i\text{ even}}}
P_{i,\ell}(T).
$$

They are coprime, have constant coefficient $1$, and the
Hasse–Weil zeta series satisfies

$$
Z(X_0,T)=\frac{N_\ell(T)}{D_\ell(T)}
$$

after coefficient extension to $\Ql[[T]]$. More precisely, the ordinary
root multiset of each $P_{i,\ell}$ is exactly the submultiset of roots of
the appropriate parity product whose reciprocal $\alpha$ satisfies

$$
|\iota(\alpha)|=q^{i/2}
$$

for the fixed field embedding
$\iota:\Qlb\hookrightarrow\mathbf C$.
