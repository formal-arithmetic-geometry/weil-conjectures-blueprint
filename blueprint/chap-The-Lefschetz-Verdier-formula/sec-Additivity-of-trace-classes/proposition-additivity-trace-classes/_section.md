+++
id = "proposition-additivity-trace-classes"
kind = "proposition"
title = "Additivity of trace classes"
order = 942
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_distTriang", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_isPullback"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-correspondence", "definition-trace-class-local-terms", "definition-pushforward-correspondence", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $c:C\to X\times X$ be a correspondence.

1. Let $\mathcal K$ be a finitely filtered complex on $X$ with
   underlying complex $K$ and graded pieces $K_a$ in $D^b_{\mathrm{ctf}}(X,A)$, and let
   $\tilde u:c_2^*\mathcal K\to c_1^!\mathcal K$ be a cohomological
   correspondence in the filtered derived category, with underlying
   correspondence $u$ on $K$ and graded pieces $u_a$ on $K_a$. Then
   $$
   \operatorname{Tr}_c(u)=\sum_a\operatorname{Tr}_c(u_a)
   \quad\text{in }H^0(\Fix(c),\omega_{\Fix(c)}).
   $$
2. Let $i:Z\to X$ be a closed immersion with open complement $U$ such
   that $c_1^{-1}(Z)\subset c_2^{-1}(Z)$, let $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
   $u$ be a cohomological correspondence on $(X,K)$. Then
   $$
   \operatorname{Tr}_c(u)=\operatorname{Tr}_c(u_U)+\operatorname{Tr}_c(u_Z),
   $$
   where $u_U$ and $u_Z$ are the graded pieces of the lift of
   Lemma [lemma-lift-correspondence-invariant-decomposition], and $u_Z$
   is the pushforward along $i$ and $C_Z\to C$ of the correspondence
   $u_{|Z}$ on $(Z,i^*K)$ for $c_Z:C_Z=(c_1^{-1}(Z))_{\mathrm{red}}\to
Z\times Z$ (Lemma [lemma-closed-piece-pushforward]).
