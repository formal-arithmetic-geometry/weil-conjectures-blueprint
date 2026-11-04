+++
id = "prose-06-09"
kind = "hidden"
title = "Smooth morphisms (1)"
order = 550
+++
Let $f:X\to S$ be smooth of relative dimension $d$. Extending the formula
$p^!=p^*(1)[2]$ for $p:\mathbf P^1_S\to S$, we show in
Proposition [proposition-exceptional-inverse-image-smooth-morphism] that
$f^!N\simeq f^*N\otimes^{\mathbf L}\omega_f$ with $\omega_f$ locally
isomorphic to $\Lambda(d)[2d]$. The proof of generic constructibility
below needs this formula. It must control $Rf_*L$ for a locally constant
sheaf $L$, and we know nothing about $Rf_*L$ directly, whereas the
finiteness theorem and proper base change control $Rf_!$. With the
formula, the adjunction $Rf_!\dashv f^!$ becomes a duality between
$Rf_*L$ and $Rf_!$ of the twisted dual of $L$
(Lemma [lemma-smooth-morphisms-locally-constant-sheaves]). On a manifold, Poincaré duality
exchanges ordinary and compactly supported cohomology in the same way.

For example, let $f:\mathbf G_m\to\operatorname{Spec}\bar k$ and
$L=\Lambda=\Fell$. The localization triangle for the origin of
$\mathbf A^1$ and $R\Gamma_c(\mathbf A^1_{\bar k},\Lambda)\simeq\Lambda(-1)[-2]$
give $R\Gamma_c(\mathbf G_m,\Lambda)\simeq\fib\bigl(\Lambda(-1)[-2]\to\Lambda\bigr)$.
Hence $H^1_c=\Lambda$ and $H^2_c=\Lambda(-1)$ are the only nonzero groups, and
$R\Gamma_c(\mathbf G_m,\Lambda(1)[2])$ has cohomology $\Lambda(1)$ in degree
$-1$ and $\Lambda$ in degree $0$. Its dual has $\Lambda$ in degree $0$ and
$\Lambda(-1)$ in degree $1$. This is indeed $R\Gamma(\mathbf G_m,\Lambda)$,
with $H^1=\Lambda(-1)$ given by the Kummer torsors.

The duality must also commute with base change. This requires the base
change isomorphism $g'^*f^!\simeq f'^!g^*$ for smooth $f$, and for it the
local form $\omega_f|_U\simeq\Lambda_U(d)[2d]$ on charts suffices. A
global identification of $\omega_f$ with $\Lambda_X(d)[2d]$ needs a trace
map for $f$; it is part of smooth purity
(Section [chap-Smooth-purity]). Zariski locally on $X$ and $S$, a
smooth morphism $f:X\to S$ factors as an étale morphism to some
$\mathbf A^d_S$ followed by the projection to $S$. The next lemma treats
these two kinds of morphisms.
