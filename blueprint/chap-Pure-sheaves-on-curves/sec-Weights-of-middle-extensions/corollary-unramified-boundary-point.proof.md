+++
kind = "proof"
of = "corollary-unramified-boundary-point"
order = 1187
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "proposition-lattices-representations-normal-scheme", "lemma-degree-zero-top-cohomology", "proposition-weights-j-boundary-points", "lemma-finite-quasi-finite-direct-images", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
