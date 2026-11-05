+++
id = "lemma-change-coefficients-exceptional-inverse-image--4"
kind = "lemma"
title = "Exceptional inverse image: finite extension of coefficient fields for proper morphisms"
order = 640008
aliases = ["bp-r195-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_mateEquiv_boundedConstructibleLowerStarExtendScalarsSubfield"]
uses = ["theorem-exceptional-inverse-image", "definition-sp-scalar-extension", "lemma-change-coefficients-direct-image"]
+++
Let $E\subset F\subset\overline{\mathbf Q}_\ell$ be finite extensions of
$\mathbf Q_\ell$, and assume that $f$ is proper. Write
$T_Z:\Dbc(Z,E)\to\Dbc(Z,F)$ for extension of scalars, for $Z=X,Y$.
Suppose that $Rf_{*,E}$ and $Rf_{*,F}$ have right adjoints, denoted by
$f^!_E$ and $f^!_F$. The adjoint transpose of the inverse of the
pushforward comparison
$$
T_Y(Rf_{*,E}L)\xrightarrow{\ \sim\ }Rf_{*,F}(T_XL)
$$
is a natural isomorphism
$$
T_X(f^!_E K)\xrightarrow{\ \sim\ }f^!_F(T_YK),
\qquad K\in\Dbc(Y,E).
$$
Here the right adjoints may be the chosen right adjoints of the proper
direct images; no compatibility with an integral model is assumed.
