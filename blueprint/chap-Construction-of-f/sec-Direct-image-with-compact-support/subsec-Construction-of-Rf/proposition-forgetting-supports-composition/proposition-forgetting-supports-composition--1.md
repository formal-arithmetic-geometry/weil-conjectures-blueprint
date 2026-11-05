+++
id = "proposition-forgetting-supports-composition--1"
kind = "proposition"
title = "Forgetting supports and composition (1)"
name_showing = false
order = 519001
aliases = ["bp-r158-1"]
lean = ["AlgebraicGeometry.Etale.compactificationForgetSupports", "AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekToLowerStar", "AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp"]
uses = ["definition-compactification-refinement", "proposition-construction-independence-rf-shriek"]
+++
Let $\mathcal A$ be a Grothendieck abelian category with a closed symmetric
monoidal structure, additive tensor product, and functorial flat resolutions.
Write $D(\et{X},\mathcal A)$ for the unbounded derived category of
$\mathcal A$-valued sheaves on the small étale site of $X$.
For a compactification $c=(X\xrightarrow j\overline X\xrightarrow pY)$
of $f:X\to Y$, put $Rf_!^{\,c}=Rp_*j_!$. There is a natural map

$$
\eta_f^{\,c}:Rf_!^{\,c}=Rp_*j_!
\longrightarrow Rp_*Rj_*\xrightarrow{\sim}Rf_*.
$$

Here $j_!$ denotes the functor on derived categories induced by exact
extension by zero. The comparison $\alpha_j:j_!\to Rj_*$ is adjoint under
$j^*\dashv Rj_*$ to the inverse of the unit
$\mathrm{id}\xrightarrow{\sim}j^*j_!$ of $j_!\dashv j^*$. Thus, for
$K\in D(\et{X},\mathcal A)$,

$$
j_!K\xrightarrow{\mathrm{unit}}Rj_*j^*j_!K
\xrightarrow{Rj_*(\mathrm{unit}^{-1})}Rj_*K.
$$

The map $\eta_f^{\,c}$ is $Rp_*(\alpha_j)$ followed by ordinary direct-image
composition. For the chosen compactification, Lean names the intermediate
map to $Rp_*Rj_*$ `AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp`;
`AlgebraicGeometry.Etale.compactificationForgetSupports` includes the final
composition map for any $c$.
