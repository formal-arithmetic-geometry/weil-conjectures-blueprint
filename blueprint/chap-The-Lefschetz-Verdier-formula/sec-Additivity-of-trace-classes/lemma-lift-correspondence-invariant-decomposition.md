+++
id = "lemma-lift-correspondence-invariant-decomposition"
kind = "lemma"
title = "Lifting a correspondence to an invariant decomposition"
order = 930
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointOpenPieceCoeff_comp_map_counit"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $c:C\to X\times X$ be a correspondence, $i:Z\to X$ a closed
immersion with open complement $j:U\to X$, and suppose

$$
c_1^{-1}(Z)\subset c_2^{-1}(Z),
\qquad\text{equivalently }c_2^{-1}(U)\subset c_1^{-1}(U).
$$

Let $u$ be a cohomological correspondence on $(X,K)$, and write
$K_U=j_!j^*K$ and $K_Z=Ri_*i^*K$ for the two pieces of the localization
triangle $K_U\to K\to K_Z$. Then $u$ has a lift, unique up to
contractible choice, to a cohomological correspondence $\tilde u$ in the
filtered derived category on the two-step filtered complex given by this
triangle. Its graded pieces are cohomological correspondences $u_U$ on
$(X,K_U)$ and $u_Z$ on $(X,K_Z)$, and $\widehat u_Z$ restricted to $Z$ is

$$
Rc_{1Z!}c_{2Z}^*i^*K\simeq i^*\Theta K
\xrightarrow{i^*\widehat u}i^*K.
$$
