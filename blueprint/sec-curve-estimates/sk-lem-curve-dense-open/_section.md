+++
id = "sk-lem-curve-dense-open"
kind = "lemma"
title = "Removing finitely many points"
order = 1510
lean = ["AlgebraicGeometry.Etale.shortExact_openClosedShortComplex", "AlgebraicGeometry.IsCurve.assertions_iff_dense_open_prime"]
uses = ["sk-def-curve", "sk-lem-curve-finite-support"]
tags = ["sketch"]
+++
Let $j\colon U\hookrightarrow C$ be a dense open in a reduced curve and
$i\colon Z\hookrightarrow C$ its finite complementary closed subscheme. For a
classical constructible sheaf $F$ killed by a prime $r$ there is an exact
sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F\longrightarrow i_*i^*F\longrightarrow0.
$$

Consequently the assertions $(C_1)$–$(C_8)$ of [def-weil-pbc-eight-curve-assertions]
for $F$ and for $j_!j^*F$ are equivalent.
