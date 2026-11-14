+++
id = "theorem-weil-conjectures-smooth-proper-schemes"
kind = "theorem"
title = "The Weil conjectures for smooth proper schemes"
order = 1391
lean = ["AlgebraicGeometry.Scheme.riemann_hypothesis", "AlgebraicGeometry.Scheme.weil_betti", "AlgebraicGeometry.Scheme.weil_conjectures", "AlgebraicGeometry.Scheme.weil_functional_equation", "AlgebraicGeometry.Scheme.weil_integral_factors"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "corollary-point-counting-zeta-function", "corollary-functional-equation", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0/\mathbf F_q$ be smooth proper of pure dimension $d$, and let
$P_{i,\ell}$ be as above.

1. There are unique polynomials $P_i(T)\in\mathbf Z[T]$ with $P_i(0)=1$
   whose images in $\mathbf Q_\ell[T]$ are $P_{i,\ell}(T)$ for every prime
   $\ell\nmid q$, and
   $Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}$.
2. The reciprocal roots of $P_i$ are algebraic integers, and each of them
   has absolute value $q^{i/2}$ under every complex embedding.
3. The degrees $b_i=\deg P_i=\dim_{\mathbf Q_\ell}H^i_\ell$ do not depend on $\ell$,
   and $b_i=b_{2d-i}$. If $X_0$ is geometrically connected, then
   $P_0=1-T$, $P_{2d}=1-q^dT$, and $b_0=b_{2d}=1$.
4. Put $\chi=\sum_i(-1)^ib_i$. Then $d\chi$ is even and there
   is $\varepsilon\in\{1,-1\}$ such that
   $$
   Z\!\left(X_0,\frac1{q^dT}\right)
   =\varepsilon q^{d\chi/2}T^\chi Z(X_0,T)
   \quad\hbox{in }\mathbf Q(T).
   $$
