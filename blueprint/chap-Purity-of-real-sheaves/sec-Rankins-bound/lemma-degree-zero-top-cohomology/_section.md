+++
id = "lemma-degree-zero-top-cohomology"
kind = "lemma"
title = "Degree zero and top cohomology"
order = 1153
lean = ["AlgebraicGeometry.WeilGroup.exists_globalSections_linearEquiv_invariants"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-weights", "definition-weil-representation", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $U_0/\mathbf F_q$ be a smooth geometrically connected curve, let
$\mathcal F$ be a lisse Weil sheaf on $U_0$, and let $V$ be its
geometric generic fibre, a representation of the geometric fundamental
group $\pi_1(U)$.  There are canonical
Frobenius-equivariant identifications

$$
H^0(U,\mathcal F)=V^{\pi_1(U)},\qquad
H_c^2(U,\mathcal F)=V_{\pi_1(U)}(-1).
$$

There is no compactly supported cohomology outside degrees $0,1,2$.
If $U_0$ is affine, $H_c^0(U,\mathcal F)=0$.
If $\mathcal F$ is punctually of weights $\le a$, the weights of $H^0$
are at most $a$ and those of $H_c^2$ at most $a+2$.  If $\mathcal F$
is pure of weight $a$, the two groups, when nonzero, are pure of weights
$a$ and $a+2$, respectively.
