+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes"
order = 426
uses = ["theorem-comparison-direct-images", "lemma-reduction-derived-nakayama", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "proposition-proper-base-change-etale-site", "proposition-proper-direct-image-finite-coefficients", "proposition-construction-independence-rf-shriek", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "theorem-smooth-base-change-classical-torsion", "lemma-change-coefficients", "proposition-p-torsion-smooth-proper-curve"]
+++
*Finite coefficients.* Part (1), including the Tor bound, is
Proposition [proposition-proper-direct-image-finite-coefficients], and proper base change holds by
Theorem [theorem-proper-base-change-classical-pro] with $\Lambda=A$.
The projection formula, finally, is the classical torsion
formula [Stacks, [0F0G](https://stacks.math.columbia.edu/tag/0F0G)] in $D(Y_{\acute{e}t},A)$, transported to
$D(Y_{\mathrm{pro}\acute{e}t},A)$ by pullback from the étale site.

*Integral coefficients.* Let $K\in\Dbc(X,\mathcal O_E)$. We first show that $Rp_*K\in\Dbc(Y,\mathcal O_E)$, by computing its reduction as in (4.15) below. By
Proposition [proposition-integral-constructibility-criterion] and
Lemma [lemma-bounds-finite-reductions], $K$ is derived complete with
bounded classical finite reductions. Hence
Proposition [proposition-proper-base-change-complete-integral] applies. It
shows that $Rp_*K$ is derived complete and gives a canonical comparison
of reductions

$$
\rho_K:(Rp_*K)\otimes^{\mathbf L}\mathcal O_{E,Y}/\pi_E
\xrightarrow{\ \sim\ } Rp_*(K\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E).
\tag{4.15}
$$

The target of $\rho_K$ is constructible and
bounded. Indeed, it is the direct image of a torsion complex pulled back
from $X_{\acute{e}t}$ [Stacks, [09B1](https://stacks.math.columbia.edu/tag/09B1)], so it is the pullback to $Y_{\mathrm{pro}\acute{e}t}$ of the
direct image in $D(Y_{\acute{e}t},\mathbf F_E)$ [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)]. The latter is
constructible by the finiteness theorem for proper direct image
with torsion coefficients [Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0)], and bounded because $p$ has
finite cohomological dimension [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)]. Now
Proposition [proposition-integral-constructibility-criterion] gives
$Rp_*K\in\Dbc(Y,\mathcal O_E)$.

Proper base change holds by
Lemma [lemma-completed-ordinary-base-change], which applies
because $g^*Rp_*K$ and $g'^*K$ are derived complete, as inverse image
preserves integral constructibility (Lemma [lemma-integral-models](3)).

The projection formula is tested modulo $\pi_E$ in the same way. Let $C$ be
the cone of the projection formula map for $K\in\Dbc(X,\mathcal O_E)$ and
$M\in\Dbc(Y,\mathcal O_E)$. Its source $Rp_*K\otimes^{\mathbf L}M$ and
target $Rp_*(K\otimes^{\mathbf L}p^*M)$ are integrally constructible, by
Lemma [lemma-integral-models](3) and the fact just proved that $Rp_*$
maps $\Dbc(X,\mathcal O_E)$ into $\Dbc(Y,\mathcal O_E)$. As objects of
$\Dbc$ they are derived complete, and hence so is $C$. Derived
Nakayama (Lemma [lemma-reduction-derived-nakayama]) therefore reduces us
to showing $C/\pi_E=0$. In other words, we must show that the reduction
of the projection formula map is an isomorphism.

This reduction is the torsion projection formula map, which is an
isomorphism by [Stacks, [0F0G](https://stacks.math.columbia.edu/tag/0F0G)]. To identify the two maps, note that the
sources and targets correspond by $\rho_K$ and
associativity of extension of scalars, and the maps agree because both are
adjoint to the counit $p^*Rp_*K\to K$, as is
$\rho_K$.

*Rational coefficients.* Here $Rp_*$ commutes with the operations that
produce the generators of Lemma [lemma-integral-models](4) from
integral complexes. For $K\in\Dbc(X,\mathcal O_E)$, the complex
$K[1/\ell]$ is the colimit of $K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$,
and since this system has a common lower bound,
Corollary [corollary-continuity-cohomology] shows that

$$
Rp_*(K[1/\ell])\simeq(Rp_*K)[1/\ell].
$$

Likewise $Rp_*$ commutes with extension of scalars to a finite
$E'/E$, which is a finite direct sum by
Lemma [lemma-inverse-image-coefficient-sheaves](2). By
Corollary [corollary-continuity-cohomology] again, it also commutes with the filtered colimit
$\QbarX\otimes_{E_X}-=\varinjlim_{E'}E'_X\otimes_{E_X}-$.
By the integral case, it follows that $Rp_*$ maps the generators
into $\Dbc(Y,E)$ and $\Dbc(Y,\overline{\mathbf Q}_\ell)$. Since $Rp_*$ is exact and $\Dbc(Y,E)$
and $\Dbc(Y,\overline{\mathbf Q}_\ell)$ are triangulated
(Corollary [corollary-coefficient-heart-b]), $Rp_*$ preserves
$\Dbc(-,E)$ and $\Dbc(-,\overline{\mathbf Q}_\ell)$.

For proper base change and the projection formula it is enough to treat
the generators. Indeed, both sides of each map are exact functors in each
variable, so the objects for which the map is an isomorphism form a
triangulated subcategory. On the generators, the maps are obtained from
the integral isomorphisms by inverting $\ell$ and extending scalars. These
operations commute with $Rp_*$ by the preceding paragraph, and with $g^*$
and $\otimes^{\mathbf L}$ because they are given by tensoring with the
coefficient sheaves. Moreover, the maps so obtained are the base change and
projection formula maps, since these scalar comparisons commute with the
counits of $p^*\dashv Rp_*$.
