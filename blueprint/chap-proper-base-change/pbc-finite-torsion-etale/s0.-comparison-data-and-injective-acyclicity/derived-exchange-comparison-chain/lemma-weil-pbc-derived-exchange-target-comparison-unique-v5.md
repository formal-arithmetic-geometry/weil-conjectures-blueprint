+++
id = "lemma-weil-pbc-derived-exchange-target-comparison-unique-v5"
kind = "lemma"
title = "Target comparisons are unique up to homotopy"
order = 1517
uses = ["def-weil-pbc-derived-exchange-hom-test-v5", "def-weil-pbc-derived-exchange-target-comparison-v5"]
+++
Two comparisons $c,d:J\to J'$ are homotopic. Comparisons in both directions
are inverse to one another in the homotopy category.

## Proof

The difference $(c-d)q$ is null-homotopic. Since
$\underline{\operatorname{Hom}}(C(q),J')$ is acyclic, the cone exact segment

$$
H^0\underline{\operatorname{Hom}}(C(q),J')=0\longrightarrow
H^0\underline{\operatorname{Hom}}(J,J')\xrightarrow{q^*}
H^0\underline{\operatorname{Hom}}(A,J')
$$

makes $q^*$ injective; hence $c-d$ is null-homotopic. If
$c:J\to J'$ and $c':J'\to J$ are comparisons, both $c'c$ and $1_J$ compare
$q$ with itself, and both $cc'$ and $1_{J'}$ compare $q'$ with itself.
The first assertion therefore gives $c'c\simeq1_J$ and $cc'\simeq1_{J'}$.
