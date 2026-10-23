+++
id = "sk-p-dl-general-relative-line"
kind = "theorem"
title = "Pure lisse sheaves over relative affine curves"
order = 4060
lean = ["AlgebraicGeometry.isMixedOfWeightsAtMost_higherLowerShriek_of_affineLine"]
uses = ["sk-d-real-weights", "sk-def-wrp-real-definition", "sk-thm-sf-comp-composition", "sk-prop-sf-cbc", "sk-cor-wft-curve-upper", "sk-prop-wrp-real-envelope", "sk-l-dl-a1-endpoints", "sk-thm-trace-transport", "sk-thm-sf-ctf-stability", "sk-i-dl-general-real", "sk-lem-wgen-punctual-cutoff"]
tags = ["sketch"]
+++
Let $h:U_0\to Y_0$ be smooth separated of relative dimension one,
with affine geometric fibres, and let $F$ be lisse and pure of weight
$w$. Then $R^ih_!F$ is mixed of weights at most $w+i$.

*Complement.* In particular this applies to an open subscheme
$U_0\subset\mathbf A^1_{Y_0}$ with its projection $h_0:U_0\to Y_0$,
for $Y_0$ a separated $k_0$-scheme of finite type: for every $r\ge0$,
$R^rh_{0!}F_0$ is $\iota$-mixed of weights at most $w+r$.
