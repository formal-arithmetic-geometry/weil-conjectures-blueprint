+++
id = "proposition-forgetting-supports-composition"
kind = "proposition"
title = "Forgetting supports and composition"
order = 519
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp", "AlgebraicGeometry.Etale.compactificationForgetSupports", "AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekToLowerStar", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationIso_hom_app_comp_toLowerStar"]
uses = ["definition-underived-base-change-map", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
There is a natural map $\eta_f:\href{@proposition-construction-independence-rf-shriek}{Rf_!}\to Rf_*$ on
[$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory). For a compactification $f=pj$ it is

$$
Rp_*j_!\longrightarrow Rp_*Rj_*=Rf_*,
$$

where $j_!\to Rj_*$ is adjoint to the inverse of the counit
$j^*Rj_*\xrightarrow{\sim}\mathrm{id}$. It is independent of the
compactification, and the square

$$
\begin{CD}
\href{@proposition-construction-independence-rf-shriek}{Rg_!}\href{@proposition-construction-independence-rf-shriek}{Rf_!} @>{c^!_{g,f}}>> \href{@proposition-construction-independence-rf-shriek}{R(gf)_!}\\
@V{Rg_*(\eta_f)\,\circ\,(\eta_g \href{@proposition-construction-independence-rf-shriek}{Rf_!})}VV @VV{\eta_{gf}}V\\
Rg_*Rf_* @>{c^*_{g,f}}>> R(gf)_*
\end{CD}
$$

commutes. Here $c^!_{g,f}$ is the composition map of
Proposition [proposition-composition-base-change-rf-shriek], and $c^*_{g,f}$ is the
composition map for ordinary direct images. If $f$ is proper, $\eta_f$
is an isomorphism; under these isomorphisms the two composition maps
agree whenever $f$ and $g$ are proper.
