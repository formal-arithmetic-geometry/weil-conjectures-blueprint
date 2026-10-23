+++
id = "sk-prop-sf-closed-unit"
kind = "proposition"
title = "Closed-immersion unit"
order = 3220
uses = ["sk-prop-sf-open-closed-triangle", "sk-prop-sf-existence"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekAdjunction_unit_app"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian coefficient category (for
instance $\Lambda$-modules). For a closed immersion $i:Z\hookrightarrow X$ of
schemes admitting a compactification and every object $Q$ of the unbounded
derived category $D(Z_{\mathrm{et}},\mathcal A)$, the unit of the exceptional
adjunction $Ri_!\dashv Ri^!$ of [det-def-sf-operations] is an isomorphism

$$
Q\xrightarrow{\ \eta_i^!\ }Ri^!Ri_!Q,
$$

where $Ri_!=Ri_*$ because $i$ is proper.
