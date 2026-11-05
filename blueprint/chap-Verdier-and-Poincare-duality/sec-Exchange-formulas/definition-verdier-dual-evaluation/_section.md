+++
id = "definition-verdier-dual-evaluation"
kind = "definition"
title = "Verdier dual and evaluation"
order = 827
lean = ["AlgebraicGeometry.ProEtale.dualizingComplex", "AlgebraicGeometry.ProEtale.verdierDual", "AlgebraicGeometry.ProEtale.CondensedRing.dualizingComplex", "AlgebraicGeometry.ProEtale.CondensedRing.verdierDual", "AlgebraicGeometry.ProEtale.CondensedRing.verdierBiduality", "AlgebraicGeometry.Etale.verdierDualDoubleDual"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
