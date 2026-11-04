+++
id = "definition-kunneth-map"
kind = "definition"
title = "Künneth map"
order = 703
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.prodLowerStarExternalProduct", "AlgebraicGeometry.Etale.externalProductRightDerivedLowerStarMap"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $f_i:X_i\to Y_i$, $i=1,2$, be morphisms of separated $k$-schemes of
finite type, put $h=f_1\times f_2:X_1\times X_2\to Y_1\times Y_2$, and let
$M_i\in D^b_{\mathrm{ctf}}(X_i,A)$. The *Künneth map*

$$
Rf_{1*}M_1\boxtimes Rf_{2*}M_2
\longrightarrow Rh_*(M_1\boxtimes M_2)
\tag{8.3}
$$

is the adjoint transpose, for $h^*\dashv Rh_*$, of the morphism

$$
h^*(Rf_{1*}M_1\boxtimes Rf_{2*}M_2)
\simeq f_1^*Rf_{1*}M_1\boxtimes f_2^*Rf_{2*}M_2
\xrightarrow{\ \varepsilon_{f_1}\boxtimes\varepsilon_{f_2}\ }
M_1\boxtimes M_2,
$$

where $\varepsilon_{f_i}$ is the counit of $f_i^*\dashv Rf_{i*}$ and the first
isomorphism comes from $h^*p_i^*\simeq p_i^*f_i^*$.
