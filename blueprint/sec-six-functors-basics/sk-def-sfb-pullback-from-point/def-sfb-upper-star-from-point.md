+++
id = "def-sfb-upper-star-from-point"
kind = "definition"
title = "The inverse image $p_X^*$ from the point"
order = 1492
uses = ["lem-sfb-point-upper-star-braided", "sk-def-sfb-finite-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.upperStarFromPoint"]
+++
For a scheme $X$ with structure morphism $\pi_X\colon X\to\Spec\Z$, define
$$
p_X^*:=\pi_X^*\circ p^*\colon\Sh(*_{\mathrm{proét}},\Ab)\longrightarrow\Sh(X_{\mathrm{proét}},\Ab),
$$
where $\pi_X^*$ is the pullback of [sk-def-sfb-finite-pushforward-pullback]
for $\mathcal A=\Ab$. Then $p_X^*$ is strong monoidal and braided.
