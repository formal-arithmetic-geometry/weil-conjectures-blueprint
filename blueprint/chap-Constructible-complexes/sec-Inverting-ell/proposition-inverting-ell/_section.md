+++
id = "proposition-inverting-ell"
kind = "proposition"
title = "Inverting $\\ell$"
order = 303
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.integral_scalar_map_eq", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves"]
+++
Assume that the underlying topological space of $X$ is Noetherian (for
instance, that $X$ is of finite type over a field). A complex in
$\Dbc(X,\mathcal O_E)$ that is killed by inverting $\ell$ is killed by a
fixed power of $\ell$, and extension of scalars induces an equivalence

$$
\Dbc(X,\mathcal O_E)[\ell^{-1}]\xrightarrow{\ \sim\ }\Dbc(X,E),
$$

where the source category has the objects of $\Dbc(X,\mathcal O_E)$ and
Hom groups tensored with $E$.
