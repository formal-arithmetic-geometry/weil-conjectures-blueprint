+++
id = "theorem-grothendieck-lefschetz-trace-formula"
kind = "theorem"
title = "Grothendieck–Lefschetz trace formula"
order = 1018
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula", "AlgebraicGeometry.WeilComplex.sum_trace_compactlySupportedCohomology_eq_sum_traceFunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "corollary-open-direct-image-over-field", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "lemma-perfect-complexes-geometric-point", "definition-weil-structure", "definition-categorical-trace", "definition-correspondence", "definition-frobenius-correspondences-their-operators", "definition-trace-function", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and suppose
that $\ell\nmid q$. Let

$$
\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\},
\qquad K\in D^b_{\mathrm{ctf}}(X,\Lambda),
$$

with a Weil structure as in Definition [definition-weil-structure].
Here $A$ is any finite commutative $\ell$-primary ring, and for
integral and rational coefficients, $D^b_{\mathrm{ctf}}(X,\Lambda)=\Dbc(X,\Lambda)$.
Let $\operatorname{Frob}_{X,K}$
be the geometric Frobenius on $R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)$, and let
$\operatorname{Frob}_{y,m}$ be the Frobenius acting on the stalk $K_{\bar y}$ at
$y\in X_0(\mathbf F_{q^m})$. Then for every $m\geq1$ we have, in $\Lambda$,

$$
\operatorname{tr}_{\Lambda}
\bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\Lambda}
\bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
\tag{12.3}
$$

The complexes inside the traces are perfect over $\Lambda$, and the
formula is compatible with the change-of-coefficients maps of
Proposition [proposition-six-operations-change-coefficients]. For $\Lambda=\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell$, it reads

$$
\sum_i(-1)^i\operatorname{Tr}
\bigl(\operatorname{Frob}_{X,K}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}\sum_j(-1)^j
\operatorname{Tr}\bigl(\operatorname{Frob}_{y,m}\mid H^j(K_{\bar y})\bigr),
\tag{12.4}
$$

where all sums over degrees are finite.
