+++
id = "definition-correspondence"
kind = "definition"
title = "Correspondences"
order = 904
lean = ["AlgebraicGeometry.Etale.CohomologicalCorrespondence", "AlgebraicGeometry.Etale.CohomologicalCorrespondence.fixedScheme", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $X$ be a separated $k$-scheme of finite type. A *correspondence*
on $X$ is a morphism of $k$-schemes $c=(c_1,c_2):C\to X\times_sX$ from a
separated $k$-scheme of finite type (similarly over a base $S$). For $K\in D^b_{\mathrm{ctf}}(X,A)$, a
*cohomological correspondence* on $(X,K)$ is a morphism

$$
u:c_2^*K\longrightarrow c_1^!K.
$$

The *fixed locus* of $c$ is the closed subscheme

$$
\Fix(c)=C\times_{X\times X,\Delta_X}X,
\qquad i_c:\Fix(c)\longrightarrow C,\quad d_c:\Fix(c)\longrightarrow X,
$$

where $i_c$ and $d_c$ are the two projections.
