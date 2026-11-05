+++
id = "prose-06-09"
kind = "hidden"
title = "Smooth morphisms (1)"
order = 556
+++
Let $f:X\to S$ be smooth of relative dimension $d$. Extending the formula
$p^!=p^*(1)[2]$ for $p:\mathbf P^1_S\to S$, we show in
Proposition [proposition-exceptional-inverse-image-smooth-morphism] that
$f^!N\simeq f^*N\otimes^{\mathbf L}\omega_f$ with $\omega_f$ locally
isomorphic to $A(d)[2d]$. We need this formula in the proof of generic constructibility below, because
it must control $Rf_*L$ for a locally constant sheaf $L$. Indeed, we know nothing about $Rf_*L$ directly, whereas the finiteness theorem and proper base change control $Rf_!$. With the formula, however, the adjunction $Rf_!\dashv f^!$ becomes a duality between
$Rf_*L$ and $Rf_!$ of the twisted dual of $L$
(Lemma [lemma-smooth-morphisms-locally-constant-sheaves]). On a manifold, Poincaré duality exchanges ordinary and compactly supported cohomology in the same way.

For example, let $f:\mathbf G_m\to\operatorname{Spec}\bar k$ and
$L=A=\Fell$. The localization triangle for the origin of
$\mathbf A^1$ and $R\Gamma_c(\mathbf A^1_{\bar k},A)\simeq A(-1)[-2]$
give $R\Gamma_c(\mathbf G_m,A)\simeq\fib\bigl(A(-1)[-2]\to A\bigr)$.
Hence $H^1_c=A$ and $H^2_c=A(-1)$ are the only nonzero groups, and
$R\Gamma_c(\mathbf G_m,A(1)[2])$ has cohomology $A(1)$ in degree
$-1$ and $A$ in degree $0$. Its dual has $A$ in degree $0$ and
$A(-1)$ in degree $1$. This is indeed $R\Gamma(\mathbf G_m,A)$,
with $H^1=A(-1)$ given by the Kummer torsors.

The duality must also commute with base change. This requires the base
change isomorphism $g'^*f^!\simeq f'^!g^*$ for smooth $f$, and for it the
local form $\omega_f|_U\simeq A_U(d)[2d]$ on charts suffices. A global identification of $\omega_f$ with $A_X(d)[2d]$, by contrast, needs a trace map for $f$; it is part of smooth purity
(Section [chap-Smooth-purity]). For the local form we use that, Zariski locally on $X$ and $S$, a smooth morphism $f:X\to S$ factors as an étale morphism to some
$\mathbf A^d_S$ followed by the projection to $S$, and the next lemma treats these two kinds of morphisms.
