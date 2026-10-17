+++
id = "lem-zl-relative-curve-mixedness"
kind = "lemma"
title = "Mixedness of the direct images over a relative affine curve"
order = 3187
lean = ["AlgebraicGeometry.exists_isMixedOfWeightsAtMost_higherLowerShriek_of_isAffine_fiber"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "def-weil-scheme-morphism-properties", "def-wf-constant-weil-twist", "lem-a1-mixed-direct-summand", "lem-wf-constant-twist-cohomology", "sk-def-sf-weil-complexes", "sk-lem-coefficient-heart", "sk-thm-sf-ctf-stability", "sk-thm-sfb-shriek-base-change"]
+++
Fix the coefficient and weight conventions of
[def-weil-punctual-weights]. Let $h:U_0\to Y_0$ be a
smooth separated morphism
between separated finite-type
$k_0$-schemes, with every nonempty geometric fiber a smooth affine curve,
and let $\mathcal F$ be a
lisse
$\Qlb$-Weil sheaf (a lisse $\Qlb$-module on $U_{\mathrm{proét}}$
[sk-lem-coefficient-heart] with a Weil structure [sk-def-sf-weil-complexes]) that is
punctually $\iota$-pure of weight
$w$. Then for every $i$ there is a real number $u_i$ such that
$R^ih_!\mathcal F$ is
$\iota$-mixed of weights at most
$u_i$.
