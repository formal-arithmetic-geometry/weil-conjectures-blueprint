+++
id = "corollary-cup-product-pairing"
kind = "corollary"
title = "The cup product pairing"
order = 871
lean = ["AlgebraicGeometry.WeilSheaf.exists_traceCup_poincarePairing", "AlgebraicGeometry.WeilSheaf.exists_traceCup_isPerfect"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-compactification-refinement"]
+++
Let $X/k$ be smooth, proper and connected of pure dimension $d$, with
$k$ algebraically closed, and let $\Lambda$ be a field. For every $i$
the pairing

$$
\langle a,b\rangle=\operatorname{tr}_X(a\cup b),\qquad
H^i(X,\Lambda)\times H^{2d-i}(X,\Lambda)\longrightarrow\Lambda(-d),
$$

is perfect, and $\langle b,a\rangle=(-1)^i\langle a,b\rangle$. In
particular, if $d$ is odd and $\Lambda$ has characteristic zero, the
pairing on $H^d(X,\Lambda)$ is alternating, as for a compact complex
manifold of odd dimension.
