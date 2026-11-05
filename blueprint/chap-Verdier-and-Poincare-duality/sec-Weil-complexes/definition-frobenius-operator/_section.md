+++
id = "definition-frobenius-operator"
kind = "definition"
title = "Frobenius operator"
order = 878
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius", "AlgebraicGeometry.ProEtale.StrictWeilComplex.globalFrobenius", "AlgebraicGeometry.ProEtale.compactFrobenius"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "definition-weil-structure", "definition-frobenius-correspondences-their-operators", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
For a Weil complex $(K,\phi_K)$ on $T$, the *geometric Frobenius
operator* on compactly supported cohomology is the endomorphism

$$
\begin{gathered}
\operatorname{Frob}_{T,K}:R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K)
\xrightarrow{\ \operatorname{pb}_{\operatorname{Fr}_T}\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\operatorname{Fr}_T^*K)\\
\xrightarrow{\ R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\phi_K)\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K).
\end{gathered}
$$

Here $\operatorname{pb}_{\operatorname{Fr}_T}$ is the pullback along $\operatorname{Fr}_T$
constructed above.
