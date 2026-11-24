+++
id = "proposition-continuous-cohomology-pro-etale-cohomology"
kind = "proposition"
title = "Continuous cohomology as pro-étale cohomology"
order = 192
lean = ["AlgebraicGeometry.ProEtale.continuousCohomology"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site"]
+++
Let $X$ be a scheme and $(F_n)$ an inverse system of abelian sheaves
on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) with epimorphic transition maps.
Put $F=\varprojlim_nF_n$ in the [pro-étale topos](@proposition-topos-functoriality). Then, in the
derived category of abelian groups,

$$
R\Gamma(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},F)
\simeq R\varprojlim_n R\Gamma(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},F_n).
$$
