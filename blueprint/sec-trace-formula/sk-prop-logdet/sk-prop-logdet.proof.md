+++
kind = "proof"
of = "sk-prop-logdet"
uses = ["sk-p-trace", "sk-p-linear-triangular", "sk-def-frobmod"]
+++
In $L[[T]]$ the matrix $1-Tv$ is invertible, with inverse
$\sum_{r\geq0}T^rv^r$. The logarithmic derivative of the
determinant of an invertible matrix $M$ over $L[[T]]$ is
$\operatorname{Tr}(M^{-1}M')$, so

$$
 \frac{d}{dT}\log\det(1-Tv)
   =-\operatorname{Tr}\bigl(v(1-Tv)^{-1}\bigr)
   =-\sum_{m\geq1}\operatorname{Tr}(v^m)T^{m-1}.
$$

Both logarithms have constant coefficient zero, and $L$ has
characteristic zero; integrating and exponentiating gives
(1). For a perfect complex, the categorical trace
over a field is the alternating sum of the traces on the finitely many
nonzero cohomology spaces ([sk-p-trace]), and the
assertion follows by multiplying the identities for the $H^i(P)$.

*Complement.* The formal exponential and logarithm are mutually inverse
between $TL[[T]]$ and $1+TL[[T]]$, so (1) is equivalent to the logarithmic
form. Alternatively, over an algebraic closure $\bar L$ of $L$ put $v$ in upper
triangular form ([sk-p-linear-triangular]) with diagonal
$(\lambda_1,\dots,\lambda_r)$. Then
$\operatorname{Tr}(v^{m}\mid V)=\sum_j\lambda_j^{m}$ and
$\det(1-Tv\mid V)=\prod_j(1-\lambda_jT)$; the formal logarithm is additive on
$1+T\bar L[[T]]$ (compare derivatives), and
$\log(1-\lambda T)=-\sum_{m\ge1}\lambda^{m}T^{m}/m$, so summing over the finite
index range gives the logarithmic form. No semisimplicity is used. For a
Frobenius module, $\operatorname{tr}_F(T)$ of [sk-def-frobmod] is the series
on the right, with $L=\overline{\mathbf Q}_\ell$.
