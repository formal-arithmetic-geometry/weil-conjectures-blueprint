+++
id = "lemma-scheme-frobenius-geometric-frobenius"
kind = "lemma"
title = "Scheme Frobenius and geometric Frobenius"
order = 954
lean = ["AlgebraicGeometry.Etale.leftDerivedUpperStarGeometricFiberFrobeniusIso", "AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.globalOperator_eq_frobeniusCompactOperator", "AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.iterateStr_hom_eq_frobeniusCoefficientIterate"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-weil-structure", "definition-frobenius-operator", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $\operatorname{Fr}_X$ be the semilinear geometric Frobenius
of Definition [definition-weil-structure], and for a morphism
$\phi:\operatorname{Fr}_X^*K\to K$ put
$\phi_m=\phi\circ \operatorname{Fr}_X^*\phi\circ\cdots\circ(\operatorname{Fr}_X^{m-1})^*\phi$.
There are natural isomorphisms

$$
\kappa_m:(\Phi_X^m)^*K\xrightarrow{\sim}(\operatorname{Fr}_X^m)^*K
$$

compatible with iteration. For a Weil structure
$\phi:\operatorname{Fr}_X^*K\xrightarrow{\sim}K$, put
$\psi=\phi\kappa_1$. Then

$$
\psi_m=\phi_m\kappa_m,
\qquad T_{c_m}(\psi_m)=\operatorname{Frob}_{X,K}^{m},
$$

where $\operatorname{Frob}_{X,K}$ is the geometric Frobenius operator
on compact cohomology of
Definition [definition-frobenius-operator]. The same identity of
operators holds for an arbitrary morphism $(\operatorname{Fr}_X^m)^*K\to K$ in place
of $\phi_m$.
