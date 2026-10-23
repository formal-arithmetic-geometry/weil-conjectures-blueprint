+++
id = "thm-zl-wme-deligne-estimate"
kind = "theorem"
title = "General $Rf_!$ weight theorem"
order = 4087
lean = ["AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek"]
uses = ["def-weil-complex-weights", "def-weil-weil-sheaf-complex", "lem-zl-sheaves-to-complexes", "sk-def-sf-weil-complexes", "det-def-sfb-bounded-constructible", "sk-d-real-weights"]
+++
For every separated finite-type morphism $f:X_0\to Y_0$ of separated
finite-type $k_0$-schemes and every constructible $\Qlb$-Weil complex
$K$, that is, $K\in\Dbc(X,\Qlb)$ ([det-def-sfb-bounded-constructible])
with a Weil structure ([sk-def-sf-weil-complexes],
[def-weil-weil-sheaf-complex]),

$$
K\in D_{\le w}(X_0)\quad\Longrightarrow\quad Rf_!K\in D_{\le w}(Y_0),
$$

where $D_{\le w}$ is the complex-weight predicate of
[def-weil-complex-weights].
