+++
id = "sk-lem-curve-dense-open"
kind = "lemma"
title = "Removing finitely many points"
order = 1598
lean = ["AlgebraicGeometry.Etale.shortExact_openClosedShortComplex", "AlgebraicGeometry.IsCurve.assertions_iff_dense_open_prime"]
uses = ["sk-lem-curve-finite-support"]
tags = ["sketch"]
+++
Let $j\colon U\hookrightarrow C$ be a dense open in a reduced curve, and let
$i\colon Z\hookrightarrow C$ be its finite complementary closed subscheme. For a
classical constructible sheaf $F$, there is an exact sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F\longrightarrow i_*i^*F\longrightarrow0.
$$

The assertions $(C_1)$–$(C_8)$ of [def-weil-pbc-eight-curve-assertions] hold for $F$
if and only if they hold for $j_!j^*F$.
