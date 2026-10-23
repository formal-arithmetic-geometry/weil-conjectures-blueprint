+++
id = "def-sf-orientation"
kind = "definition"
title = "Orientation datum"
lean = ["AlgebraicGeometry.Etale.OrientationComparisonData", "AlgebraicGeometry.Etale.OrientationComparisonData.compIso", "AlgebraicGeometry.Etale.OrientationComparisonData.baseChangeIso", "AlgebraicGeometry.Etale.OrientationDatum", "AlgebraicGeometry.Etale.OrientationDatum.nonempty_iso_dualizingComplex", "AlgebraicGeometry.Etale.CoefficientChange", "AlgebraicGeometry.Etale.OrientationDatum.IsCompatibleCoefficientChange", "AlgebraicGeometry.Etale.ProEtaleRealization", "AlgebraicGeometry.Etale.OrientationDatum.IsCompatibleProEtaleRealization"]
order = 3330
uses = ["def-sf-datum", "thm-weil-pbc-site-comparison", "def-sfb-finite-upper-shriek"]
+++
In the setting of [def-sf-datum], an *orientation datum* consists
of, for every smooth separated finite-type $f:X\to Y$ of pure relative
dimension $d$, an isomorphism

$$
\gamma_{f,\Lambda_Y}:\ Lf^*\Lambda_Y(d)[2d]\xrightarrow{\ \sim\ }Rf^!\Lambda_Y,
$$

natural in $Y$ (for every Cartesian square, $\gamma$ of the base-changed
morphism is the base change of $\gamma_{f,\Lambda_Y}$; in particular $\gamma$
is compatible with étale base change), compatible with composition, and equal
to the canonical orientation of the affine line $\mathbf A^1_Y\to Y$ on the
projection; for $f=a_X$ it reads $\omega_{X,\Lambda}\cong\Lambda_X(d)[2d]$.

*Change of coefficients.* Let $\Lambda'$ be a second finite coefficient ring
with a Tate twist datum. A *change of coefficients* $F$ from $\Lambda$ to
$\Lambda'$ consists of functors
$F_X:D(X_{\Et},\Lambda)\to D(X_{\Et},\Lambda')$ for all schemes $X$, together
with isomorphisms $F_X(\Lambda_X(d)[2d])\cong\Lambda'_X(d)[2d]$ for all
$d\in\mathbf Z$ and $F_X(Rf^!\Lambda_Y)\cong Rf^!\Lambda'_Y$ for all
compactifiable $f:X\to Y$; finite reduction and scalar extension are the
intended examples. Orientation data $\gamma$ over $\Lambda$ and $\gamma'$ over
$\Lambda'$ are *compatible with $F$* if, for every smooth separated
finite-type $f$ of pure relative dimension $d$, the image $F_X(\gamma_f)$
followed by $F_X(Rf^!\Lambda_Y)\cong Rf^!\Lambda'_Y$ equals
$F_X(\Lambda_X(d)[2d])\cong\Lambda'_X(d)[2d]$ followed by $\gamma'_f$.

*Pro-étale realization.* Let $\nu^*$ be the comparison functor from étale to
pro-étale sheaves [thm-weil-pbc-site-comparison]. A *pro-étale realization
datum* consists of isomorphisms $\nu^*(Rf^!\Lambda_Y)\cong Rf^!_{\mathrm{pro\acute et}}\Lambda_Y$
[def-sfb-finite-upper-shriek] for every smooth separated finite-type $f$ of
pure relative dimension $d$ whose étale $Rf^!$ is bounded below. A family of
pro-étale orientations
$\gamma^{\mathrm{pro\acute et}}_f:\nu^*(\Lambda_X(d)[2d])\cong Rf^!_{\mathrm{pro\acute et}}\Lambda_Y$
is *compatible with the realization* if each $\gamma^{\mathrm{pro\acute et}}_f$
is $\nu^*(\gamma_f)$ followed by the realization isomorphism.
