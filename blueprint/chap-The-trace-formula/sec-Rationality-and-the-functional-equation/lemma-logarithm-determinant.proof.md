+++
kind = "proof"
of = "lemma-logarithm-determinant"
order = 1034
+++
For a single eigenvalue $\alpha$ the identity is
$-\log(1-\alpha T)=\sum_m\alpha^mT^m/m$, and the general case could be
reduced to this by triangularizing $v$ over an algebraic closure. Instead we use logarithmic derivatives, which allows us to stay over $L$.
In $L[[T]]$, the matrix $1-Tv$ is invertible, with inverse
$\sum_{r\geq0}T^rv^r$. Moreover, the logarithmic derivative of the determinant of an invertible matrix $M$ over $L[[T]]$ is
$\operatorname{Tr}(M^{-1}M')$, and hence

$$
\frac{d}{dT}\log\det(1-Tv)
=-\operatorname{Tr}\bigl(v(1-Tv)^{-1}\bigr)
=-\sum_{m\geq1}\operatorname{Tr}(v^m)T^{m-1}.
$$

Since both logarithms have constant coefficient zero and $L$ has
characteristic zero, we may integrate and exponentiate, and we obtain
(12.5). For a perfect complex, the categorical trace
over a field is the alternating sum of the traces on the finitely many
nonzero cohomology spaces (Proposition [proposition-properties-trace]), and the
assertion follows by multiplying the identities for the $H^i(P)$.
