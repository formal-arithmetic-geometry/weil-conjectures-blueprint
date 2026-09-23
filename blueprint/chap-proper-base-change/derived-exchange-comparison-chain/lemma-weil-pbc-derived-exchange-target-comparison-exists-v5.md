+++
id = "lemma-weil-pbc-derived-exchange-target-comparison-exists-v5"
kind = "lemma"
title = "Target-replacement comparisons exist"
order = 1422
uses = ["def-weil-pbc-derived-exchange-hom-test-v5", "def-weil-pbc-derived-exchange-target-comparison-v5"]
+++
Every target-replacement comparison problem has a comparison.

## Proof

The cone $C(q)$ is acyclic because $q$ is a quasi-isomorphism. K-injectivity
of $J'$ makes $\underline{\operatorname{Hom}}(C(q),J')$ acyclic. The
cone triangle gives the exact segment

$$
H^0\underline{\operatorname{Hom}}(J,J')\longrightarrow
H^0\underline{\operatorname{Hom}}(A,J')\longrightarrow
H^1\underline{\operatorname{Hom}}(C(q),J')=0.
$$

Thus $[q']$ lifts to $[c]$; equality $[cq]=[q']$ is exactly a homotopy
$cq\simeq q'$.
