+++
kind  = "proof"
of    = "sk-prop-logdet"
+++
Over the algebraically closed field $\Qlb$ put $F$ in upper triangular form
with diagonal $(\lambda_1,\dots,\lambda_m)$. Then
$\Tr(F^{n}\mid V)=\sum_j\lambda_j^{n}$ and
$\det(1-TF\mid V)=\prod_j(1-\lambda_jT)$. The formal logarithm is additive on
$1+T\Qlb[[T]]$ (compare derivatives), and
$\log(1-\lambda T)=-\sum_{n\ge1}\lambda^{n}T^{n}/n$; summing over the finite
index range gives the identity. Exponentiating, and using that the formal
exponential and logarithm are mutually inverse between $T\Qlb[[T]]$ and
$1+T\Qlb[[T]]$, gives the second form. No semisimplicity is used: the
computation is triangular and therefore valid for arbitrary $F$.
