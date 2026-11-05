+++
id = "definition-derived-base-change-map"
kind = "definition"
title = "Derived base change map"
order = 317
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus"]
+++
For $K\in D^+(X_{\acute{e}t},\Lambda)$, the *base change map*

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
\tag{4.3}
$$

is the adjoint, under $f'^*\dashv Rf'_*$, of

$$
f'^*g^*Rf_*K
\simeq g'^*f^*Rf_*K
\xrightarrow{g'^*\varepsilon_f}g'^*K,
$$

where $\varepsilon_f:f^*Rf_*\to\mathrm{id}$ now denotes the derived
counit. The morphism is natural in $K$.
