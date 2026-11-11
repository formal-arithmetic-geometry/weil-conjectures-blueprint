+++
kind = "proof"
of = "lemma-base-change-cone-x-z"
order = 1636
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "corollary-evaluation-weakly-contractible-objects", "proposition-exact-products", "proposition-milnor-sequence", "corollary-continuity-cohomology", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-reduction-derived-nakayama", "lemma-descent-finite-coefficient-field", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-pro-etale-base-change-map", "theorem-comparison-over-henselian-pair-degree", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-completed-ordinary-base-change", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-etale-derived-category", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "theorem-smooth-base-change-all-admissible", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms"]
+++
Both the source and the target of $\tau$ are compatible with proper
direct image and smooth pullback, so the cone is as well. To prove the
vanishing on $i_*M$, we reduce to the pair $(Z,Z)$, where the
deformation is a constant family.

By Lemma [lemma-functoriality-deformation], $f$ induces a morphism
$\widetilde f$ of deformations, which is proper if $f$ is proper and
smooth if $f$ is smooth. To this morphism we apply the base change maps of
nearby cycles, together with proper or smooth base change for the
restriction to the zero section.  The resulting squares for
$\tau$ then commute because the base change map for pullback is compatible
with composition, and their cofibres give the two isomorphisms.
In the special case $f=i$, the source pair is $(Z,Z)$ and
$\mathcal D_ZZ=Z\times S$, so $\tau_{Z,Z}$ is the
inverse of the isomorphism of Lemma [lemma-nearby-cycles-constant-family].
Hence $C_{Z,Z}=0$, and since $i$ is proper, the first isomorphism gives
$C_{X,Z}(i_*M)=0$.
The last assertion then follows by applying the exact functor $C_{X,Z}$
to $j_!j^*L\to L\to i_*i^*L$.
