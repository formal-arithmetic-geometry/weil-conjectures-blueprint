+++
id = "proposition-forgetting-supports-composition--3"
kind = "proposition"
title = "Forgetting supports and composition (3)"
name_showing = false
order = 519003
aliases = ["bp-r158-3"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekToLowerStarComp_of_isProper", "AlgebraicGeometry.Etale.rightDerivedLowerShriekIsoRightDerivedLowerStar", "AlgebraicGeometry.Etale.properShriekComp_comp_forgetSupports"]
uses = ["proposition-forgetting-supports-composition--1", "proposition-composition-base-change-rf-shriek"]
+++
Let $f:X\to Y$ be proper, with a chosen compactification $f=pj$, and
let $\mathcal A$ satisfy the hypotheses of
[proposition-forgetting-supports-composition--1]. On
$D(\et{X},\mathcal A)$ the intermediate map
$Rf_!\to Rp_*Rj_*$ is an isomorphism. Composing it with ordinary
direct-image composition gives the natural isomorphism

$$
\eta_f:Rf_!\xrightarrow{\sim}Rf_*.
$$

For composition, let $\Lambda$ be a finite commutative ring, let
$X\xrightarrow fY\xrightarrow gZ$ be proper morphisms, and let
$h:X\to Z$ be proper with a specified equality $h=gf$.
Let $c^!_{g,f}:Rg_!Rf_!\xrightarrow{\sim}Rh_!$ be the specified
compact-support composition map of
[proposition-composition-base-change-rf-shriek], transported along this
equality, and let $c^*_{g,f}:Rg_*Rf_*\xrightarrow{\sim}Rh_*$ be the
ordinary composition map. For every $K\in D(\et{X},\Lambda)$,

$$
\eta_h(K)\circ c^!_{g,f}(K)
=c^*_{g,f}(K)\circ\eta_g(Rf_*K)\circ Rg_!(\eta_f(K)).
$$

Naturality of $\eta_g$ identifies the last two factors with
$Rg_*(\eta_f(K))\circ\eta_g(Rf_!K)$, giving the composition square for
proper $f$ and $g$. In Lean, $c^!_{g,f}$ is the inverse of
`AlgebraicGeometry.Etale.properRouteCompIso`.
