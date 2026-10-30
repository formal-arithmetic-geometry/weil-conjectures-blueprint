+++
kind = "proof"
of = "sk-prop-an"
uses = ["sk-lem-sp-finite-existence", "sk-prop-geo-p1-adjunction"]
+++
We construct the trace isomorphism $\operatorname{Tr}_\pi$ for $V$ from
trivializations and show that it does not depend on the trivialization, and
the map $\pi^*K(d)[2d]\to\pi^!K$ is then its adjoint. A change of trivialization
multiplies the trace map by a locally constant unit on $\GL_d$, and this unit
is $1$ because the fibres of $\GL_d$ are connected and contain the identity.

*Local trace maps.* Over an open $U\subset S$ on which $V$
is trivial, a trivialization $\tau:V\times_S U\xrightarrow{\sim}\mathbf A^d_U$
transports (10.7) to an isomorphism

$$
\operatorname{Tr}_{\tau}:
R(\pi|_{V\times_S U})_!(\mathbf Z/\ell^n\mathbf Z)_{V\times_S U}(d)[2d]
\xrightarrow{\sim}(\mathbf Z/\ell^n\mathbf Z)_U.
$$

These maps commute with base change in $U$. Indeed, the construction uses
only $c_1(\mathcal O_{\mathbf P^1_U}(1))$, the splitting
(10.4) and localization at infinity. Pullback
preserves the Kummer class, and proper base change and localization
identify the pullbacks of the constructions with those over the new base.

*Independence of the trivialization.* Let

$$
\theta:\mathbf A^d_{\GL_{d,S}}\longrightarrow\mathbf A^d_{\GL_{d,S}},
\qquad (g,v)\longmapsto(g,gv),
$$

be the universal linear change of coordinates, an automorphism over
$\GL_{d,S}$. It induces an automorphism of the compactly supported
direct image of $(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^d_{\GL_{d,S}}}(d)[2d]$
to $\GL_{d,S}$, which the trace map identifies with the constant sheaf
$(\mathbf Z/\ell^n\mathbf Z)_{\GL_{d,S}}$ in degree zero. Hence this
automorphism is multiplication by a section

$$
u\in H^0\bigl((\GL_{d,S})_{\acute{e}t},
(\mathbf Z/\ell^n\mathbf Z)_{\GL_{d,S}}^{\times}\bigr),
$$

a locally constant function with values in
$(\mathbf Z/\ell^n\mathbf Z)^{\times}$. For a geometric point
$\bar s\to S$, the fibre $\GL_{d,\bar s}$ is connected: for $d\geq1$ it
is a nonempty open subset of the affine space of $d\times d$ matrices,
and for $d=0$ it is a point. Hence $u$ is constant on it. Since the map
$\theta$ is the identity at the identity matrix, which lies on
every geometric fibre, we conclude that $u=1$.

If $\tau$ and $\tau'$ are two trivializations over $U$, then $\tau'\circ\tau^{-1}$ is
the pullback of $\theta$ along the transition matrix $U\to\GL_{d,S}$. By
base change, the equality $u=1$ implies $\operatorname{Tr}_{\tau'}=\operatorname{Tr}_{\tau}$.
Since source and target are, locally, sheaves in degree zero, the
local maps glue over a trivializing cover to an isomorphism

$$
\operatorname{Tr}_{\pi}:
R\pi_!(\mathbf Z/\ell^n\mathbf Z)_V(d)[2d]
\xrightarrow{\sim}(\mathbf Z/\ell^n\mathbf Z)_S.
$$

*The map $\pi^*K(d)[2d]\to\pi^!K$.* For general $K$, the projection formula and
$\operatorname{Tr}_\pi$ give

$$
R\pi_!\bigl(\pi^{*}K(d)[2d]\bigr)
\simeq K\otimes^{\mathbf L} R\pi_!(\mathbf Z/\ell^n\mathbf Z)_V(d)[2d]
\xrightarrow{\ \mathrm{id}_K\otimes\operatorname{Tr}_{\pi}\ }K.
$$

Its adjoint under $R\pi_!\dashv\pi^{!}$
(Proposition [sk-prop-cohsm](1)) is the asserted map. Over each
trivializing open, it is the isomorphism given by the adjunction for affine space
following (10.7). Thus its cone vanishes on an
open cover, and the map is an isomorphism.
