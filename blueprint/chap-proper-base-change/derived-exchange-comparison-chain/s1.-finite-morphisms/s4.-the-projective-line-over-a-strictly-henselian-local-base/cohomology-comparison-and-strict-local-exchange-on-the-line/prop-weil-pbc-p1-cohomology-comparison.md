+++
id = "prop-weil-pbc-p1-cohomology-comparison"
kind = "theorem"
title = "Cohomology comparison on the projective line"
order = 1555
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-strict-henselian-p1-setup", "lem-weil-pbc-etale-degree-zero", "prop-weil-pbc-p1-acyclicity"]
+++
In the setup of [def-weil-pbc-strict-henselian-p1-setup], for every torsion
etale sheaf $F$ on $X$, restriction gives natural isomorphisms

$$
 H^q(X,F)\xrightarrow{\sim}H^q(X_0,F_0)
 \qquad(q\geq0).
$$

## Proof

Choose a K-injective resolution $F\to I^\bullet$. By the acyclicity statement
of [prop-weil-pbc-p1-acyclicity] each $I^m|_{X_0}$ is acyclic on $X_0$, so
$H^q(X_0,F_0)$ is computed by $\Gamma(X_0,I^\bullet|_{X_0})$; the degree-zero
comparison, applied termwise to the abelian sheaves $I^m$, identifies this
with $\Gamma(X,I^\bullet)$, whose cohomology is $H^q(X,F)$. Naturality in $F$
is the naturality of the two comparisons in the setup of
[def-weil-pbc-strict-henselian-p1-setup].
