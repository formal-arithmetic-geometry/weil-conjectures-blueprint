+++
id = "sk-d-real-monodromy"
kind = "definition"
title = "Arithmetic monodromy and a central representative"
order = 2967
uses = ["sk-d-real-setup", "sk-d-real-weil", "sk-d-monodromy", "sk-d-central"]
lean = ["AlgebraicGeometry.WeilGroup.toLinearAut"]
tags = ["sketch"]
+++
For the Weil representation
$\rho:W(C_0)\to\GL(V)$ over the coefficient field
$K=\Qlb$ (algebraically closed of characteristic zero), with $\gamma$ of
degree one, the degree sequence of [sk-d-real-weil] makes
$(W(C_0),\deg,\gamma,\rho)$ a represented degree datum with $P=\pi_1(C)$.
Its monodromy data $(P,H,G,F)$ are those of [sk-d-monodromy]:

$$
H=\overline{\rho(\pi_1(C))},\qquad
G=\overline{\rho(W(C_0))},\qquad F=\rho(\gamma).
$$

Positive central Frobenius representatives $(N,z)$ are the positive
central pairs of [sk-d-central] for these data.
