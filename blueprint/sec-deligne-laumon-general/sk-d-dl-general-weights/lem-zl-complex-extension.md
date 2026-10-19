+++
id = "lem-zl-complex-extension"
kind = "lemma"
title = "Extension stability of complex weights"
lean = ["AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.of_distTriang"]
order = 3156
uses = ["def-weil-complex-weights", "def-weil-derived-cohomology-sheaves", "def-weil-frobenius-module-weights", "def-weil-weil-sheaf-complex", "def-weil-punctual-weights", "lem-a1-extension-bounds", "lem-a1-mixed-direct-summand", "lem-a1-subquotient-extension-bounds", "lem-sp-long-exact-of-triangle", "sk-def-sf-weil-complexes", "sk-def-sfb-bounded-constructible"]
+++
Let $K'\to K\to K''\to K'[1]$ be a distinguished triangle in
$\Dbc(X,\Qlb)$ ([sk-def-sfb-bounded-constructible]) between Weil complexes
([sk-def-sf-weil-complexes], [def-weil-weil-sheaf-complex]) whose three maps
commute with the Weil structures (for instance a functorial triangle of
Weil complexes). If $K'$ and $K''$ belong to

$$
D_{\le w}(X_0):=\{K:\Wt_{\iota,\leq w}(K)\}
$$

in the sense of [def-weil-complex-weights], then so does $K$.
