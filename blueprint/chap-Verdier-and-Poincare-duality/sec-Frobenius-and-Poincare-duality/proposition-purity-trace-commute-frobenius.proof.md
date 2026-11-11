+++
kind = "proof"
of = "proposition-purity-trace-commute-frobenius"
order = 883
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "proposition-exact-products", "proposition-milnor-sequence", "corollary-continuity-cohomology", "definition-tate-twists", "lemma-reduction-derived-nakayama", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "lemma-change-coefficients-compact-support", "lemma-change-coefficients-exceptional-inverse-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "theorem-smooth-base-change-classical-torsion", "theorem-smooth-base-change-all-admissible", "lemma-kunneth-one-identity-factor", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "proposition-relative-dualizing-complex", "definition-sp-scalar-extension", "theorem-sp-qbar", "proposition-compatibility-purity-base-change", "definition-trace-map", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "lemma-kunneth-formula-compact-supports", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure"]
+++
Both identities are instances of base change for smooth purity, applied
to a square whose horizontal maps are not $k$-linear. Since $\gamma_f$
and $\operatorname{Tr}_f$ are built from base change maps and from the
Kummer class of the twist, we only have to know how $\operatorname{Fr}_T$
acts on Kummer classes.

The first identity is Proposition [proposition-compatibility-purity-base-change] for this
square. Since $\operatorname{Fr}_X$ is not a morphism over $k$, the only
point to check is that the identification of twists used there is the
Kummer identification, that is, that pullback along
$\operatorname{Fr}_T$ sends the Kummer class of a unit to the Kummer class
of its pullback. This holds because the Kummer sequence
$0\to\mu_{\ell^n}\to\mathbf G_m\xrightarrow{\ell^n}\mathbf G_m\to0$ and its
boundary map are natural for every morphism of schemes, $k$-linear or not.

For the second identity we combine the first with
the counit identity defining exceptional base change, which says that
after base change for compact support, the pulled-back
counit is the counit preceded by the exceptional comparison. As the
trace map is the counit composed with $\gamma_f$, the two identities
together give the statement for $\operatorname{Tr}_f$.
