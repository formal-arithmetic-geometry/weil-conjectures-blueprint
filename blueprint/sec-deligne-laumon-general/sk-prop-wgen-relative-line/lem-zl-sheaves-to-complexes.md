+++
id = "lem-zl-sheaves-to-complexes"
kind = "lemma"
title = "Passage from sheaves to complexes"
lean = ["AlgebraicGeometry.HasDirectImageWeightBound.isMixedOfWeightsAtMost_derivedLowerShriek", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.map_of_forall_toComplex"]
order = 4074
uses = ["def-weil-complex-weights", "thm-sp-truncation-e2", "def-weil-weil-sheaf-complex", "def-weil-punctual-weights", "lem-a1-extension-bounds", "lem-a1-subquotient-extension-bounds", "lemma-weil-pbc-hypercohomology-convergence", "prop-functor-package", "sk-def-sf-weil-complexes", "det-def-sfb-bounded-constructible", "sk-lem-coefficient-heart"]
+++
Suppose that, for a separated finite-type map $f:X_0\to Y_0$, every
mixed constructible $\Qlb$-Weil sheaf $\mathcal F$ ([sk-lem-coefficient-heart],
[def-weil-weil-sheaf-complex]) of weights at most $v$ has
$R^af_!\mathcal F$ mixed of weights at most $v+a$, for every $a$.
Then $Rf_!$ carries $D_{\le w}(X_0)$ into $D_{\le w}(Y_0)$; here
$D_{\le w}$ consists of Weil complexes $K\in\Dbc(-,\Qlb)$
([det-def-sfb-bounded-constructible], [sk-def-sf-weil-complexes]).
