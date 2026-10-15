+++
kind = "proof"
of = "sk-prop-an"
uses = ["sk-lem-sp-finite-existence", "sk-lem-sp-p1"]
+++
*Local integration maps.* Over an open $U\subset S$ on which $V$ is trivial, a
frame $\tau:V\times_SU\xrightarrow{\sim}\mathbf A^d_U$ transports the integration
isomorphism $\operatorname{Tr}_{p_d}$ to an isomorphism in
$D(U_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$

$$
\operatorname{Tr}_\tau:R(\pi|_{V\times_SU})_!(\mathbf Z/\ell^n\mathbf Z)_{V\times_SU}(d)[2d]
\xrightarrow{\ \sim\ }(\mathbf Z/\ell^n\mathbf Z)_U.
$$

These maps commute with base change in $U$: the construction uses only
$c_1(\mathcal O_{\mathbf P^1_U}(1))$, the splitting of $Rq_*$ of [sk-lem-sp-p1] and
localization at infinity, and pullback preserves the Kummer class while proper
base change and localization identify the pulled-back constructions with those
over the new base.

*Independence of the frame.* The key point is that a linear change of
coordinates acts trivially on integration, because $\GL_d$ has connected
geometric fibres. Let

$$
a:\mathbf A^d_{\GL_{d,S}}\longrightarrow\mathbf A^d_{\GL_{d,S}},\qquad(g,v)\longmapsto(g,gv),
$$

be the universal linear change of coordinates, an automorphism over
$\GL_{d,S}$. It induces an automorphism in
$D(\GL_{d,S,\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$ of the compactly supported direct
image of $(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^d_{\GL_{d,S}}}(d)[2d]$ to $\GL_{d,S}$, which
integration identifies with the constant sheaf $(\mathbf Z/\ell^n\mathbf Z)_{\GL_{d,S}}$
in degree zero. So this automorphism is multiplication by a section

$$
u_a\in H^0\bigl((\GL_{d,S})_{\mathrm{ét}},(\mathbf Z/\ell^n\mathbf Z)^\times_{\GL_{d,S}}\bigr),
$$

a locally constant function with values in $(\mathbf Z/\ell^n\mathbf Z)^\times$. For a
geometric point $\bar s\to S$, the fibre $\GL_{d,\bar s}$ is connected (for
$d\ge1$ it is a nonempty open subset of the affine space of $d\times d$
matrices, for $d=0$ a point), so $u_a$ is constant on it; at the identity
matrix $a$ is the identity, so the constant is $1$. Hence $u_a=1$.

If $\tau,\tau'$ are two frames over $U$, then $\tau'\circ\tau^{-1}$ is the
pullback of $a$ along the transition matrix $U\to\GL_{d,S}$. By base change,
$u_a=1$ gives $\operatorname{Tr}_{\tau'}=\operatorname{Tr}_\tau$. Since source and
target are, locally, sheaves in degree zero, the local maps glue over a
trivializing cover to an isomorphism in $D(S_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$

$$
\operatorname{Tr}_\pi:R\pi_!(\mathbf Z/\ell^n\mathbf Z)_V(d)[2d]\xrightarrow{\ \sim\ }(\mathbf Z/\ell^n\mathbf Z)_S.
$$

*The purity map.* For general $K$, the projection formula and
$\operatorname{Tr}_\pi$ give

$$
R\pi_!\bigl(\pi^*K(d)[2d]\bigr)\simeq K\otimes^{\mathbf L}R\pi_!(\mathbf Z/\ell^n\mathbf Z)_V(d)[2d]
\xrightarrow{\ \mathrm{id}_K\otimes\operatorname{Tr}_\pi\ }K.
$$

Its adjoint under $R\pi_!\dashv\pi^!$ ([sk-lem-sp-finite-existence]) is the
asserted map. Over each trivializing open it is the affine-space adjunction
isomorphism following the integration isomorphism, so its cone vanishes on an
open cover and the map is an isomorphism.

The Kummer classes, projective-line integration and vector-bundle integration
all commute with base change on $S$, by the same arguments.
