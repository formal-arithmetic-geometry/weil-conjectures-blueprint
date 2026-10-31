+++
id = "prose-11-01"
kind = "hidden"
title = "Verdier and Poincaré duality"
order = 499
+++
Weil's axiom (c) asks that for a smooth proper variety of dimension
$d$ the cup product pair $H^i$ with $H^{2d-i}$ perfectly, in such a way
that the Frobenius eigenvalues $\alpha$ in degree $i$ correspond to the
eigenvalues $q^d/\alpha$ in degree $2d-i$. For a compact oriented
manifold $M$ of dimension $n$ this is Poincaré duality, and Verdier
explained it as a statement about sheaves: if $a:M\to\mathrm{pt}$ is the
map to a point, then $\omega_M=a^!\mathbf Z$ is the orientation sheaf
placed in degree $-n$, the functor $\mathbb D=\cHom(-,\omega_M)$ is an
involution on constructible complexes, and
$R\Gamma(M,\mathbb DK)\simeq R\!\operatorname{Hom}(R\Gamma_c(M,K),\mathbf Z)$. We
follow the same route.

For a scheme $X$ with structure map $a_X:X\to s=\operatorname{Spec}k$,
put $\omega_X=a_X^!\Lambda_s$ and $\mathbb D_X=\cHom(-,\omega_X)$
(Definition [sk-def-ops]). The adjunction $Ra_{X!}\dashv a_X^!$
already gives a pairing: evaluation
$K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$ followed by the counit
$R\Gamma_c(X,\omega_X)\to\Lambda$ pairs $R\Gamma_c(X,K)$ with
$R\Gamma(X,\mathbb D_XK)$. The same adjunctions give, without further
work, two exchange formulas

$$
\mathbb D_YRf_!\simeq Rf_*\mathbb D_X,\qquad
f^!\mathbb D_Y\simeq\mathbb D_Xf^*
$$

(Lemma [sk-thm-sf-tensor-hom]). Nothing formal makes the pairing
perfect. What does is Verdier biduality: the double-dual map
$K\to\mathbb D_X\mathbb D_XK$ is an isomorphism for every
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and every admissible $\Lambda$
(Theorem [sk-thm-pd-verdier-duality]). Once $\mathbb D_X$ is an
anti-equivalence, applying the two formulas to $\mathbb D_XK$ gives the
other two, $\mathbb D_YRf_*\simeq Rf_!\mathbb D_X$ and
$\mathbb D_Xf^!\simeq f^*\mathbb D_Y$
(Corollary [sk-thm-sf-verdier-exchange]). Over an algebraically closed
field the first exchange formula for $a_X$ is global duality,
$R\Gamma(X,\mathbb D_XK)\simeq R\!\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda)$
(Theorem [sk-thm-sf-global-duality]). For smooth $X$ of pure dimension $d$,
smooth purity identifies $\omega_X$ with $\Lambda_X(d)[2d]$, and global
duality becomes Poincaré duality: the pairing

$$
R\Gamma_c(X,K)\otimes^{\mathbf L}R\Gamma(X,K^\vee(d))[2d]
\longrightarrow\Lambda,\qquad K^\vee=\cHom(K,\Lambda_X),
$$

built from evaluation and the trace map, is perfect
(Theorem [sk-thm-sf-identification]). For a field $\Lambda$ and $X$ smooth,
proper and connected, the trace in top degree is an isomorphism
$H^{2d}(X,\Lambda)\simeq\Lambda(-d)$ sending the class of a point to
$1$ (Theorem [sk-cor-trace]), and we obtain the perfect cup product
pairing between $H^i$ and $H^{2d-i}$, symmetric up to the sign $(-1)^i$
(Corollary [sk-cor-pd-cup-product]).

