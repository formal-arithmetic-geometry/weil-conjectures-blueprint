+++
kind = "proof"
of = "proposition-projective-line-rational-coefficients"
order = 608
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "corollary-evaluation-weakly-contractible-objects", "proposition-repleteness-pro-etale-topos", "lemma-comparison-completed-coefficients", "definition-local-cohomology", "lemma-local-cohomology-right-adjoint", "lemma-integral-models", "definition-pro-etale-base-change-map", "lemma-finite-morphisms", "definition-projection-formula-map", "lemma-checking-isomorphisms-constructible-complexes", "lemma-cycle-class-cartier-divisor", "lemma-cohomology-projective-line-trace", "lemma-class-diagonal-projective-line", "definition-change-of-coefficients-maps", "definition-kunneth-map", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve"]
+++
Define the unit and counit by the formulas (6.7) and
(6.8) of
Proposition [proposition-adjunction-projective-line], using
$\Delta_*M\simeq p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda$ [Stacks, [09AD](https://stacks.math.columbia.edu/tag/09AD)] and
the maps $\delta_\Lambda$ and $\operatorname{Tr}_q$ in place of their
torsion versions. The proof of the identities $s_1=s_2=1$ computed stalks of torsion sheaves, but apart from these identities the torsion calculation
of the triangle identities used only the projection formula and proper
base change. These hold here by
Propositions [proposition-projection-formula-rational-coefficients]
and [proposition-proper-base-change-localizing-categories]. Thus the calculation reduces the triangle identities to the identities
$\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta_\Lambda)=1$ of
Proposition [proposition-ell-adic-cycle-class-diagonal]. Finally, uniqueness of adjoints gives the last claim.
