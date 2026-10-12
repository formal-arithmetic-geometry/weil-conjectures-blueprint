+++
id = "sk-def-sfb-pulled-back-coefficients"
kind = "definition"
title = "Coefficients pulled back from the point"
order = 1532
uses = ["sk-def-sfb-pullback-from-point"]
lean = ["AlgebraicGeometry.ProEtale.condensedRingObj", "AlgebraicGeometry.ProEtale.coefficientRing", "AlgebraicGeometry.ProEtale.isCommMonObj_condensedRingObj"]
tags = ["sketch"]
+++
Let $\Lambda$ be a ring object of $\Sh(*_{\mathrm{proét}},\Ab)$, that is, a
condensed ring ([sk-def-sfb-ring-object]). For a scheme $X$, put
$$
\Lambda_X:=p_X^*\Lambda\in\Sh(X_{\mathrm{proét}},\Ab),
$$
where $p_X^*$ is the inverse image from the point
([sk-def-sfb-pullback-from-point]).

The ring object structure is transported along the strong monoidal functor
$p_X^*$. The unit is $\Z\cong p_X^*\Z\to p_X^*\Lambda$. The multiplication is
$$
p_X^*\Lambda\otimes p_X^*\Lambda\cong p_X^*(\Lambda\otimes\Lambda)\to p_X^*\Lambda .
$$
This makes $\Lambda_X$ a ring object of $\Sh(X_{\mathrm{proét}},\Ab)$, and
$\Lambda\mapsto\Lambda_X$ is a functor from ring objects of
$\Sh(*_{\mathrm{proét}},\Ab)$ to ring objects of $\Sh(X_{\mathrm{proét}},\Ab)$.
If $\Lambda$ is commutative, then so is $\Lambda_X$.
