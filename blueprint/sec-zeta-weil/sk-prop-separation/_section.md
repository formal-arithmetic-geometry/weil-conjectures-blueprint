+++
id = "sk-prop-separation"
kind = "proposition"
title = "Weight separation and the parity factorization"
order = 2898
lean = ["Polynomial.isCoprime_prod_odd_prod_even", "Polynomial.prod_odd_eq_map_and_prod_even_eq_map"]
uses = ["sk-def-cohfamily", "sk-def-roots", "sk-prop-rootpurity", "sk-thm-tracetodeterminant"]
tags = ["sketch"]
+++
Assume [sk-prop-rootpurity]. Then for $i\ne j$ the polynomials
$P_{i,\ell}$ and $P_{j,\ell}$ are coprime in $\Qlb[T]$, and with the parity
products

$$
N_\ell(T)=\prod_{i\ \text{odd}}P_{i,\ell}(T),\qquad
D_\ell(T)=\prod_{i\ \text{even}}P_{i,\ell}(T)
$$

one has $\gcd(N_\ell,D_\ell)=1$, $N_\ell(0)=D_\ell(0)=1$, and

$$
Z(X_0,T)=\frac{N_\ell(T)}{D_\ell(T)}
\qquad\text{after coefficient extension to }\Ql[[T]] .
$$

More precisely, the ordinary-root multiset of each $P_{i,\ell}$ is exactly the
submultiset of roots of the appropriate parity product whose reciprocal
$\alpha$ satisfies $|\iota(\alpha)|=q^{i/2}$ for the fixed $\iota$.
