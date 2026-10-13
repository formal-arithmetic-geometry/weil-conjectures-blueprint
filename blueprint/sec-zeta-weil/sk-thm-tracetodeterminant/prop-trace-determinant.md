+++
id = "prop-trace-determinant"
kind = "theorem"
title = "Trace-to-determinant factorization"
order = 3227
tags = ["latex:proposition"]
uses = ["def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-ordinary-compact-cohomology", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "prop-every-iterate-trace"]
+++
Let $K$ be a characteristic-zero field, fix an indeterminate $T$, let
$I\subset\mathbf Z$ be finite, and let
$(V_i,u_i)_{i\in I}$ be a finite graded family of finite-dimensional vector
spaces and endomorphisms over $K$. Put

$$
P_i(T)=\det(1-Tu_i\mid V_i),
\qquad
\Delta(T)=\prod_iP_i(T)^{(-1)^{i+1}}.
$$

Then, for every $i\in I$,

$$
-\log P_i(T)=
\sum_{n\geq1}\Tr(u_i^n\mid V_i)\frac{T^n}{n},
$$

and, with the displayed parity signs,

$$
\log\Delta(T)=
\sum_{n\geq1}\left(\sum_{i\in I}(-1)^i\Tr(u_i^n\mid V_i)\right)
\frac{T^n}{n}.
$$

For the geometric application, let $d\in\mathbf Z_{\geq0}$, take
$I=\{0,\ldots,2d\}$, and use the
finite-field datum; fix a prime
$p$, an integer $a\geq1$, put $q=p^a$, and set
$k_0=\Fq$, and let $k=\Fbar$ be the fixed algebraic closure of $k_0$.
Choose a prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, and let
$X_0/k_0$ be smooth, proper,
geometrically connected of pure dimension $d\in\mathbf Z_{\geq0}$. Put
$X=X_0\times_{k_0}k$, $V_i=H^i(X,\Ql)$, and $u_i=F_{i,\ell}$, where
$(V_{i,\ell},F_{i,\ell})$ is the
smooth-proper
cohomological family. The
point-count and zeta series and the
ordinary cohomology
construction give, after coefficient extension
$\mathbf Q[[T]]\to\Ql[[T]]$, the identity

$$
Z(X_0,T)=
\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}.
$$

This identity belongs to $\Ql(T)\cap\Ql[[T]]$.
