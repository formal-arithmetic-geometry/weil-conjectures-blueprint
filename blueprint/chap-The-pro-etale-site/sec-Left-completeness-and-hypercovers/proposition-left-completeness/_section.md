+++
id = "proposition-left-completeness"
kind = "proposition"
title = "Left completeness"
order = 97
lean = ["AlgebraicGeometry.Scheme.ProEt.left_complete_quasiIso", "DerivedCategory.isHomotopyLimit_truncGECone"]
uses = ["definition-small-pro-etale-site"]
+++
The standard $t$-structure on $D(X_{\mathrm{pro}\acute{e}t},\mathcal R)$ is left complete:
for every complex $K$ the natural map

$$
K\longrightarrow R\varprojlim_{n\geq0}\tau_{\geq-n}K
$$

is an isomorphism.
