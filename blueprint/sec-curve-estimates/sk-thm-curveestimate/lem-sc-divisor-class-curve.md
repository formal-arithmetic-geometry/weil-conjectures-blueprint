+++
id = "lem-sc-divisor-class-curve"
kind = "lemma"
title = "$\\operatorname{Pic}$ is the divisor class group for smooth curves"
lean = ["AlgebraicGeometry.Scheme.exists_divisorClassGroup_addEquiv_pic"]
order = 1393
uses = ["def-sc-curves", "def-sc-function-field", "def-sc-picard-group", "lem-sc-line-bundle-rational-section"]
+++
Let $C$ be a smooth connected curve over $k$
(proper or not; for a disconnected smooth curve the assertion holds
componentwise). The map

$$
\operatorname{Cl}(C)\to\operatorname{Pic}(C),\qquad
D\mapsto[\mathcal O_C(D)],
$$

is an isomorphism of abelian groups (the group law on $\operatorname{Pic}(C)$ being [def-sc-picard-group]).
