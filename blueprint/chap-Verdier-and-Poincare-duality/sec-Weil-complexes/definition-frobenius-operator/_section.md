+++
id = "definition-frobenius-operator"
kind = "definition"
title = "Frobenius operator"
order = 877
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius", "AlgebraicGeometry.ProEtale.compactFrobenius", "AlgebraicGeometry.ProEtale.StrictWeilComplex.globalFrobenius"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-pro-etale-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-perfect-complexes-geometric-point", "definition-weil-structure", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For a Weil complex $(K,\phi_K)$ on $T$, the *geometric Frobenius
operator* on compactly supported cohomology is the endomorphism

$$
\begin{gathered}
\operatorname{Frob}_{T,K}:R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K)
\xrightarrow{\ \text{pullback along }\operatorname{Fr}_T\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\operatorname{Fr}_T^*K)\\
\xrightarrow{\ R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\phi_K)\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K).
\end{gathered}
$$
