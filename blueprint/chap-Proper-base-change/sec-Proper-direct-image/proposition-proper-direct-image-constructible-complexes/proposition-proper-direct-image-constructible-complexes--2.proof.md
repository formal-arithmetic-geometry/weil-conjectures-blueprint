+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--2"
order = 425005
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-comparison-morphism-inverse-image--2", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "theorem-comparison-direct-images--1", "proposition-comparison-immersions--1", "proposition-locally-constant-sheaves-finite-presentation--3", "definition-derived-adic-completeness--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--4", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "definition-lisse-sheaves--1", "proposition-integral-constructibility-criterion--1", "lemma-constructible-sheaves--8", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "definition-torsion-pbc-property--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "proposition-proper-base-change-etale-site--1", "corollary-cohomology-geometric-fibres--2", "proposition-proper-base-change-complete-integral--1", "proposition-comparison-etale-derived-category--5", "proposition-comparison-etale-derived-category--6", "corollary-open-direct-image-over-field--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1", "theorem-chow-s-lemma-projective-form--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-degree-jacobian--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
+++
*Integral coefficients.* Let $K\in\Dbc(X,\mathcal O_E)$. We first show that $Rp_*K\in\Dbc(Y,\mathcal O_E)$, by computing its reduction as in (4.15) below. By
Proposition [proposition-integral-constructibility-criterion] and
Lemma [lemma-bounds-finite-reductions], $K$ is derived complete with
bounded classical finite reductions. Hence
Proposition [proposition-proper-base-change-complete-integral] applies.
It shows that $Rp_*K$ is derived complete, and it gives a canonical comparison
of reductions

$$
(Rp_*K)\otimes^{\mathbf L}\mathcal O_{E,Y}/\pi_E
\simeq Rp_*(K\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E).
$$

The right side of (4.15) is constructible and
bounded. Indeed, it is the direct image of a torsion complex pulled back
from $X_{\acute{e}t}$ [Stacks, [09B1](https://stacks.math.columbia.edu/tag/09B1)]. So it is the pullback to $Y_{\mathrm{pro}\acute{e}t}$ of the
direct image in $D(Y_{\acute{e}t},\mathbf F_E)$ [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)]. The latter is
constructible by the finiteness theorem for proper direct image
with torsion coefficients [Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0)]. It is bounded because $p$ has
finite cohomological dimension [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)]. Now
Proposition [proposition-integral-constructibility-criterion] gives
$Rp_*K\in\Dbc(Y,\mathcal O_E)$.

*Source:* the proof of Proposition [proposition-proper-direct-image-constructible-complexes].
