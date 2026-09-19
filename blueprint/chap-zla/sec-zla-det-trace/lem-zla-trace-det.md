+++
id = "lem-zla-trace-det"
kind = "lemma"
title = "Finite-dimensional trace–determinant identity"
order = 990
uses = ["def-zla-recip-charpoly"]
+++
Let $V$ be a finite-dimensional $E$-vector space and let
$u\in\operatorname{End}_E(V)$. Then

$$
P_{V,u}(T)^{-1}
=\operatorname{Exp}\left(\sum_{n\geq1}\Tr(u^n\mid V)\frac{T^n}{n}\right)
\qquad\text{in }E[[T]],
$$

the inverse on the left being taken in $E[[T]]$, which is legitimate because
$P_{V,u}(0)=1$. Equivalently,

$$
T\frac{d}{dT}\operatorname{Log}P_{V,u}(T)^{-1}
=\sum_{n\geq1}\Tr(u^n\mid V)T^n.
$$

No semisimplicity assumption is imposed on $u$.

## Proof

Differentiating a determinant gives the matrix identity
$\frac{d}{dT}\det(1-Tu)=-\det(1-Tu)\Tr\!\left((1-Tu)^{-1}u\right)$ in
$E[[T]]$, where the formal resolvent is
$(1-Tu)^{-1}=\sum_{n\geq0}T^nu^n$; taking the trace coefficientwise turns the
right-hand side into $-\det(1-Tu)\sum_{n\geq1}\Tr(u^n)T^{n-1}$. Both sides of
the asserted identity therefore have constant coefficient $1$ and the same
logarithmic derivative, and over a $\mathbf Q$-algebra a power series is
determined by its constant coefficient and its derivative.
