+++
id = "lemma-reciprocal-roots-zeta"
kind = "lemma"
title = "Reciprocal roots of the zeta function"
order = 1389
lean = ["AlgebraicGeometry.Scheme.integral_recovery"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "corollary-point-counting-zeta-function", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0/\mathbf F_q$ be smooth proper of pure dimension $d$, let
$Z(X_0,T)=A/B$ be the reduced fraction fixed above, and let
$\ell\nmid q$ be a prime. Then

$$
A=\prod_{i\ \mathrm{odd}}P_{i,\ell},\qquad
B=\prod_{i\ \mathrm{even}}P_{i,\ell}
\quad\hbox{in }\mathbf Q_\ell[T].
\tag{19.2}
$$

Every reciprocal root $a\in\overline{\mathbf Q}$ of $A$ or of $B$ is a
nonzero algebraic integer, and there is an integer $i$, odd for $A$
and even for $B$, such that $|\tau(a)|=q^{i/2}$ for every field
embedding $\tau:\mathbf Q(a)\hookrightarrow\mathbf C$ and such that
$\theta(a)$ is a Frobenius eigenvalue on $H^i_\ell$ for every field
embedding $\theta:\overline{\mathbf Q}\hookrightarrow\overline{\mathbf Q}_\ell$.
