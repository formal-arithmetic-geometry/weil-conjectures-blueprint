+++
id = "sk-lem-curve-dense-open"
kind = "lemma"
title = "Removing finitely many points"
order = 930
lean = ["AlgebraicGeometry.Etale.shortExact_openClosedShortComplex", "AlgebraicGeometry.IsCurve.assertions_iff_dense_open_prime"]
uses = ["sk-lem-curve-finite-support"]
tags = ["sketch"]
+++
Let $j:U\hookrightarrow C$ be a dense open in a reduced curve, and let
$i:Z\hookrightarrow C$ be its finite complementary closed subscheme.
For a classical constructible sheaf $F$, there is an exact sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F
\longrightarrow i_*i^*F\longrightarrow0.
$$

Suppose that $C$ is separated of finite type over an algebraically
closed field $k$. Fix a prime $\ell$ and suppose that $\ell F=0$.
For each of the assertions $(C_1)$–$(C_8)$ of
Theorem [sk-thm-curve-package], under its hypotheses on $C$ and the
coefficient prime, the assertion holds for $F$ if and only if it
holds for $j_!j^*F$.
More generally the same equivalence holds for a constructible torsion
$F$ whenever the hypotheses of the assertion hold for both sheaves.
