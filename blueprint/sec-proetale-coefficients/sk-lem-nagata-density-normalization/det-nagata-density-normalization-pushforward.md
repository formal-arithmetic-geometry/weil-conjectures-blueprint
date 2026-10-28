+++
id = "det-nagata-density-normalization-pushforward"
kind = "lemma"
title = "Proper direct image through the schematic closure"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso"]
order = 1353
uses = ["det-nagata-density-normalization-sheaves"]
+++
In the situation of [det-nagata-density-normalization-sheaves], assume also
that $S$ is separated of finite type over $k$. For every
$K\in D^b_c(X,\Lambda)$ there is a canonical isomorphism in
$D^b_c(S,\Lambda)$

$$
Rp_*j_!K\simeq R(p\circ i)_*j_{Z,!}K ,
$$

natural in $K$: it is $Rp_*$ applied to the pushforward comparison
$j_!K\simeq Ri_*j_{Z,!}K$, followed by $Rp_*Ri_*\simeq R(p\circ i)_*$.
