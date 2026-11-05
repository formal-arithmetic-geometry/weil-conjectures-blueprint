+++
id = "proposition-additivity-trace-classes"
kind = "proposition"
title = "Additivity of trace classes"
order = 943
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_distTriang", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_isPullback"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-correspondence", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
