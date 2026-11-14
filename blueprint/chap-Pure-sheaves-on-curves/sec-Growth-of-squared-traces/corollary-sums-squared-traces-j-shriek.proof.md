+++
kind = "proof"
of = "corollary-sums-squared-traces-j-shriek"
order = 1215
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-trace-function", "proposition-weights-j-boundary-points", "lemma-growth-finite-corrections", "theorem-weights-sums-squared-traces", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
For $j_!$ the trace function is that of $\mathcal G$ extended by zero,
and for $j_*$ it differs from this at finitely many points of small
weight, which Lemma [lemma-growth-finite-corrections] allows us to
ignore.

The open curve $U_0$ is again smooth, geometrically connected and
affine, and Theorem [theorem-weights-sums-squared-traces] on $U_0$ gives
$\nu(\mathcal G)=w$. Extension by zero only adds zero traces, so
$\nu(j_!\mathcal G)=w$. The trace functions of $j_*$
and of the extension by zero differ only at the points of
$X_0-U_0$, by the trace function of the boundary stalks. These stalks
have weights at most $w$ by
Proposition [proposition-weights-j-boundary-points], so if $i$
denotes the inclusion of $X_0-U_0$, then
Lemma [lemma-bounds-squared-traces](2), applied to the sheaf
$i_*i^*j_*\mathcal G$, bounds the squared sum of the difference by
$Cq^{nw}$. Since $\nu(j_!\mathcal G)=w>w-1$,
Lemma [lemma-growth-finite-corrections] shows that
$\nu(j_*\mathcal G)$ is still $w$.
