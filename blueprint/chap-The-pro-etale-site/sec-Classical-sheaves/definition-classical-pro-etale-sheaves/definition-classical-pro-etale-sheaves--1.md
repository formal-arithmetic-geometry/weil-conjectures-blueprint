+++
id = "definition-classical-pro-etale-sheaves--1"
kind = "definition"
title = "Classical pro-étale sheaves (1)"
name_showing = false
order = 111001
aliases = ["bp-r030-1"]
lean = ["AlgebraicGeometry.ProEtale.AffinePresentation", "AlgebraicGeometry.ProEtale.IsClassical", "AlgebraicGeometry.ProEtale.continuityMap", "AlgebraicGeometry.ProEtale.IsClassicalModuleSheaf", "AlgebraicGeometry.ProEtale.IsClassicalModuleFor", "AlgebraicGeometry.ProEtale.IsClassicalModule"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1"]
+++
A sheaf $F$ on $X_{\mathrm{pro}\acute{e}t}$ is *classical* if, for every
pro-étale affine presentation $U=\varprojlim_i U_i$ with $U_i$ affine
and étale over $X$, its restriction maps induce a bijection

$$
\varinjlim_i F(U_i)\xrightarrow{\ \sim\ }F(U).
\tag{2.4}
$$
