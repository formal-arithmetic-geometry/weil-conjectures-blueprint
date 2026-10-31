+++
kind = "proof"
of = "sk-prop-logdet"
uses = ["sk-p-trace", "sk-p-linear-triangular", "sk-def-frobmod"]
+++
In $L[[T]]$, the matrix $1-Tv$ is invertible, with inverse
$\sum_{r\geq0}T^rv^r$. The logarithmic derivative of the
determinant of an invertible matrix $M$ over $L[[T]]$ is
$\operatorname{Tr}(M^{-1}M')$, and hence

$$
\frac{d}{dT}\log\det(1-Tv)
=-\operatorname{Tr}\bigl(v(1-Tv)^{-1}\bigr)
=-\sum_{m\geq1}\operatorname{Tr}(v^m)T^{m-1}.
$$

Both logarithms have constant coefficient zero, and $L$ has
characteristic zero, so integrating and exponentiating gives
(13.5). For a perfect complex, the categorical trace
over a field is the alternating sum of the traces on the finitely many
nonzero cohomology spaces (Proposition [sk-p-trace]), and the
assertion follows by multiplying the identities for the $H^i(P)$.
