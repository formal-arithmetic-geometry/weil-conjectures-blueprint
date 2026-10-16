+++
id = "lem-sc-generic-cohomology-comparison"
kind = "lemma"
title = "Generic replacement in degrees at least two"
lean = ["AlgebraicGeometry.IsCurve.isIso_functorH_map_unit_fromSpecFunctionField"]
order = 1013
uses = ["def-sc-curves", "def-sc-function-field", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "lem-sc-zero-generic-acyclic", "prop-weil-pbc-strict-henselization-stalk-formula"]
+++
Let $C/k$ be a smooth integral separated
curve over algebraically closed $k$,
and let $\eta:\operatorname{Spec}k(C)\to C$ be its generic point,
with function field $k(C)$.
For every torsion etale sheaf
$F$, the adjunction map induces

$$
H^q(C,F)\ \xrightarrow{\ \sim\ }\ H^q(C,\eta_*\eta^*F)
\qquad(q\geq2)
$$

on cohomology.
