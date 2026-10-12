+++
id = "thm-zl-wme-deligne-estimate"
kind = "theorem"
title = "General $Rf_!$ weight theorem"
order = 3189
lean = ["AlgebraicGeometry.LAdicWeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek"]
uses = ["def-weil-complex-weights", "def-weil-pbc-qbar-category", "lem-zl-sheaves-to-complexes"]
+++
For every separated finite-type morphism $f:X_0\to Y_0$ of separated
finite-type $k_0$-schemes and every constructible $\Qlb$-Weil complex
$K$ (in the coefficient categories of
[def-weil-pbc-qbar-category]),

$$
K\in D_{\le w}(X_0)\quad\Longrightarrow\quad Rf_!K\in D_{\le w}(Y_0),
$$

where $D_{\le w}$ is the complex-weight predicate of
[def-weil-complex-weights].
