+++
id = "lemma-additivity-open-subscheme-complement"
kind = "lemma"
title = "Additivity for an open subscheme and its complement"
order = 1003
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.closedPieceCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.openPieceCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.trace_compactPullback_comp_eq_add"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "definition-trace-function", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $j_0:U_0\hookrightarrow X_0$ be open with reduced closed
complement $i_0:Z_0\to X_0$, and let $K\in D^b_{\mathrm{ctf}}(X,A)$. A Frobenius
correspondence $\psi$ on $K$ induces Frobenius correspondences on
$j^*K$, $i^*K$, $j_!j^*K$ and $Ri_*i^*K$, whose stalk maps are the
restrictions of $\psi_m$. Writing $T_{c_m}$ also for the endomorphisms
of $R\Gamma_c$ induced by the Frobenius correspondences on $U$ and $Z$, for
every $m\geq1$

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X,K))
=\operatorname{tr}_A(T_{c_m}\mid R\Gamma_c(U,j^*K))
+\operatorname{tr}_A(T_{c_m}\mid R\Gamma_c(Z,i^*K)).
$$
