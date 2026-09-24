+++
id = "lemma-weil-pbc-derived-exchange-source-comparison-v5"
kind = "lemma"
title = "Source-resolution comparisons exist and invert"
order = 1630
uses = ["def-weil-pbc-derived-exchange-hom-test-v5", "def-weil-pbc-derived-exchange-source-comparison-v5", "lemma-weil-pbc-derived-exchange-bounded-injective-kinjective-v5", "lemma-weil-pbc-derived-exchange-target-comparison-exists-v5", "lemma-weil-pbc-derived-exchange-target-comparison-unique-v5"]
+++
There are comparisons $a:I\to I'$ and $b:I'\to I$, unique up to homotopy,
with $ba\simeq1_I$ and $ab\simeq1_{I'}$.

## Proof

The resolutions are bounded below, so the preceding lemma makes $I'$ and $I$
K-injective. Apply
Lemma [lemma-weil-pbc-derived-exchange-target-comparison-exists-v5]
with $A=K$, $q=u$, $q'=u'$, $J=I$, and $J'=I'$ to obtain $a$.
Interchanging the two resolutions gives $b$. Now apply
Lemma [lemma-weil-pbc-derived-exchange-target-comparison-unique-v5]:
$ba$ and $1_I$ are two comparisons of $u$ with itself, while $ab$ and
$1_{I'}$ compare $u'$ with itself. It gives uniqueness up to homotopy and
the two displayed inverse equations.
