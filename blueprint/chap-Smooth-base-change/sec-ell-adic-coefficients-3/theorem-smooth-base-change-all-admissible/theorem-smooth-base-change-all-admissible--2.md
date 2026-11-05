+++
id = "theorem-smooth-base-change-all-admissible--2"
kind = "theorem"
title = "Integral coefficients"
order = 700004
aliases = ["bp-r210-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_integral_app_of_reduction"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-pro-etale-base-change-map", "definition-derived-adic-completeness"]
+++
For the integral step, the reduction criterion does not require $g$ to be
smooth. Let (8.1) be a cartesian square of separated schemes of finite type
over a field $k$ of characteristic $p>0$, with $p\ne\ell$. Let
$E/\mathbf Q_\ell$ be finite, with a fixed embedding into
$\overline{\mathbf Q}_\ell$, and write $\mathbf F_E$ for its residue field.
For $K_0\in\Dbc(X,\mathcal O_E)$ put

$$
K_1=K_0\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathbf F_{E,X}.
$$

If the finite-coefficient base change map

$$
g^*_{\mathbf F_E}Rf_{*,\mathbf F_E}K_1
\longrightarrow Rf'_{*,\mathbf F_E}g'^*_{\mathbf F_E}K_1
$$

is an isomorphism, then so is

$$
g^*_{\mathcal O_E}Rf_{*,\mathcal O_E}K_0
\longrightarrow Rf'_{*,\mathcal O_E}g'^*_{\mathcal O_E}K_0.
$$

The integral map is taken in $\Dbc(Y',\mathcal O_E)$, and $Y'$ is
Noetherian under these hypotheses.

Here $\Dbc$ is read in the module-object sense used in Lean: the complexes
are bounded, and each cohomology sheaf admits a finite stratification on
whose strata it is pro-étale locally finitely presented over the
coefficient sheaf. The entries of these local presentations are sections
of that sheaf; they are not required to come from the coefficient ring
at the point.
