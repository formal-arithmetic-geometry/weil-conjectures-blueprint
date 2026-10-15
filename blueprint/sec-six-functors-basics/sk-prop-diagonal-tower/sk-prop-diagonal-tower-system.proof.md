+++
kind = "proof"
of = "det-prop-diagonal-tower-system"
+++
(1) The diagonal is an effective Cartier divisor in $W$, with equation
$x_0y_1-x_1y_0$. With $u$ the inclusion of the complement of $\Delta$, the
sheaf $\mathcal M_\Delta\subset u_*\mathbf G_{m}$ of sections that are units
away from $\Delta$ with at most a simple pole along $\Delta$ is generated locally by the units and $t^{-1}$, and the order of the
pole defines the surjection onto $\Delta_*\mathbf Z$ with kernel
$\mathbf G_m$; this is the extension in the proof of [sk-lem-geo-cartier]
(compare [lem-amb-cartier-kummer-map]). Pullback to the pro-étale site is
exact, and $\Delta_*$ of the pulled-back sheaf $\mathbf Z$ is the pullback of
$\Delta_*\mathbf Z$ by closed base change, so the pulled-back sequence is still
exact. Consequently the map from the two-term complex
$[\mathbf G_m\to\mathcal M_\Delta]$ (degrees $-1,0$) to $\Delta_*\mathbf Z$
given by the quotient map in degree $0$ is a quasi-isomorphism, and the
projection to $\mathbf G_m$ in degree $-1$ gives a map of complexes to
$\mathbf G_m[1]$. The roof is the morphism $\partial$; it is the class of the
extension in $\Ext^1(\Delta_*\mathbf Z,\mathbf G_m)$.

(2) Choose a K-flat resolution $P\to K$ of complexes of
$\mathbf Z$-modules on $W_{\mathrm{proét}}$ and set
$T(K)=(P\otimes_{\mathbf Z}\underline{\mathbf Z/\ell^n})_n$, with transition
maps induced by the reductions $\mathbf Z/\ell^{n+1}\to\mathbf Z/\ell^n$;
$\mathbf Z_\ell$ acts on the $n$-th term through $\mathbf Z/\ell^n$. A
quasi-isomorphism of K-flat complexes stays a quasi-isomorphism after
tensoring with each $\underline{\mathbf Z/\ell^n}$, and a map of inverse
systems is a quasi-isomorphism if and only if each evaluation is (evaluation
at a level is exact and the evaluations jointly detect acyclicity). Hence $T$
is independent of the resolution up to unique isomorphism and defines an
exact functor on derived categories. The composite with $R\varprojlim$ sends
$K$ to $R\varprojlim_n(K\otimes^{\mathbf L}\mathbf Z/\ell^n)$, which is the
derived $\ell$-completion $\widehat K$ (Stacks, Tag 099M).

(3) *Source.* For a sheaf $F$, the map
$(\Delta_*\mathbf Z)\otimes F\to\Delta_*\Delta^{-1}F$ is an isomorphism: after
restriction to the open complement both sides vanish, and after
$\Delta^{-1}$ both become $\Delta^{-1}F$; these two restrictions are jointly
conservative (Stacks, Tag 09AD). The right side is exact in $F$, so
$\Delta_*\mathbf Z$ is flat and $T(\Delta_*\mathbf Z)$ is the system
$\Delta_*\mathbf Z/\ell^\bullet$ with reduction maps as transitions.

*Target.* The Kummer sequence $0\to\mu_{\ell^n}\to\mathbf G_m\xrightarrow{\ell^n}\mathbf G_m\to0$
is exact on the pro-étale site ($\ell$ invertible), so computing
$\mathbf G_m\otimes^{\mathbf L}\mathbf Z/\ell^n$ with the resolution
$[\mathbf Z\xrightarrow{\ell^n}\mathbf Z]$ (degrees $-1,0$) gives the complex
$[\mathbf G_m\xrightarrow{\ell^n}\mathbf G_m]$, whose only cohomology is
$\mu_{\ell^n}$ in degree $-1$; thus
$\mathbf G_m\otimes^{\mathbf L}\mathbf Z/\ell^n\simeq\mu_{\ell^n}[1]$. The
transition from level $n+1$ to level $n$ is induced by the map of resolutions
which is multiplication by $\ell$ in degree $-1$ and the identity in degree
$0$; on the kernel $\mu_{\ell^{n+1}}$ in degree $-1$ it is
$\zeta\mapsto\zeta^\ell$. Since every level has cohomology in a single degree,
the canonical truncations identify $T(\mathbf G_m[1])$ with the system
$(\mu_{\ell^n}[2])_n=\mathbf Z/\ell^\bullet(1)[2]$, compatibly with the linear
structures.

(4) $T$ applied to $\partial$ is a single morphism in
$D(W^{\mathbf N}_{\mathrm{proét}})$. Evaluating at level $n$ gives
$\partial\otimes^{\mathbf L}\mathbf Z/\ell^n:\Delta_*\mathbf Z/\ell^n\to\mu_{\ell^n}[2]$,
which is the composite of the Cartier boundary with the Kummer boundary
$\mathbf G_m[1]\to\mu_{\ell^n}[2]$, that is, the torsion cycle class of
$\Delta$ as constructed in [sk-lem-geo-cartier], with the same sign
convention.
