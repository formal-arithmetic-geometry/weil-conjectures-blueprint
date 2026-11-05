+++
id = "theorem-weights-rf-shriek"
kind = "theorem"
title = "Weights of $Rf_!$"
order = 1084
lean = ["AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek", "AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_adicConstant"]
uses = ["definition-weil-structure", "definition-weights", "proposition-construction-independence-rf-shriek", "definition-frobenius-operator"]
+++
For every separated morphism of finite type $f:X_0\to Y_0$,

$$
Rf_!D_{\leq w}(X_0)\subset D_{\leq w}(Y_0).
$$

In particular, if $K\in D_{\leq w}(X_0)$, then
$H_c^n(X,K)$ has weights at most $w+n$.
