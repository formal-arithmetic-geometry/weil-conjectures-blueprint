+++
id = "sk-prop-pe-continuous-cohomology"
kind = "proposition"
title = "Continuous cohomology as pro-étale cohomology"
order = 113
lean = ["AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi", "CategoryTheory.Pretriangulated.IsHomotopyLimit.map", "DerivedCategory.shortExact_milnor_of_isHomotopyLimit"]
uses = ["sk-prop-pe-replete", "sk-prop-pe-milnor", "sk-prop-sf-comparison"]
tags = ["sketch"]
+++
Let $X$ be a scheme and $(F_n)$ an inverse system of abelian sheaves
on $X_{\mathrm{pro}\acute{e}t}$ with epimorphic transition maps.
Put $F=\varprojlim_nF_n$ in the pro-étale topos. Then, in the
derived category of abelian groups,

$$
R\Gamma(X_{\mathrm{pro}\acute{e}t},F)
\simeq R\varprojlim_n R\Gamma(X_{\mathrm{pro}\acute{e}t},F_n).
$$
