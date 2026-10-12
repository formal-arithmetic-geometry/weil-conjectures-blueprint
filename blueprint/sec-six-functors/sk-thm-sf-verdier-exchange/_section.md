+++
id = "sk-thm-sf-verdier-exchange"
kind = "theorem"
title = "Verdier-duality exchange"
order = 2508
uses = ["sk-def-sf-operations", "sk-lem-sf-mate", "sk-thm-sf-comp-composition", "sk-thm-sf-tensor-hom"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_dualizingComplex"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be a separated finite-type morphism of finite-type $k$-schemes,
with $Rf^!$ and the dualizing complexes $\omega_X=Ra_X^!\Lambda$,
$\omega_Y=Ra_Y^!\Lambda$ formed with the constructible exceptional adjoint of
[sk-def-sf-operations](vi) (no admissibility datum is assumed).
Then $Rf^!\omega_Y\cong\omega_X$, and for $M\in\Dctf(X,\Lambda)$ there is a canonical isomorphism

$$
\mathbb D_Y(Rf_!M)\xrightarrow{\ \sim\ }Rf_*\mathbb D_X(M),
$$

in the ambient category $D^+(Y,\Lambda)$, natural in $M$ and compatible with
finite reduction, scalar extension and shifts.
