+++
id = "lem-kun-invertible-orders-colimit"
kind = "lemma"
title = "The colimit description of invertible orders"
order = 2026
uses = ["def-kun-torsion-invertible", "def-weil-pbc-etale-sheaves", "lem-kun-stalks-commute-colimits", "lemma-weil-pbc-geometric-stalk-conservative", "lemma-weil-pbc-torsion-filtered-union"]
+++
Let $K$ be a field and $F$ a
torsion sheaf on the etale site
of a $K$-scheme; write $F[n]=\ker(n:F\to F)$ and let $I_K$ be the
set of integers invertible in $K$, as in
[def-kun-torsion-invertible]. Then $F$ has orders invertible in
$K$ if and only if

$$
F=\varinjlim_{n\in I_K}F[n].
$$
