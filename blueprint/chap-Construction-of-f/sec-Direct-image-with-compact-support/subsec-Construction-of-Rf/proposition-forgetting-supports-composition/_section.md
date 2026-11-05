+++
id = "proposition-forgetting-supports-composition"
kind = "proposition"
title = "Forgetting supports and composition"
order = 519
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp", "AlgebraicGeometry.Etale.compactificationForgetSupports", "AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekToLowerStar", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationIso_hom_app_comp_toLowerStar"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
