+++
id = "lem-weil-pbc-target-locality"
kind = "lemma"
title = "Target locality"
order = 1699
uses = ["def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-property-detailed", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-geometric-stalk-conservative", "lem-weil-pbc-qcqs-higher-direct-image"]
+++
For proper $f:X\to Y$, the assertion $\mathrm{PBC}(f)$ of
[def-weil-pbc-property-detailed] is local on $Y$ for the etale topology. More
precisely, after an etale covering $\coprod_iV_i\to Y$, the exchange map is an
isomorphism if and only if its pullback over every $V_i$ is an isomorphism.

## Proof

By the quasi-compact quasi-separated description of higher direct image, the
restriction of $R^qf_*F$ to $V$ is the sheafification of $U\mapsto
H^q(X\times_YU,F|)$, compatible with further etale restriction and with the
canonical exchange morphism of [def-weil-pbc-derived-exchange-detailed]. Hence the
exchange map is an isomorphism if and only if it is so on the stalks over an
etale cover, and geometric stalks are conservative.
