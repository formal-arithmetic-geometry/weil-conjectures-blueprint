+++
id = "lemma-weil-pbc-perfect-projection-formula"
kind = "lemma"
title = "Perfect projection formula for reductions"
order = 3520
uses = ["det-pe-derived-nakayama-resolution", "det-def-sfb-pulled-back-coefficients", "def-weil-pbc-proetale-operations", "def-weil-pbc-projection-formula-map", "lemma-weil-pbc-projection-formula-compactified", "lemma-weil-pbc-projection-formula-proper-piece", "lemma-weil-pbc-projection-formula-tower-compatibility"]
+++
Let $\Lambda$ be a commutative condensed ring and $f:X\to Y$ a morphism. For
fixed $K\in D(X_{\Proet},\Lambda)$, the full subcategory of objects
$P\in D(Y_{\Proet},\Lambda)$ for which $\pi_{f,K,P}$ of
[def-weil-pbc-projection-formula-map] is an isomorphism is a thick
triangulated subcategory containing every finite free $\Lambda_Y$-module. In
particular, it contains every perfect complex of $\Lambda_Y$-modules.

For $\Lambda=\mathcal O_E$ and $n\geq1$, the quotient
$P_n=(\mathcal O_E/\pi_E^n)_Y$ has the two-term resolution
$[\mathcal O_{E,Y}\xrightarrow{\pi_E^n}\mathcal O_{E,Y}]$
([det-pe-derived-nakayama-resolution]) and $Lf^*P_n=(\mathcal O_E/\pi_E^n)_X$.
Writing $K_n=K\otimes^L_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$, there is a
natural isomorphism

$$
(Rf_*K)\otimes^L_{\mathcal O_{E,Y}}P_n
\xrightarrow[\pi_n]{\sim}Rf_*K_n
$$

whose inverse is $\rho_n$. The families $(\pi_n)$ and $(\rho_n)$ commute
with the reduction tower, compatible coefficient endomorphisms, and base
change.
