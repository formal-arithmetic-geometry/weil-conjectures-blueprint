+++
id = "definition-classical-pro-etale-sheaves"
kind = "definition"
title = "Classical pro-étale sheaves"
order = 111
lean = ["AlgebraicGeometry.ProEtale.IsClassical", "AlgebraicGeometry.ProEtale.AffinePresentation", "AlgebraicGeometry.ProEtale.continuityMap", "AlgebraicGeometry.ProEtale.IsClassicalModuleSheaf", "AlgebraicGeometry.ProEtale.IsClassicalModuleComplex"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site"]
+++
A sheaf $F$ on $X_{\mathrm{pro}\acute{e}t}$ is *classical* if, for every
pro-étale affine presentation $U=\varprojlim_i U_i$ with $U_i$ affine
and étale over $X$, its restriction maps induce a bijection

$$
\varinjlim_i F(U_i)\xrightarrow{\ \sim\ }F(U).
\tag{2.4}
$$

A complex is classical if all its cohomology sheaves are
classical.
