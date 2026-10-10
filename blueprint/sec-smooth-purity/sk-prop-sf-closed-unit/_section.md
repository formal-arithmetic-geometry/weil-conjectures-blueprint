+++
id = "sk-prop-sf-closed-unit"
kind = "section"
title = "Closed-immersion unit"
order = 1852
uses = ["sk-def-sf-operations", "sk-prop-sf-existence"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekAdjunction_unit_app"]
+++
*Proposition (sketch).*

Let $\mathcal A$ be a Grothendieck abelian coefficient category (for
instance $\Lambda$-modules). For a closed immersion $i:Z\hookrightarrow X$ of
schemes admitting a compactification and every object $Q$ of the unbounded
derived category $D(Z_{\mathrm{et}},\mathcal A)$, the unit of the exceptional
adjunction $Ri_!\dashv Ri^!$ of [sk-def-sf-operations] is an isomorphism

$$
Q\xrightarrow{\ \eta_i^!\ }Ri^!Ri_!Q,
$$

where $Ri_!=Ri_*$ because $i$ is proper.

## Proof

The direct image $i_*$ of a closed immersion is exact, and so is $i^*$; the
counit $i^*i_*\to\operatorname{id}$ is an isomorphism — on geometric stalks
over $Z$ the two sides agree. Since both functors are exact they need no
deriving, so on the unbounded derived categories $Li^*Ri_*=i^*i_*\cong
\operatorname{id}$ and the counit of $Li^*\dashv Ri_*$ is an isomorphism;
hence $Ri_*:D(Z_{\mathrm{et}},\mathcal A)\to D(X_{\mathrm{et}},\mathcal A)$
is fully faithful. Since $i$ is proper, $Ri_!\cong Ri_*$ (computed with the
compactification $(\operatorname{id}_Z,i)$), so $Ri_!$ is fully faithful too,
and $Ri^!$ is its right adjoint ([sk-prop-sf-existence] (a), unconditional on
the ordinary étale derived categories). For every $P\in D(Z_{\mathrm{et}},
\mathcal A)$ the composite

$$
\operatorname{Hom}(P,Q)\xrightarrow{\ (\eta_i^!)_*\ }
\operatorname{Hom}(P,Ri^!Ri_!Q)\cong\operatorname{Hom}(Ri_!P,Ri_!Q)
$$

is the action of $Ri_!$ on morphisms, which is bijective by full
faithfulness; so $(\eta_i^!)_*$ is bijective for every $P$, and by Yoneda
$\eta_i^!:Q\to Ri^!Ri_!Q$ is an isomorphism.
