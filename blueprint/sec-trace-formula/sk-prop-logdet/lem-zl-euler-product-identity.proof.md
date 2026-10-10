+++
kind  = "proof"
of    = "lem-zl-euler-product-identity"
+++
By [lem-zl-log-det-identity],

$$
\log\det(1-TF\mid V)=-\sum_{n\geq1}N_n\frac{T^n}{n}.
$$

The exponential of a series in $T\Qlb[[T]]$ lies in
$1+T\Qlb[[T]]$, the determinant has constant coefficient $1$ and
hence a multiplicative inverse in $\Qlb[[T]]$, and on these two sets
the formal exponential and the formal logarithm are mutually inverse
bijections. Exponentiating the displayed identity therefore gives

$$
\exp\left(\sum_{n\geq1}N_n\frac{T^n}{n}\right)
=\exp\bigl(-\log\det(1-TF\mid V)\bigr)
=\det(1-TF\mid V)^{-1}.
$$
