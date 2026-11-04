+++
id = "definition-pro-etale-base-change-map"
kind = "definition"
title = "Pro-étale base change map"
order = 321
lean = ["AlgebraicGeometry.ProEtale.derivedBaseChangeMap", "AlgebraicGeometry.ProEtale.CondensedRing.baseChangeMap"]
+++
Let $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$. The *base change map*

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
\tag{4.5}
$$

in $D(Y'_{\mathrm{pro}\acute{e}t},\Lambda)$ is the adjoint transpose, for
$f'^*\dashv Rf'_*$, of the composite

$$
f'^*g^*Rf_*K\simeq g'^*f^*Rf_*K
\xrightarrow{g'^*\varepsilon_f}g'^*K,
$$

where $\varepsilon_f:f^*Rf_*\to\mathrm{id}$ is the counit of
$f^*\dashv Rf_*$.
