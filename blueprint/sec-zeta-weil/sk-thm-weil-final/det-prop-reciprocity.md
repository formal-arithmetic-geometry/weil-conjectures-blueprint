+++
id = "det-prop-reciprocity"
kind = "proposition"
title = "Duality reciprocity of the factors"
lean = ["TraceDatum.det_mul_det_rev_of_pairing", "LinearMap.C_det_mul_charpolyRev_of_similitude"]
order = 4151
uses = ["det-def-cohfamily", "det-def-roots", "sk-thm-intfactors", "sk-cor-tf-functional-equation"]
+++
With $P_i\in\Z[T]$ of [sk-thm-intfactors], $b_i=\deg P_i$ and
$D_i=(-1)^{b_i}[T^{b_i}]P_i(T)$ one has, for every $0\le i\le2d$,

$$
P_{2d-i}(q^{-d}T^{-1})=(-1)^{b_i}T^{-b_i}D_i^{-1}P_i(T),
\qquad
D_iD_{2d-i}=q^{db_i}.
$$

Moreover $d\chi$ is even, $\chi=\sum_i(-1)^{i}b_i$.
