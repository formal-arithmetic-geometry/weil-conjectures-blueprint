+++
kind = "proof"
of = "corollary-unramified-boundary-point"
order = 1187
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-logarithm-determinant", "theorem-trace-formula-euler-product", "lemma-filtrations-spectra", "proposition-weights-under-usual-operations", "proposition-lattices-representations-normal-scheme", "lemma-degree-zero-top-cohomology", "lemma-positivity-convergence", "lemma-boundary-stalk", "lemma-point-count-bound", "proposition-weights-j-boundary-points", "lemma-cohomological-range-curve", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Purity follows from the upper bounds for the sheaf and for its dual,
provided the stalk of the dual is the dual of the stalk, and trivial
inertia guarantees this. So we apply
Proposition [proposition-weights-j-boundary-points] to the sheaf and to its
dual, which is pure of weight $-a$.  Since the inertia acts trivially,
the stalk of the extended dual is the dual of the stalk of the
extension, and so every eigenvalue $\alpha$ satisfies
$|\iota\alpha|^2\le q_z^a$ and $|\iota\alpha^{-1}|^2\le q_z^{-a}$, and
equality holds.

For a sheaf that is already lisse on the curve, the inertia is trivial, and
Lemma [lemma-boundary-stalk] identifies the stalk of $j_*$ with the
original stalk. The first assertion, applied at each of the finitely many
points outside the dense open, then gives the second.
