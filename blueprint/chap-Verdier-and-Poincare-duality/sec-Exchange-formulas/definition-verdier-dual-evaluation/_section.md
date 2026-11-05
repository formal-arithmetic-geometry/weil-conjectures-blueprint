+++
id = "definition-verdier-dual-evaluation"
kind = "definition"
title = "Verdier dual and evaluation"
order = 827
lean = ["AlgebraicGeometry.ProEtale.dualizingComplex", "AlgebraicGeometry.ProEtale.verdierDual", "AlgebraicGeometry.ProEtale.CondensedRing.dualizingComplex", "AlgebraicGeometry.ProEtale.CondensedRing.verdierDual", "AlgebraicGeometry.ProEtale.CondensedRing.verdierBiduality", "AlgebraicGeometry.Etale.verdierDualDoubleDual"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The *dualizing complex* and the *Verdier dual* are

$$
\omega_X=a_X^!\Lambda_s,\qquad
\mathbb D_XK=\cHom_{\Lambda_X}(K,\omega_X).
$$

Thus $\mathbb D_X:D(X_{\mathrm{pro}\acute{e}t},\Lambda)^{\mathrm{op}}\to
D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is an exact functor. The *double-dual
morphism*

$$
\delta_K:K\longrightarrow\mathbb D_X\mathbb D_XK
$$

is the tensor–Hom adjoint of the composite
$K\otimes^{\mathbf L}\mathbb D_XK\simeq\mathbb D_XK\otimes^{\mathbf L}K
\to\omega_X$ of the symmetry isomorphism, with its Koszul sign, and
evaluation.
