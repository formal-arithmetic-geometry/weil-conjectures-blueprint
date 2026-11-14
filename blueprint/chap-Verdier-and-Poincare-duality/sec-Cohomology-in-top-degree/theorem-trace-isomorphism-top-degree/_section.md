+++
id = "theorem-trace-isomorphism-top-degree"
kind = "theorem"
title = "The trace isomorphism in top degree"
order = 866
lean = ["AlgebraicGeometry.Etale.traceIsomorphism", "AlgebraicGeometry.WeilSheaf.traceIsomorphism_adicConstant"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "lemma-cohomology-modules-underlying-abelian", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "lemma-cohomology-projective-line-trace", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "theorem-smooth-base-change-classical-torsion", "theorem-smooth-base-change-classical-torsion-2", "lemma-kunneth-one-identity-factor", "proposition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "proposition-weights-under-usual-operations", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X/k$ be smooth, proper and connected of pure dimension
$d$, with $k$ algebraically closed. For every admissible
coefficient ring,

$$
H^i(X,\Lambda_X)=0\quad(i\notin[0,2d]),\qquad
H^0(X,\Lambda_X)=\Lambda,
$$

and the map

$$
\operatorname{tr}_X:H^{2d}(X,\Lambda_X)
\xrightarrow{\sim}\Lambda(-d),
$$

the twist by $(-d)$ of the map
$\operatorname{tr}_X(d):H^{2d}(X,\Lambda_X(d))\to\Lambda$ induced on
$H^{2d}$ by $\operatorname{Tr}_X$ of Definition [definition-trace-map],
is an isomorphism.
