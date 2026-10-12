+++
id = "sk-thm-sf-tensor-hom"
kind = "theorem"
title = "Tensor–Hom form of the exchange"
order = 2506
uses = ["sk-def-sf-exchanges", "sk-def-sf-operations", "sk-lem-sf-mate", "sk-prop-sf-comparison", "sk-prop-sf-existence", "sk-rem-sf-pf-done", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_derivedHom_rightDerivedLowerShriek"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be a separated finite-type morphism of finite-type
$k$-schemes, with $f^!=Rf^!$ the constructible exceptional adjoint of
[sk-def-sf-operations] (vi) (no admissibility datum is assumed), and let
$M\in\Dctf(X,\Lambda)$ and $N\in\Dctf(Y,\Lambda)$. Then there is a canonical isomorphism

$$
Rf_*\RHom_X(M,f^!N)\xrightarrow{\ \sim\ }\RHom_Y(Rf_!M,N),
$$

in the ambient category $D^+(Y,\Lambda)$, natural in $M$ and $N$ and
compatible with finite reduction, scalar extension and shifts.
