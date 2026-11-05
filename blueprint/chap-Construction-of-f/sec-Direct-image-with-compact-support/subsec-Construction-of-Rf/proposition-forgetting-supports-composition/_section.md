+++
id = "proposition-forgetting-supports-composition"
kind = "proposition"
title = "Forgetting supports and composition"
order = 519
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp", "AlgebraicGeometry.Etale.compactificationForgetSupports", "AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekToLowerStar", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationIso_hom_app_comp_toLowerStar"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
There is a natural map $\eta_f:Rf_!\to Rf_*$ on
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. For a compactification $f=pj$ it is

$$
Rp_*j_!\longrightarrow Rp_*Rj_*=Rf_*,
$$

where $j_!\to Rj_*$ is adjoint to the inverse of the counit
$j^*Rj_*\xrightarrow{\sim}\mathrm{id}$. It is independent of the
compactification, and the square

$$
\begin{CD}
Rg_!Rf_! @>{c^!_{g,f}}>> R(gf)_!\\
@V{Rg_*(\eta_f)\,\circ\,(\eta_g Rf_!)}VV @VV{\eta_{gf}}V\\
Rg_*Rf_* @>{c^*_{g,f}}>> R(gf)_*
\end{CD}
$$

commutes. Here $c^!_{g,f}$ is the composition map of
Proposition [proposition-composition-base-change-rf-shriek], and $c^*_{g,f}$ is the
composition map for ordinary direct images. If $f$ is proper, $\eta_f$
is an isomorphism; under these isomorphisms the two composition maps
agree whenever $f$ and $g$ are proper.
