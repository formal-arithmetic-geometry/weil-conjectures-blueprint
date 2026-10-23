+++
id = "prop-sf-closed-unit-all-stages"
kind = "theorem"
title = "Closed direct image is fully faithful for every admissible coefficient ring"
lean = ["AlgebraicGeometry.ProEtale.full_boundedConstructible_\u03b9_comp_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.isIso_unit_app_boundedConstructible", "AlgebraicGeometry.ProEtale.full_rightDerivedFunctor_lowerStar_weilCoefficients", "AlgebraicGeometry.ProEtale.isIso_unit_app_weilCoefficients", "AlgebraicGeometry.ProEtale.full_boundedConstructibleAdic_\u03b9_comp_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.isIso_unit_app_boundedConstructibleAdic", "AlgebraicGeometry.ProEtale.fullyFaithfulBoundedConstructibleAdicRightDerivedLowerStar"]
order = 3225
tags = ["latex:proposition"]
uses = ["def-sf-setting", "det-def-sfb-pulled-back-coefficients", "sk-prop-sf-open-closed-triangle", "sk-thm-existence", "def-weil-derived-direct-image", "def-weil-exceptional-inverse-image", "prop-sf-closed-immersion-unit", "prop-weil-open-closed-recollement-adjunctions"]
+++
Let $i:Z\hookrightarrow X$ be a closed immersion of separated finite-type
$k$-schemes and let $\Lambda$ be one of the coefficient rings
$A_{E,n},\mathcal O_E,E,\Qlb$, regarded as condensed rings, with the
categories $D^b_c(-,\Lambda)\subseteq D(-_{\mathrm{proét}},\Lambda)$ of
[def-sf-setting] and the direct image $i_*=Ri_*=Ri_!$ of
[def-weil-derived-direct-image]. Then

$$
i_*:D(Z_{\mathrm{proét}},\Lambda)\longrightarrow D(X_{\mathrm{proét}},\Lambda)
$$

is fully faithful, and so is its restriction
$i_*:D^b_c(Z,\Lambda)\to D^b_c(X,\Lambda)$. Consequently, the right adjoint
$Ri^!$ of $i_*$ on these categories (the exceptional inverse image of
[def-weil-exceptional-inverse-image] at $\Lambda=A_{E,n}$, and of
[sk-thm-existence] in general) has unit an isomorphism

$$
Q\xrightarrow{\ \sim\ }Ri^!i_*Q\qquad(Q\in D^b_c(Z,\Lambda)).
$$

At $\Lambda=A_{E,n}$ the right adjoint exists on the ambient categories and
this is [prop-sf-closed-immersion-unit].
