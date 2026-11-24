+++
id = "definition-classical-pro-etale-sheaves"
kind = "definition"
title = "Classical pro-étale sheaves"
order = 111
lean = ["AlgebraicGeometry.ProEtale.IsClassicalModuleComplex", "AlgebraicGeometry.ProEtale.IsClassicalModuleSheaf"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality"]
+++
A sheaf $F$ on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) is *classical* if, for every
[pro-étale affine](@definition-ind-etale-pro-etale-weakly) presentation $U=\varprojlim_i U_i$ with $U_i$ affine
and étale over $X$, its restriction maps induce a bijection

$$
\varinjlim_i F(U_i)\xrightarrow{\ \sim\ }F(U).
\tag{2.4}
$$

A complex is classical if all its cohomology sheaves are
classical.
