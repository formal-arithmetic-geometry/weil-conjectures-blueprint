+++
id = "sk-def-pe-classical-definition"
kind = "definition"
title = "Classical pro-étale sheaves"
lean = ["AlgebraicGeometry.ProEtale.IsClassicalModuleSheaf"]
order = 78
uses = ["sk-def-pe-site", "sk-prop-pe-affine-basis"]
tags = ["sketch"]
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
