+++
id = "definition-exceptional-base-change-finite"
kind = "definition"
title = "The base change map for $f^!$, finite coefficients"
order = 539
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to S$ be separated and of finite type, let $g:S'\to S$ be a
morphism, let $X'=X\times_SS'$, and let $f':X'\to S'$, $g':X'\to X$ be the
projections. For $N\in D(S_{\acute{e}t},A)$, let
$\varepsilon_N:Rf_!f^!N\to N$ be the counit of $Rf_!\dashv f^!$. The
*base change map*

$$
\beta_N:g'^*f^!N\longrightarrow f'^!g^*N
\tag{6.1}
$$

is the transpose, for $f'$, of the morphism

$$
Rf'_!g'^*f^!N
\xrightarrow{\ \sim\ }g^*Rf_!f^!N
\xrightarrow{g^*\varepsilon_N}g^*N,
\tag{6.2}
$$

where the first arrow is the inverse of the base change isomorphism
for $Rf_!$ (Proposition [proposition-composition-base-change-rf-shriek](2)).
