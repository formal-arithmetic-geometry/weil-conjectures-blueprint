+++
kind = "proof"
of = "sk-thm-sfb-proper-base-change"
uses = ["sk-prop-ctf-finite-proper", "sk-thm-properbasechange", "sk-cor-pbc-proet-finite", "sk-prop-integral-criterion", "sk-lem-integral-models", "sk-lem-pe-derived-nakayama", "sk-cor-pe-bounded-continuity", "sk-prop-sfb-cartesian-coefficients", "sk-cor-coefficient-heart-ii", "sk-lem-integral-finite-levels", "sk-prop-pbc-complete", "sk-rem-pbc-complete-ordinary"]
+++
*Finite coefficients.* Let $\Lambda=A$ be a finite ring. Bounded
constructibility follows from finiteness of proper direct image for
constructible torsion sheaves and a uniform cohomological bound, and the
projection formula for constant modules yields a finite Tor bound. The
details are in Proposition [sk-prop-ctf-finite-proper]. Proper base change
holds by Theorem [sk-thm-properbasechange] with $\Lambda=A$. The projection formula is the classical torsion
formula [Stacks, Tag 0F0G](https://stacks.math.columbia.edu/tag/0F0G) in $D(Y_{\acute{e}t},A)$, transported to
$D(Y_{\mathrm{pro}\acute{e}t},A)$ by pullback from the étale site.

*Integral coefficients.* Let $K\in\Dbc(X,\mathcal O_E)$. The complex
$K$ is derived complete and has bounded classical finite reductions by
Proposition [sk-prop-integral-criterion] and
Lemma [sk-lem-integral-finite-levels]. Proposition [sk-prop-pbc-complete]
therefore shows that $Rp_*K$ is derived complete and supplies the
canonical reduction comparison

$$
(Rp_*K)\otimes^{\mathbf L}\mathcal O_{E,Y}/\pi_E
\simeq Rp_*(K\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E).
\tag{5.2}
$$

The right side of (5.2) is the
direct image of a complex with torsion coefficients. This complex is pulled
back from $X_{\acute{e}t}$ [Stacks, Tag 09B1](https://stacks.math.columbia.edu/tag/09B1), and hence its direct image in
$D(Y_{\mathrm{pro}\acute{e}t},\mathbf F_E)$ is the pullback to $Y_{\mathrm{pro}\acute{e}t}$ of its
direct image in $D(Y_{\acute{e}t},\mathbf F_E)$ [Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6). The direct image
on the étale site is constructible by the finiteness theorem for proper direct image
with torsion coefficients [Stacks, Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0), and bounded because $p$ has
finite cohomological dimension [Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10). By
Proposition [sk-prop-integral-criterion], $Rp_*K\in\Dbc(Y,\mathcal O_E)$.

Inverse image preserves integral constructibility
(Lemma [sk-lem-integral-models](3)), so $g^*Rp_*K$ and $g'^*K$ are
derived complete, and by Remark [sk-rem-pbc-complete-ordinary] the
ordinary base change map is an isomorphism.

The source and target of the projection formula map are derived complete
for the same reasons. Its reduction modulo $\pi_E$ is the torsion
projection formula map, an isomorphism by [Stacks, Tag 0F0G](https://stacks.math.columbia.edu/tag/0F0G): by
(5.2) and associativity of extension of scalars
the objects match, and the maps match because both are adjoint to the
counit $p^*Rp_*K\to K$, as is (5.2). Derived
Nakayama (Lemma [sk-lem-pe-derived-nakayama]) proves the integral projection
formula.

*Rational coefficients.* For $K\in\Dbc(X,\mathcal O_E)$, the complex
$K[1/\ell]$ is the colimit of $K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$,
a system with a common lower bound. Hence
Corollary [sk-cor-pe-bounded-continuity] shows that

$$
Rp_*(K[1/\ell])\simeq(Rp_*K)[1/\ell].
$$

In the same way, $Rp_*$ commutes with extension of scalars to a finite
$E'/E$ (which is a finite direct sum, by
Lemma [sk-prop-sfb-cartesian-coefficients](2)) and, by
Corollary [sk-cor-pe-bounded-continuity] again, with the filtered colimit
$\QbarX\otimes_{E_X}-=\varinjlim_{E'}E'_X\otimes_{E_X}-$.
By the integral case, $Rp_*$ therefore maps the generators of
Lemma [sk-lem-integral-models](4) into $\Dbc(Y,E)$ and $\Dbc(Y,\overline{\mathbf Q}_\ell)$.
Since $Rp_*$ is exact and $\Dbc(Y,E)$ and $\Dbc(Y,\overline{\mathbf Q}_\ell)$ are triangulated
(Corollary [sk-cor-coefficient-heart-ii]), it follows that $Rp_*$ preserves
$\Dbc(-,E)$ and $\Dbc(-,\overline{\mathbf Q}_\ell)$. For the projection formula and proper
base change, note that both sides of each map are exact functors in each
variable, so that the objects for which the map is an isomorphism form a
triangulated subcategory. It is therefore enough to treat the generators.
For these, the maps are obtained from the integral isomorphisms by
inverting $\ell$ and extending scalars, operations that commute with
$Rp_*$ by the preceding paragraph and with $g^*$ and $\otimes^{\mathbf L}$
because they are given by tensoring with the coefficient sheaves.
Since these scalar comparisons commute with the counits of
$p^*\dashv Rp_*$, the maps so obtained are the base change and projection
formula maps, compatible with composition as in the integral case.
