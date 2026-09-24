+++
id = "def-zl-frobenius-trace-series"
kind = "definition"
title = "Frobenius trace series"
order = 4337
uses = ["def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-smooth-proper-cohomological-family", "def-weil-weil-sheaf-complex"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$ and choose an algebraic closure $\Qlb$ of $\Ql$.
A *Frobenius module* is a pair $(V,F)$ consisting of a
finite-dimensional $\Qlb$-vector space $V$ and a $\Qlb$-linear
automorphism $F:V\to V$, in the sense of the
finite-dimensional
Frobenius-module convention of the framework chapter. For such a pair, define its
*trace series*

$$
\operatorname{tr}_F(T)
=\sum_{n\geq1}\Tr(F^n\mid V)\frac{T^n}{n}
\in T\Qlb[[T]].
$$

In the geometric situation, let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, let $(\Qlb)_X$ be the constant
Weil sheaf, and let $F$ be the
global geometric Frobenius
on $H^i(X,\Qlb)$ in the geometric-Frobenius
convention; for every $0\leq i\leq2d$ the pair
$(H^i(X,\Qlb),F|_{H^i})$ is a Frobenius module, the trace series of the
pair being the degree-$i$ trace series obtained from the
smooth-proper
cohomological family by scalar extension. The *alternating trace
series* of the family is

$$
\operatorname{str}_F(T)
=\sum_{n\geq1}\left(\sum_{i=0}^{2d}(-1)^i
\Tr\bigl(F^n\mid H^i(X,\Qlb)\bigr)\right)\frac{T^n}{n}.
$$