The proof of biduality is an induction on dimension, and it is indirect
for a reason. A constructible complex is built from locally constant
pieces $t_!P$ on smooth strata $t:T\hookrightarrow X$, and on a smooth
stratum biduality for $P$ is clear from smooth purity. But
$\mathbb D_X(t_!P)\simeq Rt_*\mathbb D_TP$, and to dualize once more we
would need $\mathbb D_XRt_*\simeq t_!\mathbb D_T$, which is itself a
consequence of biduality. Instead we control the
cone $Q$ of $K\to\mathbb D_X\mathbb D_XK$ point by point. At a
nonclosed point $x$ we choose a function $t$ on a neighbourhood that is
transcendental at $x$; on the geometric generic fibre of
$t:U\to\mathbf A^1_k$, which has smaller dimension, duality commutes with
restriction up to the twist $(1)[2]$ (Lemma [sk-lem-pd-generic-restriction]),
and the induction hypothesis kills the stalks of $Q$ above $x$. Hence
$Q$ is supported on finitely many closed points. After a reduction
to proper $X$, the exchange formula for $a_X$ identifies $R\Gamma(X,Q)$
with the cone of biduality for the perfect complex $R\Gamma(X,K)$, which
is zero, and global sections of a complex supported on finitely many
points are the sum of its stalks. This is the reason we work over all
algebraically closed fields at once, since the induction passes from $k$
to $\overline{k(t)}$. Global duality was announced by Verdier and proved
by Deligne (SGA4, XVIII); biduality for constructible complexes over
a field is due to Deligne (SGA4.5, Th. finitude).

A perfect pairing of complexes need not give perfect
pairings on cohomology modules. Over a field it does
(Corollary [sk-thm-derived-duality]). Over $\mathcal O_E$ there is an $\Ext^1$
term, and already on a point the complex
$[\mathcal O_E\xrightarrow{\pi_E}\mathcal O_E]$ in degrees $-1,0$ has
$H^0=\mathcal O_E/\pi_E$ while its dual has $H^0=0$
(Remark [sk-rem-pd-integral-corrections]). For this reason the duality
statements are formulated in the derived category, as perfect pairings
of perfect complexes (Definition [sk-def-pairing]). Note also
that duality relates eigenvalues without bounding them. For the
elliptic curve $y^2=x^3-x$ over $\mathbf F_3$ of the introduction it
shows that the Frobenius eigenvalues on $H^1$ have product $3$
(Example [sk-ex-ex-run-duality]). The pair $3,1$, with characteristic
polynomial $1-4T+3T^2$, consists of algebraic integers and satisfies
duality as well as $\pm i\sqrt3$ does; only purity excludes it.

Duality is used three times later. With its compatibility with
Frobenius (Theorem [sk-thm-frobenius]), it gives the functional equation
of the zeta function (Corollary [sk-cor-tf-functional-equation]). In the
Lefschetz–Verdier formula, the Künneth formula for Verdier duals
identifies a cohomological correspondence with a section of $c^!$ of
$K\boxtimes\mathbb D_XK$, and evaluation on the diagonal turns it into a
trace class (Lemma [sk-thm-sf-kunneth-verdier]). Finally, in
Section [sec-zeta-weil] it turns Deligne's upper bound on weights
into purity, since an eigenvalue $\alpha$ on $H^i$ and the eigenvalue
$q^d/\alpha$ on $H^{2d-i}$ both satisfy an upper bound.

Since we only consider constructible complexes of finite Tor dimension,
which at a geometric point are perfect (Lemma [sk-lem-finite]),
and $R\!\operatorname{Hom}_A(-,A)$ is a duality on perfect complexes over any ring, the
finite ring $A$ may be arbitrary. When $k$ is algebraically closed,
$D^b_{\mathrm{ctf}}(s,\Lambda)$ is the category of perfect $\Lambda$-complexes
(Lemma [sk-lem-finite]), so statements about cohomology, such as
perfect pairings in each degree, are statements in $D(\Lambda)$. Over a
finite field, the duality statements are isomorphisms on $s_{\mathrm{pro}\acute{e}t}$,
and the statements about cohomology are obtained after base change to an
algebraic closure, with the Weil action of Section [sec-frobenius].
