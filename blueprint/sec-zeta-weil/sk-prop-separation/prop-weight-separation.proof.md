+++
kind  = "proof"
of    = "prop-weight-separation"
+++
Let $\beta\in\Qlb$ be a common ordinary root of $P_{i,\ell}$ and
$P_{j,\ell}$ with $i\ne j$. Then $\alpha=\beta^{-1}$ is a
reciprocal root of both polynomials in the sense of
[def-weil-ordinary-reciprocal-roots], so the assumed absolute
value condition gives $|\iota(\alpha)|=q^{i/2}=q^{j/2}$, hence
$i=j$, a contradiction. Thus distinct $P_{i,\ell}$ have no common
ordinary root, and since every $P_{i,\ell}$ has constant coefficient
one, they are coprime in $\Qlb[T]$; consequently the parity products
$N_\ell,D_\ell$ of [def-weil-parity-products] are coprime and
have constant coefficient one. The assumed trace-to-determinant
identity for the point-count zeta series of
[def-weil-point-counts-zeta],

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}},
$$

groups the odd-degree factors into $N_\ell(T)$ and the even-degree
factors into $D_\ell(T)$, giving $Z(X_0,T)=N_\ell(T)/D_\ell(T)$
after coefficient extension to $\Ql[[T]]$. Every ordinary root of
$N_\ell$ is an ordinary root of exactly one $P_{j,\ell}$ with $j$
odd, and its reciprocal satisfies the assumed absolute value condition
with weight $j$; hence the submultiset of ordinary roots of $N_\ell$
whose reciprocal satisfies $|\iota(\alpha)|=q^{i/2}$ is exactly the
ordinary root multiset of $P_{i,\ell}$ for $i$ odd, and the
corresponding assertion with $D_\ell$ holds for $i$ even, which is the
asserted more precise multiset identification.
