+++
id = "lemma-weil-pbc-fibre-product-limit"
kind = "lemma"
title = "Base change commutes with the neighbourhood limit"
lean = ["AlgebraicGeometry.Scheme.isLimitStrictLocalizationConePullback"]
order = 1016
uses = ["def-weil-pbc-strict-henselization-limit"]
+++
Let $\bar s$ be a geometric point of a scheme $S$. For every morphism
$f:X\to S$, the projections induce an isomorphism

$$
 X\times_SS_{(\bar s)}\xrightarrow{\sim}
 \varprojlim_{(V,\bar v)}X\times_SV,
$$

the limit running over the affine pointed etale neighbourhoods of $\bar s$
([def-weil-pbc-strict-henselization-limit]).
