+++
id = "thm-zl-relative-affine-curve-core"
kind = "theorem"
title = "Pure lisse relative affine-curve step"
order = 4301
lean = ["AlgebraicGeometry.isMixedOfWeightsAtMost_higherLowerShriek_of_isAffine_fiber"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "def-weil-scheme-morphism-properties", "sk-lem-coefficient-heart"]
+++
Fix the coefficient and weight conventions of
[def-weil-punctual-weights]. Let $h:U_0\to Y_0$ be a
smooth separated morphism
between separated finite-type
$k_0$-schemes, with every nonempty geometric fiber a smooth affine
curve. Let $\mathcal F$ be a
lisse
$\Qlb$-Weil sheaf (lisse in $\Cons(U,\Qlb)$ [sk-lem-coefficient-heart]) that is
punctually $\iota$-pure of weight $w$.
Then for every $i$, $R^ih_!\mathcal F$ is $\iota$-mixed of weights
at most $w+i$.
