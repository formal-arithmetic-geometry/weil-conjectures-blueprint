+++
id = "sk-def-exchange"
kind = "definition"
title = "Derived base change map"
order = 175
lean = ["AlgebraicGeometry.Etale.baseChange", "AlgebraicGeometry.Etale.squareUpperStarIso", "AlgebraicGeometry.Etale.pullbackSquareComparison", "AlgebraicGeometry.Etale.baseChangeMap", "AlgebraicGeometry.Etale.baseChangeMap_naturality", "AlgebraicGeometry.Etale.baseChangeMap_app_pullSection", "AlgebraicGeometry.Etale.derivedUpperStarLowerStarAdjunctionPlus", "AlgebraicGeometry.Etale.baseChange_naturality", "AlgebraicGeometry.Etale.baseChange_eq_derivedBaseChangeMapPlus", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_eq_termwise"]
uses = ["sk-def-conv", "sk-def-pbc-conventions"]
tags = ["sketch"]
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
