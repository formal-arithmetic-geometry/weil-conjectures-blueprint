+++
id = "sk-thm-sf-global-duality"
kind = "theorem"
title = "Global Verdier duality"
order = 2483
uses = ["sk-def-sf-operations", "sk-thm-sf-verdier-exchange"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_coefficientDual_rightDerivedLowerShriek"]
tags = ["sketch"]
+++
Let $X$ be smooth, separated of finite type and geometrically connected of
pure dimension $d$ over $k$ (no admissibility hypothesis on $a_X$: its
exceptional adjoint is the unconditional one of [sk-def-sf-operations](vi)).
Assume either that $X$ is proper, or that
$X=X_0\times_{k_0}k$ for a smooth, separated finite-type, geometrically
connected $k_0$-scheme $X_0$; in the latter case no properness is required.
For $K\in\Dctf(X,\Lambda)$ there is a canonical isomorphism

$$
\RG_c(X,K)^\vee\xrightarrow{\ \sim\ }\RG\bigl(X,\mathbb D_XK\bigr),
$$

in the point category $\Dbc(s,\Lambda)$ of def:weil-finite-coefficient-point,
natural in $K\in\Dctf(X,\Lambda)$ and compatible with finite reduction, scalar
extension and shifts; for $K=\Lambda_X$ it reads
$\RG_c(X,\Lambda)^\vee\cong\RG(X,\omega_X)$.
