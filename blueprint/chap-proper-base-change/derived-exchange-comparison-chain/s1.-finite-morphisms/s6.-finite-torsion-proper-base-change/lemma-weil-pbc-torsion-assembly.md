+++
id = "lemma-weil-pbc-torsion-assembly"
kind = "lemma"
title = "Torsion coefficient assembly"
order = 1625
uses = ["lemma-weil-pbc-direct-image-filtered-colimit", "lemma-weil-pbc-five-lemma-transfer", "lemma-weil-pbc-prime-factor-induction", "lemma-weil-pbc-prime-proper-base-change", "lemma-weil-pbc-torsion-filtered-union"]
+++
For every torsion abelian sheaf $F$ and every proper Cartesian square, the
specific map $\operatorname{Ex}_{\square,F}$ is an isomorphism.

## Proof

Write $F=\varinjlim_nF[n]$ and commute both sides of exchange with the
filtered colimit. Induct on the number of prime factors of $n$ through
$0\to F[\ell]\to F[n]\to F[n]/F[\ell]\to0$; the quotient is killed by
$n/\ell$. Prime coefficients are handled by the preceding lemma, and the
five-lemma transfer handles the induction step. Naturality shows at every
stage that the comparison is the S0 exchange map.
