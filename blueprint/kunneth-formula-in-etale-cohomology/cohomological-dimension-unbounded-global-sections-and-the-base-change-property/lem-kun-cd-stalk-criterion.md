+++
id = "lem-kun-cd-stalk-criterion"
kind = "lemma"
title = "Vanishing of a higher direct image, checked at a geometric point"
order = 6036
lean = ["AlgebraicGeometry.Etale.higherDirectImage_eq_zero_iff_stalk"]
uses = ["def-weil-pbc-strict-henselization-limit"]
+++
Let $f:X\to Y$ be a quasi-compact and quasi-separated morphism of schemes,
let $q\ge0$, and let $F$ be a torsion étale sheaf on $X_{\Et}$. Then
$R^qf_*F=0$ if and only if for every geometric point $\bar y$ of $Y$ the
filtered colimit of the groups $H^q(W\times_YX,F)$, taken over the pointed
étale neighbourhoods $(W,\bar w)$ of $\bar y$, vanishes.

## Proof

The sheaf $R^qf_*F$ is the sheafification of the presheaf
$W\mapsto H^q(W\times_YX,F)$ on $Y_{\Et}$, and its stalk at a geometric
point $\bar y$ of $Y$ is precisely the filtered colimit of these groups over
the pointed étale neighbourhoods of $\bar y$. The sheaf $R^qf_*F$ vanishes
if and only if all its geometric stalks vanish; hence the stated
equivalence.

Unresolved dependencies: def:weil-pbc-direct-image, def:weil-pbc-etale-sheaves, def:weil-pbc-geometric-stalks, def:weil-pbc-scheme-conventions, lem:weil-pbc-geometric-stalk-conservative
