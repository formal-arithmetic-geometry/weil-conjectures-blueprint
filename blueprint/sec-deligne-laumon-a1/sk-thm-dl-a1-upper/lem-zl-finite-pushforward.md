+++
id = "lem-zl-finite-pushforward"
kind = "lemma"
title = "Finite pushforward preserves upper weights"
lean = ["AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerStar_of_isFinite", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerStar_of_isClosedImmersion"]
order = 3133
uses = ["def-weil-complex-weights", "sk-def-sfb-bounded-constructible", "sk-def-sf-weil-complexes", "def-weil-pbc-scheme-conventions", "prop-functor-package"]
+++
If $g:Z_0\to Y_0$ is finite and
$K\in D_{\le w}(Z_0)$ is a Weil complex with underlying object in
$\Dbc(Z,\Qlb)$ ([sk-def-sfb-bounded-constructible], [sk-def-sf-weil-complexes],
[def-weil-complex-weights]), then $Rg_*K=Rg_!K$ belongs to
$D_{\le w}(Y_0)$.
