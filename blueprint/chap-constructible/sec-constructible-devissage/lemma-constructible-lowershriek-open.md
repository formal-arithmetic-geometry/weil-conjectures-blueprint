+++
id = "lemma-constructible-lowershriek-open"
kind = "lemma"
title = "Extension by zero along an open immersion"
order = 1066
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.openImmersionLowerShriek"]
uses = ["lemma-openclosed-vanishing-lowershriek", "prop-constructible-open-closed"]
+++
If $\mathcal G\in\shv{\et U}$ is constructible, then so is
$j_!\mathcal G$.

## Proof

As before: $i^*j_!\mathcal G=0$ by
[lemma-openclosed-vanishing-lowershriek], and $j^*j_!\mathcal G\cong \mathcal G$ by the unit isomorphism of the adjunction $j_!\dashv j^*$
([sec-openclosed-setting]).
