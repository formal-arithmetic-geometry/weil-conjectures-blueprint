+++
id = "thm-sf-dual-perfect"
kind = "theorem"
title = "The dual of a perfect complex"
lean = ["CategoryTheory.MonoidalClosed.ihomCurry_comp_map_ihomIsoIhomUnitTensor_hom", "CategoryTheory.MonoidalClosed.map_ihomIsoIhomUnitTensor_hom", "AlgebraicGeometry.ProEtale.verdierDualIsoDerivedDualTensor", "AlgebraicGeometry.ProEtale.whiskerLeft_verdierDualIsoDerivedDualTensor_hom_app_comp", "AlgebraicGeometry.ProEtale.isDualizable_verdierDual", "AlgebraicGeometry.ProEtale.isIso_toIhomIhomUnit", "AlgebraicGeometry.ProEtale.toIhomIhom_comp_verdierDualVerdierDualIso_hom", "AlgebraicGeometry.ProEtale.isIso_toIhomIhom_dualizingComplex", "AlgebraicGeometry.ProEtale.verdierDualEquivalenceOfIso"]
order = 3509
uses = ["cor-pur-adic-and-rational-smooth-dualizing-complexes", "cor-pur-finite-stage-smooth-dualizing-complex", "thm-pur-finite-reduction-of-purity", "def-pod-conventions", "def-sf-datum", "def-sf-orientation", "def-weil-derived-pullback-tensor-hom", "lem-sf-hom-finite-projective", "lem-sf-twist-interchange", "prop-sf-dualizable", "prop-sf-dualizable-hom"]
+++
In the Poincare duality conventions of [def-pod-conventions] (an
instance of the setting of [def-sf-datum], with $X$ smooth,
separated of finite type and of pure dimension $d$), let
$K\in D^b_{ctf}(X,\Lambda)$ be perfect over $\Lambda_X$, at any
admissible coefficient ring $\Lambda\in\{A_{E,n},\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$.
The smooth dualizing-complex identification
$\eta_X:\omega_{X,\Lambda}\xrightarrow{\ \sim\ }\Lambda_X(d)[2d]$ of the
purity chapter (at the finite stage, the case $f=a_X$ of an orientation
datum in the sense of [def-sf-orientation]) and the twist interchange give a canonical isomorphism

$$
\mathbb D_XK\xrightarrow{\ \sim\ }K^\vee(d)[2d],
$$

natural in $K$, compatible with finite reduction, scalar extension,
shifts, and the canonical evaluation. Moreover $K^\vee$ is perfect, the
canonical map $K\to K^{\vee\vee}$ is an isomorphism, and consequently
$\mathbb D_X$ restricts to an anti-equivalence on the perfect objects,
the biduality $K\to\mathbb D_X\mathbb D_XK$ being, under this
identification, the coefficient-dual biduality $K\to K^{\vee\vee}$.

*Relative form.* The same holds for a smooth separated finite-type
$f:X\to Y$ of pure relative dimension $d$ over an arbitrary base $Y$ of the
setting: with the orientation $\gamma_f:\Lambda_X(d)[2d]\xrightarrow{\sim}
Rf^!\Lambda_Y$ of [def-sf-orientation] and
$\mathbb D_{X/Y}K=R\mathcal Hom_X(K,Rf^!\Lambda_Y)$, the composite of
$R\mathcal Hom_X(K,\gamma_f^{-1})$ with the twist interchange is a natural
isomorphism $\mathbb D_{X/Y}K\xrightarrow{\sim}K^\vee(d)[2d]$ for perfect
$K$, with the same biduality statement; the absolute case is $f=a_X$.
