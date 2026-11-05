+++
id = "lemma-additivity-open-subscheme-complement"
kind = "lemma"
title = "Additivity for an open subscheme and its complement"
order = 1003
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.trace_compactPullback_comp_eq_add", "AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.openPieceCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.closedPieceCoefficient"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-categorical-trace", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
