+++
id = "thm-zla-degreewise-reciprocal"
kind = "theorem"
title = "Degreewise reciprocal-polynomial identities"
order = 1033
uses = ["def-zla-recip-charpoly", "def-zla-similitude-pairing", "prop-zla-reciprocal-eigenvalue-pairing"]
+++
Let $B:V\times W\to E$ be a perfect similitude pairing of multiplier $\mu$ for
the automorphisms $F_V,F_W$. Put $b=\dim_EV=\dim_EW$ and
$D_V=\det(F_V)$, and set

$$
P_V(T)=\det(1-TF_V\mid V),
\qquad
P_W(T)=\det(1-TF_W\mid W).
$$

Then, in $E[T,T^{-1}]$,

$$
P_W(\mu^{-1}T^{-1})=(-1)^bT^{-b}D_V^{-1}P_V(T),
$$

or equivalently

$$
P_W(T)=(-1)^b\mu^bD_V^{-1}T^bP_V(\mu^{-1}T^{-1}).
$$

## Proof

Over an algebraic closure, $P_V(T)=\prod_{j=1}^b(1-\alpha_jT)$ with the
$\alpha_j$ the eigenvalues of $F_V$, all nonzero, and
$D_V=\prod_j\alpha_j$. By
[prop-zla-reciprocal-eigenvalue-pairing],
$P_W(T)=\prod_j(1-\mu\alpha_j^{-1}T)$. Substituting $T\mapsto\mu^{-1}T^{-1}$
and clearing $\prod_j(-\alpha_j^{-1}T^{-1})$ from the product gives the first
identity; both sides have coefficients in $E$, so the identity descends from
$\Omega[T,T^{-1}]$ to $E[T,T^{-1}]$. The second form follows by substituting
$T\mapsto\mu^{-1}T^{-1}$ once more.
