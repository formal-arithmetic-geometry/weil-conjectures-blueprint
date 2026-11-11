+++
kind = "proof"
of = "proposition-purity-vector-bundles"
order = 742
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "lemma-affine-space-etale-localization", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
We transport the trace map of affine space along local trivializations,
show that the result does not depend on the trivialization, so that the
local maps glue to a trace isomorphism $\operatorname{Tr}_\pi$ for $V$, and
take the map $\pi^*K(d)[2d]\to\pi^!K$ to be its adjoint.

*Local trace maps.* Locally on $S$ the bundle is affine space, where
the trace map has already been constructed. Over an open $U\subset S$ on
which $V$ is trivial, a trivialization
$\tau:V\times_S U\xrightarrow{\sim}\mathbf A^d_U$
transports (9.11) to an isomorphism

$$
\operatorname{Tr}_{\tau}:
R(\pi|_{V\times_S U})_!(\mathbf Z/\ell^n\mathbf Z)_{V\times_S U}(d)[2d]
\xrightarrow{\sim}(\mathbf Z/\ell^n\mathbf Z)_U.
$$

These maps commute with base change in $U$, because the construction uses
only $c_1(\mathcal O_{\mathbf P^1_U}(1))$, the splitting
(9.8) and localization at infinity: pullback
preserves the Kummer class, and proper base change and localization
identify the pullbacks of the constructions with those over the new base.

*Independence of the trivialization.* A change of trivialization
multiplies the trace map by a locally constant unit on $\GL_d$, and this
unit is $1$. As two trivializations differ by a matrix with values in
$\GL_d$, it suffices to study one universal change of coordinates,
parametrized by $\GL_{d,S}$ itself, and then pull back. Let

$$
\theta:\mathbf A^d_{\GL_{d,S}}\longrightarrow\mathbf A^d_{\GL_{d,S}},
\qquad (g,v)\longmapsto(g,gv),
$$

be the universal linear change of coordinates, an automorphism over
$\GL_{d,S}$. It induces an automorphism of the compactly supported
direct image of $(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^d_{\GL_{d,S}}}(d)[2d]$
to $\GL_{d,S}$, which the trace map identifies with the constant sheaf
$(\mathbf Z/\ell^n\mathbf Z)_{\GL_{d,S}}$ in degree zero, so that this
automorphism is multiplication by a section

$$
u\in H^0\bigl((\GL_{d,S})_{\acute{e}t},
(\mathbf Z/\ell^n\mathbf Z)_{\GL_{d,S}}^{\times}\bigr),
$$

a locally constant function with values in
$(\mathbf Z/\ell^n\mathbf Z)^{\times}$. It is therefore constant on each geometric
fibre $\GL_{d,\bar s}$, which is connected: for $d\geq1$ it
is a nonempty open subset of the affine space of $d\times d$ matrices,
and for $d=0$ it is a point. As $\theta$ is the identity at the identity
matrix, which lies on every geometric fibre, $u=1$.

The local trace maps agree on overlaps of trivializing opens. Indeed, let
$\tau$ and $\tau'$ be two trivializations over $U$. Then
$\tau'\circ\tau^{-1}$ is the pullback of $\theta$ along the transition
matrix $U\to\GL_{d,S}$, so by base change the equality $u=1$ implies
$\operatorname{Tr}_{\tau'}=\operatorname{Tr}_{\tau}$. Moreover, morphisms between
source and target form a sheaf, as both are locally sheaves in degree zero.
Hence the local maps glue over a trivializing cover to an isomorphism

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
(Proposition [proposition-exceptional-inverse-image-smooth-morphism](1)) is the asserted map.
We show that it is an isomorphism. This may be checked locally on $V$,
because $\pi^!$ commutes with restriction to opens. Over each trivializing
open, $\operatorname{Tr}_\pi$ is $\operatorname{Tr}_\tau$ by construction,
so there the map is the isomorphism given by the adjunction for
affine space following (9.11).
