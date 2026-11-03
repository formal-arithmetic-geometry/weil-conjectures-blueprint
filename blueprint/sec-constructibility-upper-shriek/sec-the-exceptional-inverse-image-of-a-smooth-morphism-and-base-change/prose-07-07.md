+++
id = "prose-07-07"
kind = "hidden"
title = "The exceptional inverse image of a smooth morphism and base change"
order = 334
+++
The adjunction for the projective line computes $p^!$ for
$p:\mathbf P^1_S\to S$, and we now extend the computation to smooth
morphisms. The reason is the proof of generic constructibility below.
There we need $Rf_*L$ for a smooth $f$ and a locally constant sheaf $L$,
about which nothing is known directly, while $Rf_!$ is under control by
the finiteness theorem and proper base change. The bridge is the formula
$f^!N\simeq f^*N\otimes^{\mathbf L}\omega_f$ with $\omega_f$ locally
$\Lambda(d)[2d]$ (Proposition [sk-prop-cohsm]). With it, the
adjunction $Rf_!\dashv f^!$ becomes a duality between $Rf_*L$ and
$Rf_!$ of the twisted dual of $L$ (Lemma [sk-lem-geo-smooth-generic]),
just as Poincaré duality on a manifold exchanges ordinary and compactly
supported cohomology. For $f:\mathbf G_m\to\operatorname{Spec}\bar k$ and
$L=\Lambda=\Fell$, the exercise above shows that
$R\Gamma_c(\mathbf G_m,\Lambda(1)[2])$ has cohomology $\Lambda(1)$ in degree
$-1$ and $\Lambda$ in degree $0$. Its dual has $\Lambda$ in degree $0$ and
$\Lambda(-1)$ in degree $1$, and this is indeed $R\Gamma(\mathbf G_m,\Lambda)$,
with $H^1=\Lambda(-1)$ given by the Kummer torsors.

The duality must also commute with base change, and for this we need
the base change isomorphism $g'^*f^!\simeq f'^!g^*$ for smooth $f$. For this the
local form $\omega_f|_U\simeq\Lambda_U(d)[2d]$ on charts suffices; a global
identification of $\omega_f$ with $\Lambda_X(d)[2d]$ needs a trace map for
$f$ and is part of smooth purity (Section [sec-smooth-purity]). Zariski locally on $X$ and $S$, a
smooth morphism $f:X\to S$ factors as an étale morphism to some
$\mathbf A^d_S$ followed by the projection to $S$, and so we first treat
these two kinds of morphisms.
