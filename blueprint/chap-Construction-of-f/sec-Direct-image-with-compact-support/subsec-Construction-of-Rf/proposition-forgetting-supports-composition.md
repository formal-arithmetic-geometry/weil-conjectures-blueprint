+++
id = "proposition-forgetting-supports-composition"
kind = "proposition"
title = "Forgetting supports and composition"
order = 514
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekToLowerStarComp_of_isProper", "AlgebraicGeometry.Etale.properShriekComp_comp_forgetSupports"]
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
