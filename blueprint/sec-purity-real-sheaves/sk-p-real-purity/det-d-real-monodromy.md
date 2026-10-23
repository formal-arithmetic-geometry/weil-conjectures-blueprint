+++
id = "det-d-real-monodromy"
kind = "definition"
title = "Arithmetic monodromy and a central representative"
lean = ["AlgebraicGeometry.WeilGroup.toLinearAut"]
order = 3889
uses = ["lem-wf-weil-group-exact-sequence", "d-monodromy", "sk-p-central"]
+++
For the Weil representation
$\rho:W(C_0)\to\GL(V)$ over the coefficient field
$K=\Qlb$ (algebraically closed of characteristic zero), with $\gamma$ of
degree one, the degree sequence of [lem-wf-weil-group-exact-sequence] makes
$(W(C_0),\deg,\gamma,\rho)$ a represented degree datum with $P=\pi_1(C)$.
Its monodromy data $(P,H,G,F)$ are those of [d-monodromy]:

$$
H=\overline{\rho(\pi_1(C))},\qquad
G=\overline{\rho(W(C_0))},\qquad F=\rho(\gamma).
$$

Positive central Frobenius representatives $(N,z)$ are the positive
central pairs of [sk-p-central] for these data.
