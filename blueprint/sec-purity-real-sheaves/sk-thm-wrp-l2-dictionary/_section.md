+++
id = "sk-thm-wrp-l2-dictionary"
kind = "theorem"
title = "$L^2$ growth and pure weights"
lean = ["AlgebraicGeometry.WeilSheaf.l2Weight_eq_of_isPunctuallyPureOfWeight"]
order = 3914
uses = ["sk-def-wrp-l2-definition", "sk-def-wrp-real-definition", "sk-lem-wrp-hc2", "sk-lem-wrp-l2-growth", "sk-lem-wrp-positive-euler", "sk-prop-wrp-real-envelope", "sk-thm-trace-transport"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be a smooth geometrically connected affine curve.
For every nonzero pure lisse Weil sheaf $\mathcal G$ of weight $w$,

$$
 \nu(\mathcal G)=w
$$

in the sense of [sk-def-wrp-l2-definition].

*Complement.* Consequently, if $N\ne0$ is lisse and pure of weight $v$ on
$X_0$ and $S_n(N)\le Cq^{nB}$ for every $n\ge1$, with $C$ independent of $n$,
then $v\le B-1$ ([det-l-dl-a1-energy]).
