+++
id = "cor-weil-pbc-torsor-comparison"
kind = "theorem"
title = "Torsor comparison"
order = 1656
uses = ["def-weil-pbc-finite-torsors", "thm-galois-lc-etale", "thm-weil-pbc-finite-etale-lifting"]
tags = ["latex:corollary"]
+++
Under the hypotheses of [thm-weil-pbc-finite-etale-lifting], restriction is a
bijection

$$
 H^1(Y,\underline M)\xrightarrow{\sim}H^1(Y_0,\underline M)
$$

for every finite abelian group $M$.

## Proof

By [def-weil-pbc-finite-torsors] the two sides classify $M$-torsors, which by
[thm-galois-lc-etale] are the simply transitive $M$-actions on finite etale schemes. The equivalence of
[thm-weil-pbc-finite-etale-lifting] preserves such actions and their
isomorphism classes, giving the bijection.
