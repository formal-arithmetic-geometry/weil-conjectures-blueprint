+++
id = "lemma-weil-pbc-perfect-projection-formula"
kind = "lemma"
title = "Perfect projection formula for reductions"
order = 1342
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-complete-coefficient-datum", "def-weil-pbc-proetale-operations", "def-weil-pbc-projection-formula-map", "lemma-weil-pbc-projection-formula-base-change-naturality", "lemma-weil-pbc-projection-formula-identity-compactification", "lemma-weil-pbc-projection-formula-totalization", "lemma-weil-pbc-projection-formula-tower-compatibility"]
+++
For fixed $f$ and $K$, the full subcategory of objects $P$ for which
$\pi_{f,K,P}$ of [def-weil-pbc-projection-formula-map] is an isomorphism is a
thick triangulated subcategory containing every finite free $A$-module. In
particular, it contains every perfect complex, and for every $n$ there is a
natural isomorphism

$$
(Rf_*K)\otimes^L_\Lambda\Lambda/I^n
\xrightarrow[\pi_n]{\sim}Rf_*K_n
$$

whose inverse is $\rho_n$. The families $(\pi_n)$ and $(\rho_n)$ commute
with the reduction tower, compatible coefficient endomorphisms, and base
change.
