+++
id = "proposition-function-sheaf-dictionary"
kind = "proposition"
title = "The function–sheaf dictionary"
order = 1029
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "definition-trace-function", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $\Lambda$ be as in Theorem [theorem-grothendieck-lefschetz-trace-formula],
let $m\geq1$, and let $K$, $L$ be Weil complexes in $D^b_{\mathrm{ctf}}(X,\Lambda)$.

1. For $g_0:W_0\to X_0$ and $w\in W_0(\mathbf F_{q^m})$,
   $t_{g^*K,m}(w)=t_{K,m}(g_0(w))$.
2. $t_{K\otimes^{\mathbf L}_\Lambda L,m}=t_{K,m}\,t_{L,m}$.
3. For $f_0:X_0\to Y_0$ and $y\in Y_0(\mathbf F_{q^m})$,
   $t_{Rf_!K,m}(y)=\sum_{x\in X_0(\mathbf F_{q^m}),\,f_0(x)=y}t_{K,m}(x)$.
4. For $U_0\subset X_0$ open with closed complement $Z_0$, and
   $j:U\to X$, $i:Z\to X$ the inclusions,
   $t_{K,m}=t_{j_!j^*K,m}+t_{i_*i^*K,m}$, where $t_{j_!j^*K,m}$ is
   $t_{K,m}$ on $U_0(\mathbf F_{q^m})$ and $0$ on $Z_0(\mathbf F_{q^m})$.
5. $\sum_{x\in X_0(\mathbf F_{q^m})}t_{K,m}(x)
  =\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{X,K}^m\mid
  R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)$.
