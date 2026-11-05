+++
id = "lemma-boundary-stalk"
kind = "lemma"
title = "The boundary stalk"
order = 1176
lean = ["AlgebraicGeometry.Scheme.isIso_unit_upperStarLowerStarAdjunction", "AlgebraicGeometry.WeilGroup.exists_equivalence_isLisse_stalk_directImage_boundaryStalk_eq_invariants"]
uses = ["lemma-stability", "definition-weil-representation"]
+++
Let $j:U_0\hookrightarrow X_0$ be a dense open in a smooth curve, let
$\mathcal F$ be a lisse Weil sheaf on $U_0$, and let $j_*$ be the
ordinary direct image of sheaves. Let $\bar z$ be a geometric point
over a point $z$ of $X_0-U_0$, and let $I_z$ be the inertia group at
$z$, acting on the local generic fibre $V$ of $\mathcal F$. There is a
canonical Frobenius-equivariant identification

$$
(j_*\mathcal F)_{\bar z}=V^{I_z}.
$$

If $\mathcal F$ extends to a lisse sheaf on $X_0$, the adjunction map
from that extension to $j_*\mathcal F$ is an isomorphism.
