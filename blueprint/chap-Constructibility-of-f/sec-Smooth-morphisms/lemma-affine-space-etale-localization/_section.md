+++
id = "lemma-affine-space-etale-localization"
kind = "lemma"
title = "Affine space and étale localization"
order = 557
lean = ["AlgebraicGeometry.Etale.affineSpaceAdjunction_baseChange", "AlgebraicGeometry.Etale.nonempty_rightDerivedLowerShriek_adjunction_affineSpace", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp_leftDerivedUpperStar_of_etale"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $S$ be of finite type over the base field $k$.

1. For the projection $p_d:\mathbf A^d_S\to S$, the right adjoint
   $p_d^!$ of $Rp_{d!}:D((\mathbf A^d_S)_{\acute{e}t},A)
\to D(S_{\acute{e}t},A)$ is $p_d^*(d)[2d]$. Its counit
   $Rp_{d!}p_d^*N(d)[2d]\to N$ is compatible with base change: for a morphism
   $g:S'\to S$ of finite type over $k$, with base change
   $p'_d:\mathbf A^d_{S'}\to S'$, the pullback $g^*$ of the counit for $N$ is,
   under the base change isomorphism for $Rp_{d!}$, the counit for $g^*N$.
   The same holds for the unit, which is determined by the counit through
   the triangle identities.
2. Let $f:X\to S$ be separated of finite type, let
   $N\in D(S_{\acute{e}t},A)$, and let $u:U\to X$ be separated, étale
   and of finite type. There is a canonical isomorphism
   $$
   u^*f^!N\simeq(fu)^!N
   \tag{6.10}
   $$
   under which the counit of $R(fu)_!\dashv(fu)^!$ is the composite
   $$
   R(fu)_!u^*f^!N\simeq Rf_!u_!u^*f^!N\longrightarrow Rf_!f^!N
   \longrightarrow N
   $$
   of the composition isomorphism, the counit of $u_!\dashv u^*$ and the
   counit of $Rf_!\dashv f^!$. For a second separated étale morphism
   $u':U'\to U$ of finite type, the isomorphism (6.10) for $uu'$ is
   the composite of $u'^*$ of (6.10) for $u$ and
   (6.10) for $u'$ and $fu$.
