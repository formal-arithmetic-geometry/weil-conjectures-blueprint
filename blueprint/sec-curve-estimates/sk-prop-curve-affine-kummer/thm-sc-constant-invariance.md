+++
id = "thm-sc-constant-invariance"
kind = "theorem"
title = "Base-change invariance for constant sheaves"
lean = ["AlgebraicGeometry.IsConnectedCurve.bijective_fieldExtensionCohomologyMap_of_isAffine", "AlgebraicGeometry.IsConnectedCurve.natCard_sheafH_one_constantZMod_mul", "AlgebraicGeometry.IsConnectedCurve.bijective_fieldExtensionCohomologyMap", "AlgebraicGeometry.IsConnectedCurve.bijective_fieldExtensionCohomologyMap_of_isProper"]
order = 1429
uses = ["def-sc-curves", "def-sc-field-extension", "def-sc-genus", "lem-sc-compactification"]
+++
Let $k\subseteq k'$ be algebraically closed, let $C$ be a
smooth separated connected curve over $k$, let
$\overline C$ be a compactification of $C$
([lem-sc-compactification]; thus $\overline C=C$ when $C$
is proper), and let
$g:=g(\overline C)$ ([def-sc-genus]). Let $n\geq1$ be
prime to $\operatorname{char}k$.
For every $q\geq0$, the pullback map of
[def-sc-field-extension]

$$
\rho^q_{k'/k}(C,\mathbf F_n):H^q(C_{\Et},\mathbf F_n)
\longrightarrow H^q((C_{k'})_{\Et},\mathbf F_n)
$$

is an isomorphism. If moreover $C$ is affine and
$r:=\#(\overline C\setminus C)$ is the number of points at infinity,
then $H^1(C_{\Et},\mathbf F_n)$ is finite of order $n^{2g+r-1}$.
