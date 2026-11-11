+++
id = "corollary-functional-equation"
kind = "corollary"
title = "Functional equation"
order = 1045
lean = ["AlgebraicGeometry.Scheme.functional_equation_frobeniusCharpolyRev"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0/\mathbf F_q$ be smooth and proper of pure dimension $d$, and let
$\ell\nmid q$. Put $H^i=H^i(X_{\mathrm{pro}\acute{e}t},\mathbf Q_\ell)$, let $F_i$ be the Frobenius operator $F$ on $H^i$
(Section [sec-Weil-complexes]), and put

$$
b_i=\dim_{\mathbf Q_\ell}H^i,\qquad \chi=\sum_i(-1)^ib_i,\qquad
D=\prod_i\det(F_i)^{(-1)^i}.
$$

Then $b_{2d-i}=b_i$, $d\chi$ is even, $D^2=q^{d\chi}$, and in $\mathbf Q_\ell(T)$

$$
Z\!\left(X_0,\frac1{q^dT}\right)=(-1)^{\chi}D\,T^{\chi}\,Z(X_0,T)
=\varepsilon q^{d\chi/2}T^{\chi}Z(X_0,T),
\qquad \varepsilon=(-1)^\chi Dq^{-d\chi/2}\in\{1,-1\}.
$$
