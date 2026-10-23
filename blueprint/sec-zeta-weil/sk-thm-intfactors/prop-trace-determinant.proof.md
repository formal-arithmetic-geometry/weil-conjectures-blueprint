+++
kind  = "proof"
of    = "prop-trace-determinant"
+++
Over an algebraic closure of $K$, let
$\lambda_{i,1},\ldots,\lambda_{i,n_i}$ denote the eigenvalues of
$u_i$, counted with algebraic multiplicity, where
$n_i=\dim_KV_i$. Then $P_i(T)=\prod_j(1-\lambda_{i,j}T)$ and, in the
ring of formal power series,

$$
-\log P_i(T)
=\sum_j\sum_{n\geq1}\lambda_{i,j}^n\frac{T^n}{n}
=\sum_{n\geq1}\operatorname{Tr}_K(u_i^n\mid V_i)\frac{T^n}{n},
$$

the last equality because the trace is the sum of the eigenvalues after
scalar extension. Summing over $i$ with the parity signs in
$\Delta(T)=\prod_iP_i(T)^{(-1)^{i+1}}$ gives

$$
\log\Delta(T)=\sum_{n\geq1}\Bigl(\sum_{i\in I}(-1)^i
\operatorname{Tr}_K(u_i^n\mid V_i)\Bigr)\frac{T^n}{n},
$$

which proves the linear-algebra part of the statement.

For the geometric application, $Z(X_0,T)$ is the point-count zeta
series of [def-weil-point-counts-zeta], and by
[prop-every-iterate-trace] applied to the constant Weil sheaf on
the smooth proper geometrically connected $X_0$,

$$
N_n(X_0)=\sum_{i=0}^{2d}(-1)^i
\operatorname{Tr}_{\Ql}(F_{i,\ell}^n\mid V_{i,\ell})
$$

for every $n\geq1$, where $(V_{i,\ell},F_{i,\ell})$ is the
smooth-proper cohomological family of
[def-weil-smooth-proper-cohomological-family]. Hence
$\log Z(X_0,T)$ equals the logarithm of
$\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}$ after the coefficient
extension $\mathbf Q[[T]]\to\Ql[[T]]$, and exponentiating gives the
displayed identity. Both sides are Taylor expansions of rational
functions, so the identity belongs to
$\Ql(T)\cap\Ql[[T]]$.
