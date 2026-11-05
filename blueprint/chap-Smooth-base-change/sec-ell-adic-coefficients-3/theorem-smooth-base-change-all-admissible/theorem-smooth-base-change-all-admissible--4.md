+++
id = "theorem-smooth-base-change-all-admissible--4"
kind = "theorem"
title = "Algebraically closed coefficients"
order = 700008
aliases = ["bp-r210-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_smooth"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-pro-etale-base-change-map"]
+++
Let (8.1) be a cartesian square of separated schemes of finite type over a
field $k$ of characteristic $p>0$ different from $\ell$, and let $g$ be
smooth. For every $K\in\Dbc(X,\overline{\mathbf Q}_\ell)$, the map

$$
g^*_{\overline{\mathbf Q}_\ell}Rf_{*,\overline{\mathbf Q}_\ell}K
\longrightarrow
Rf'_{*,\overline{\mathbf Q}_\ell}g'^*_{\overline{\mathbf Q}_\ell}K
$$

is an isomorphism in $\Dbc(Y',\overline{\mathbf Q}_\ell)$.

Here $\Dbc$ is read in the module-object sense used in Lean: the complexes
are bounded, and each cohomology sheaf admits a finite stratification on
whose strata it is pro-étale locally finitely presented over the
coefficient sheaf. The entries of these local presentations are sections
of that sheaf; they are not required to come from the coefficient ring
at the point.
