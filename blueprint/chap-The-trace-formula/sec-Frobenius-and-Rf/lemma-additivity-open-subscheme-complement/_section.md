+++
id = "lemma-additivity-open-subscheme-complement"
kind = "lemma"
title = "Additivity for an open subscheme and its complement"
order = 1002
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.trace_compactPullback_comp_eq_add", "AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.openPieceCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.closedPieceCoefficient"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
