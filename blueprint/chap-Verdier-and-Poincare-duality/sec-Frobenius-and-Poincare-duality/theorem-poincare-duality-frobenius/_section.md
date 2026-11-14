+++
id = "theorem-poincare-duality-frobenius"
kind = "theorem"
title = "Poincaré duality and Frobenius"
order = 885
lean = ["AlgebraicGeometry.Etale.TateOrientation.conj_frobeniusOperator_eq_smul_inverse_dualMap", "AlgebraicGeometry.Etale.TateOrientation.roots_map_charpoly_frobeniusOperator", "AlgebraicGeometry.WeilSheaf.exists_traceCup_poincareDuality", "AlgebraicGeometry.WeilSheaf.exists_traceCup_poincarePairing", "AlgebraicGeometry.WeilSheaf.poincareDuality"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "proposition-construction-independence-rf-shriek", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0/\mathbf F_q$ be smooth and separated of pure dimension
$d$, let $X=X_0\times\overline{\mathbf F}_q$, and let
$(K,\phi_K)$ be a Weil complex on $X$ (Definition [definition-weil-structure])
with $K$ locally perfect.
Equip the dual with the contragredient Weil structure

$$
\operatorname{Fr}_X^*K^\vee
\simeq(\operatorname{Fr}_X^*K)^\vee
\xrightarrow{\ (\phi_K^{-1})^\vee\ }K^\vee.
$$

For every admissible $\Lambda$ the Poincaré pairing $\beta_K$ of (10.7)
is a morphism of Weil complexes. Thus, with $F$ the Frobenius operators
defined above, the pairing
$H^i_c(X,K)\times H^{2d-i}(X,K^\vee(d))\to\Lambda$ satisfies
$\langle Fx,Fy\rangle=\langle x,y\rangle$, and the pairing
$H^i_c(X,K)\times H^{2d-i}(X,K^\vee)\to\Lambda(-d)$ satisfies

$$
\langle Fx,Fy\rangle=q^d\langle x,y\rangle.
$$

If $\Lambda$ is a field, then $F$ is invertible on $H^i_c(X,K)$, and
with respect to the second pairing $F$ on $H^{2d-i}(X,K^\vee)$ is $q^d$
times the inverse transpose of $F$ on $H^i_c(X,K)$. Hence the two
spaces have the same dimension $b$, the eigenvalues of $F$ on
$H^{2d-i}(X,K^\vee)$ are the $q^d/\alpha$, with multiplicities, where
$\alpha$ ranges over the eigenvalues on $H^i_c(X,K)$, and
$\det(F\mid H^i_c(X,K))\det(F\mid H^{2d-i}(X,K^\vee))=q^{db}$.
