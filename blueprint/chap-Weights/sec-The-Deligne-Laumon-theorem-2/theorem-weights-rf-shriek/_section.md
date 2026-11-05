+++
id = "theorem-weights-rf-shriek"
kind = "theorem"
title = "Weights of $Rf_!$"
order = 1084
lean = ["AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For every separated morphism of finite type $f:X_0\to Y_0$,

$$
Rf_!D_{\leq w}(X_0)\subset D_{\leq w}(Y_0).
$$

In particular, if $K\in D_{\leq w}(X_0)$, then
$H_c^n(X,K)$ has weights at most $w+n$.
