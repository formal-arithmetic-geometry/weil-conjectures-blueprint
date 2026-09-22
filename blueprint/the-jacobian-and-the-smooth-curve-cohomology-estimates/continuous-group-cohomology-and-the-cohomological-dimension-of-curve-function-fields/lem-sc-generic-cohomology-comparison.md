+++
id = "lem-sc-generic-cohomology-comparison"
kind = "lemma"
title = "Generic replacement in degrees at least two"
order = 4525
lean = ["AlgebraicGeometry.Curve.cohomology_iso_genericPushforward"]
uses = ["prop-weil-pbc-strict-henselization-stalk-formula", "lem-sc-zero-generic-acyclic"]
+++
Let $C/k$ be a smooth integral separated curve over algebraically closed
$k$, and let $\eta:\operatorname{Spec}k(C)\to C$ be its generic point, with
function field $k(C)$. For every torsion étale sheaf $F$, the adjunction map
induces
$$
H^q(C,F)\ \xrightarrow{\ \sim\ }\ H^q(C,\eta_*\eta^*F)\qquad(q\geq2)
$$
on cohomology.

## Proof

The generic restriction of $\eta_*M$ is $M$: after a geometric generic base
change the source is the same separably closed point, as is also seen from
the strict-henselization stalk formula [prop-weil-pbc-strict-henselization-stalk-formula] in degree zero. Hence the kernel and
cokernel of $F\to\eta_*\eta^*F$ both have zero generic restriction. They are
acyclic by [lem-sc-zero-generic-acyclic]. Write the map as a surjection onto
its image followed by an injection. The two long exact sequences give the
displayed isomorphism for $q\geq2$.

Unresolved dependencies: def:sc-curves, def:sc-function-field, def:weil-pbc-etale-sheaves, def:weil-pbc-etale-cohomology
