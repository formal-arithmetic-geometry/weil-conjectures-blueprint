+++
id = "theorem-weights-rf-shriek--2"
kind = "theorem"
title = "Weights of compactly supported cohomology with constant coefficients"
name_showing = false
order = 1084002
aliases = ["bp-r333-2"]
lean = ["AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_adicConstant"]
uses = ["definition-weights", "definition-frobenius-operator"]
+++
The mainline uses the following constant-coefficient case of the
compact-support bound. Let $X_0$ be separated of finite type over
$k_0=\Fq$, put $X=X_0\times_{k_0}\Fbar$, and fix a prime $\ell\nmid q$
and an embedding $\iota:\Qbarl\hookrightarrow\C$. For every
$n\in\Z$, each eigenvalue $\alpha$ of geometric Frobenius on
$H_c^n(X,\Qbarl)$ satisfies

$$
|\iota(\alpha)|\leq q^{n/2}.
$$
