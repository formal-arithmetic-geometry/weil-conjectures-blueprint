+++
id = "lem-tw-tate-twist-weight-shift"
kind = "lemma"
title = "Weight shift under a Tate twist"
lean = ["AlgebraicGeometry.WeilGroup.IsPunctuallyPure.tprod_tateLine", "AlgebraicGeometry.WeilGroup.HasWeightsAtMost.tprod_tateLine"]
order = 3987
uses = ["def-coefficient-twists-detailed", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-frobenius-module-weights", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "lem-tw-multiplicativity", "sk-def-sf-weil-complexes"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$ and a field embedding
$\iota:\Qlb\hookrightarrow\mathbf C$ as in
[def-weil-punctual-weights]. If a lisse
Weil sheaf $\mathcal F$ is
punctually $\iota$-pure of weight $w$, then its
Tate twist $\mathcal F(n)$ is
punctually $\iota$-pure of weight $w-2n$, for every
$n\in\mathbf Z$. The same shift holds for upper weight bounds: if
$\mathcal F$ is $\iota$-mixed of weights at most $w$, then
$\mathcal F(n)$ is $\iota$-mixed of weights at most $w-2n$.
