+++
kind = "proof"
of = "sk-prop-sp-tower-geometric"
uses = ["sk-lem-sp-tower-levels", "sk-prop-geo-p1-adjunction", "sk-lem-sp-finite-existence", "sk-lem-sp-reduction"]
+++
We repeat the finite construction in the ringed topos of towers on
$T_{\mathrm{proét}}$, with coefficient ring $\mathcal O_{E,T}/\ell^\bullet$, and
check each identity level by level.

*Classes and integration.* In the abelian category of towers of abelian
sheaves there is an exact Kummer sequence

$$
0\longrightarrow(\mu_{\ell^n})_n
\longrightarrow(\mathbb G_m,(\cdot)^\ell)
\xrightarrow{\ ((\cdot)^{\ell^n})_n\ }
(\mathbb G_m,\mathrm{id})\longrightarrow0,
$$

with the $\ell$-power map as transition on $\mu_{\ell^n}$. A line bundle $L$
gives a class in $H^1$ of the last tower, and its boundary is a class in
$H^2((\mu_{\ell^n})_n)$, that is, a morphism
$(\mathbf Z/\ell^n)_n\to(\mu_{\ell^n})_n[2]$ in the derived category of
$(\mathbf Z/\ell^n)_n$-modules. Extending coefficients to
$\mathcal O_{E,T}/\ell^\bullet$ gives
$c_1(L):\mathcal O_{E,T}/\ell^\bullet\to (\mathcal O_{E,T}/\ell^\bullet)(1)[2]$. The
Kummer sequence is used only in the abelian category where it is exact, and
linearity over $\mathcal O_{E,T}/\ell^\bullet$ is added afterwards. The version
with supports, applied to a Cartier divisor with its canonical section, gives
the diagonal class, a morphism in
$D(\operatorname{Tow}(\mathbf P^1_S\times_S\mathbf P^1_S,\mathcal O_E))$,
$\delta_\bullet:\Delta_*\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet\to
(\mathcal O_{E,\mathbf P^1_S\times_S\mathbf P^1_S}/\ell^\bullet)(1)[2]$.

The unit and $c_1(\mathcal O(1))$ define a morphism in
$D(\operatorname{Tow}(S,\mathcal O_E))$

$$
\mathcal O_{E,S}/\ell^\bullet\oplus (\mathcal O_{E,S}/\ell^\bullet)(-1)[-2]\longrightarrow
Rq_{*,\bullet}\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet.
$$

It is an isomorphism, since by [sk-lem-sp-tower-levels] it evaluates at each
level to the projective-line splitting of [sk-prop-geo-p1-adjunction], and evaluations
jointly detect isomorphisms. Let $\operatorname{Tr}_{q,\bullet}$ be the projection
onto the twisted second summand.

*Unit and counit on the projective line.* The counit is the projection formula
followed by $\mathrm{id}\otimes\operatorname{Tr}_{q,\bullet}$, and the unit is given
by the diagonal class:

$$
\begin{aligned}
Rq_{*,\bullet}(q_\bullet^*K_\bullet(1)[2])
&\simeq K_\bullet\otimes^{\mathbf L}
Rq_{*,\bullet}(\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet)(1)[2]
\longrightarrow K_\bullet,\\
M_\bullet&\simeq Rp_{2*,\bullet}\Delta_*M_\bullet
\xrightarrow{\ Rp_{2*,\bullet}(\delta_\bullet\otimes p_1^*M_\bullet)\ }
Rp_{2*,\bullet}p_1^*M_\bullet(1)[2]
\simeq q_\bullet^*Rq_{*,\bullet}M_\bullet(1)[2].
\end{aligned}
$$

As in [sk-prop-geo-p1-adjunction], proper base change and the projection formulas in this
topos reduce the triangle identities to

$$
\operatorname{Tr}_{p_i,\bullet}\circ Rp_{i*,\bullet}\delta_\bullet
=\mathrm{id}_{\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet}\qquad(i=1,2).
$$

Both sides are morphisms between tower sheaves in degree zero, and they agree
at each level by the finite diagonal integrals; so they agree. This gives the
projective-line adjunction in $D(\operatorname{Tow})$.

*Charts and gluing.* Restrict to $\mathbf A^1_S$ by extension by zero, iterate
to $\mathbf A^d_S$, and compose with the étale adjunction
$e_{!,\bullet}\dashv e_\bullet^*$. The local counits are the iterated
integrations and fibre sums of the finite construction, now as maps of towers.
For each $K_\bullet$, glue the local representing pairs by the open-cover cone
and the Hom sequences of the open-cover argument, as after
[sk-lem-sp-finite-existence]: compatible local counits lift by exactness of the
Hom sequence, and comparing Hom sequences shows that the glued pair represents
$M_\bullet\mapsto\operatorname{Hom}(Rf_{!,\bullet}M_\bullet,K_\bullet)$. Its restrictions
to charts have the stated form, so the cohomological and Tor bounds are
uniform. Since a representing pair with its counit is unique up to unique
isomorphism, this defines the functor and its action on maps without a
functorial choice of cones.

Evaluation at level $n$ preserves these constructions and gives the finite
local counits, so by the same argument the evaluated pair represents the finite
functor. Uniqueness identifies it with $f_{\mathcal O_E/\ell^n}^!C_n$, compatibly
with counits and hence with units. The coefficient comparisons have the same
local counits, so uniqueness also identifies the transition maps with those of
[sk-lem-sp-reduction].
