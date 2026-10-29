+++
kind  = "proof"
of    = "sk-thm-sfb-proper-base-change"
uses = ["sk-prop-ctf-finite-proper", "sk-thm-properbasechange", "sk-cor-pbc-proet-finite", "sk-prop-integral-criterion", "sk-lem-integral-models", "sk-lem-pe-derived-nakayama", "sk-cor-pe-bounded-continuity", "sk-prop-sfb-cartesian-coefficients", "sk-cor-coefficient-heart-ii"]
+++
*Finite coefficients.* Let $\Lambda=A$ be a finite ring. Bounded constructibility follows from
finiteness of proper direct image for constructible torsion sheaves and a uniform
cohomological bound, and the projection formula for constant modules yields a finite Tor
bound. The details are in [sk-prop-ctf-finite-proper]. Proper base change holds by
[sk-thm-properbasechange] with $\Lambda=A$, in the form [sk-cor-pbc-proet-finite] for a finite
ring. The projection formula is the classical torsion formula
([Stacks, Tag 0F0G](https://stacks.math.columbia.edu/tag/0F0G)) in $D(Y_{\mathrm{ét}},A)$,
transported to $D(Y_{\mathrm{proét}},A)$ by pullback from the étale site. Details:
[det-thm-sfb-proper-base-change-finite].

*Integral coefficients.* Let $K\in\Dbc(X,\cO_E)$. The complex $Rp_*K$ is derived complete.
Indeed, $K$ is derived complete if and only if
$R\varprojlim(\cdots\xrightarrow{\pi_E}K\xrightarrow{\pi_E}K)=0$, and $Rp_*$ commutes with
$R\varprojlim$ because it is a right adjoint. Moreover, reduction modulo $\pi_E$ commutes with
$Rp_*$, in other words,
$$
(Rp_*K)\otimes^{\mathbf L}\cO_{E,Y}/\pi_E\simeq Rp_*(K\otimes^{\mathbf L}\cO_{E,X}/\pi_E).
$$
Indeed, $K\otimes^{\mathbf L}\cO_{E,X}/\pi_E$ is the cone of multiplication by $\pi_E$ on $K$,
and the exact functor $Rp_*$ commutes with this cone. The right side is the direct image of a
complex with torsion coefficients. This complex is pulled back from $X_{\mathrm{ét}}$
([Stacks, Tag 09B1](https://stacks.math.columbia.edu/tag/09B1)), and hence its direct image
in $D(Y_{\mathrm{proét}},\mathbf F_E)$ is the pullback to $Y_{\mathrm{proét}}$ of its direct
image in $D(Y_{\mathrm{ét}},\mathbf F_E)$
([Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6)). The direct image on the étale
site is constructible by the finiteness theorem for proper direct image with torsion
coefficients ([Stacks, Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0)), and bounded
because $p$ has finite cohomological dimension
([Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10)). By
[sk-prop-integral-criterion], $Rp_*K\in\Dbc(Y,\cO_E)$.

Consider the projection formula map and the base change map for constructible integral
complexes. By the preceding paragraph and [sk-lem-integral-models] (3), the sources and
targets of these maps are derived complete, and their reductions modulo $\pi_E$ are the
projection formula map and the proper base change map with torsion coefficients. The first of
these is an isomorphism by the projection formula for torsion coefficients
([Stacks, Tag 0F0G](https://stacks.math.columbia.edu/tag/0F0G)). The second is an isomorphism
by [sk-thm-properbasechange], which applies because the finite reductions are bounded below
complexes pulled back from the étale site (see also [sk-prop-pbc-complete] and
[Stacks, Tag 09C9](https://stacks.math.columbia.edu/tag/09C9)). Thus each integral map is a
morphism between derived complete complexes whose reduction modulo $\pi_E$ is an isomorphism,
and by derived Nakayama ([sk-lem-pe-derived-nakayama]) it is an isomorphism. Details:
[det-thm-sfb-proper-base-change-integral].

*Rational coefficients.* For $K\in\Dbc(X,\cO_E)$, the complex $K[1/\ell]$ is the colimit of
$K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$, a system with a common lower bound. Hence
[sk-cor-pe-bounded-continuity] shows that
$$
Rp_*(K[1/\ell])\simeq(Rp_*K)[1/\ell].
$$
In the same way, $Rp_*$ commutes with extension of scalars to a finite $E'/E$ (which is a
finite direct sum, by [sk-prop-sfb-cartesian-coefficients] (2)) and, by
[sk-cor-pe-bounded-continuity] again, with the filtered colimit
$\QbarX\otimes_{E_X}-=\varinjlim_{E'}E'_X\otimes_{E_X}-$. By the integral case, $Rp_*$ therefore
maps the generators of [sk-lem-integral-models] (4) into $\Dbc(Y,E)$ and $\Dbc(Y,\Qlb)$. Since
$Rp_*$ is exact and $\Dbc(Y,E)$ and $\Dbc(Y,\Qlb)$ are triangulated
([sk-cor-coefficient-heart-ii]), it follows that $Rp_*$ preserves $\Dbc(-,E)$ and
$\Dbc(-,\Qlb)$. For the projection formula and proper base change, note that both sides of
each map are exact functors in each variable, so that the objects for which the map is an
isomorphism form a triangulated subcategory. It is therefore enough to treat the generators.
For these, the maps are obtained from the integral isomorphisms by inverting $\ell$ and
extending scalars, operations that commute with $Rp_*$ by the preceding paragraph and with
$g^*$ and $\otimes^{\mathbf L}$ because they are given by tensoring with the coefficient
sheaves. Details: [det-thm-sfb-proper-base-change-rational].
