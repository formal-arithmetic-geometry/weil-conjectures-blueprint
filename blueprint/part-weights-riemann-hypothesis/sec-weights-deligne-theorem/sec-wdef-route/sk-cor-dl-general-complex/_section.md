+++
id = "sk-cor-dl-general-complex"
kind = "theorem"
title = "Weights of $Rf_!$"
order = 640
lean = ["AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek"]
uses = ["sk-d-real-weights", "sk-thm-dl-general-sheaf", "sk-prop-cohsm"]
tags = ["sketch"]
+++
For every separated morphism of finite type $f:X_0\to Y_0$,

$$
Rf_!D_{\leq w}(X_0)\subset D_{\leq w}(Y_0).
$$

In particular, if $K\in D_{\leq w}(X_0)$, then
$H_c^n(X,K)$ has weights at most $w+n$.
