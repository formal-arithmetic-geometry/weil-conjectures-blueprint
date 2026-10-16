+++
id = "def-sf-orientation"
kind = "definition"
title = "Orientation datum"
lean = ["AlgebraicGeometry.Etale.OrientationComparisonData", "AlgebraicGeometry.Etale.OrientationComparisonData.compIso", "AlgebraicGeometry.Etale.OrientationComparisonData.baseChangeIso", "AlgebraicGeometry.Etale.OrientationDatum", "AlgebraicGeometry.Etale.OrientationDatum.nonempty_iso_dualizingComplex", "AlgebraicGeometry.Etale.CoefficientChange", "AlgebraicGeometry.Etale.OrientationDatum.IsCompatibleCoefficientChange", "AlgebraicGeometry.Etale.ProEtaleRealization", "AlgebraicGeometry.Etale.OrientationDatum.IsCompatibleProEtaleRealization"]
order = 2391
uses = ["def-sf-datum"]
+++
In the setting of [def-sf-datum], an *orientation datum* consists
of, for every smooth separated finite-type $f:X\to Y$ of pure relative
dimension $d$, an isomorphism

$$
\gamma_{f,\Lambda_Y}:\ Lf^*\Lambda_Y(d)[2d]\xrightarrow{\ \sim\ }Rf^!\Lambda_Y,
$$

natural in $Y$, compatible with composition, with étale base change,
with finite reduction, scalar extension, and the pro-étale realization,
and equal to the canonical orientation of the affine line
$\mathbf A^1_Y\to Y$ on the projection; for $f=a_X$ it reads
$\omega_{X,\Lambda}\cong\Lambda_X(d)[2d]$.
