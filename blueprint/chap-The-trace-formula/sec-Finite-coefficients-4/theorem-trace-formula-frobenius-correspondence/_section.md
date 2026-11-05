+++
id = "theorem-trace-formula-frobenius-correspondence"
kind = "theorem"
title = "Trace formula for a Frobenius correspondence"
order = 1007
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.traceFormulaHolds_of_isModelFrobenius", "AlgebraicGeometry.ProEtale.CondensedRing.trace_frobeniusCompactOperator_eq_sum"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, put
$X=X_0\times_{\mathbf F_q}k$, let $A$ be any finite commutative
$\ell$-primary ring and $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
$\psi:\Phi_X^*K\to K$ be any Frobenius correspondence on $K$. For every
$m\geq1$, in $A$,

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K))
=\sum_{x\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x}).
$$
