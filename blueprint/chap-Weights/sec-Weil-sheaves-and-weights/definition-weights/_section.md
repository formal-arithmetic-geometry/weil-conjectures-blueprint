+++
id = "definition-weights"
kind = "definition"
title = "Weights, purity and mixedness"
name_showing = false
order = 1058
lean = ["AlgebraicGeometry.WeilGroup.IsOfWeight", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight", "AlgebraicGeometry.WeilSheaf.HasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost", "AlgebraicGeometry.WeilSheaf.IsMixed", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local"]
+++
Let $K$ be a constructible Weil sheaf on $X$, let $x$ be a closed point of
$X_0$, and let $\alpha$ be an eigenvalue of $\operatorname{Frob}_x$ on
$K_{\bar x}$. We say $\alpha$ has *$\iota$-weight $w$* if
$|\iota(\alpha)|=q_x^{w/2}$.

1. $K$ is *punctually $\iota$-pure of weight $w$*, or simply
   *pure of weight $w$*, if every such eigenvalue, at every closed
   point, has $\iota$-weight $w$.
2. $K$ is *punctually of weights $\le w$* if
   $|\iota(\alpha)|\le q_x^{w/2}$ for every such eigenvalue at every closed
   point.
3. $K$ is *$\iota$-mixed* if it has a finite filtration by Weil
   subsheaves whose nonzero quotients are pure, of possibly different real
   weights. It is *mixed of weights at most $w$*, or has
   *weights at most $w$*, if it has such a filtration whose nonzero
   quotients have weights at most $w$.

A bounded constructible Weil complex $K$ has *weights at most $w$* if
$\mathcal H^i(K)$ has weights at most $w+i$ for all $i$, and it is
*pure of weight $w$* if each nonzero $\mathcal H^i(K)$ is pure of
weight $w+i$.
