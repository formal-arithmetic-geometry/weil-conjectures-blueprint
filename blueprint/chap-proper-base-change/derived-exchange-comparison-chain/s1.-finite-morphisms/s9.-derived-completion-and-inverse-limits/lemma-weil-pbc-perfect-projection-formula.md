+++
id = "lemma-weil-pbc-perfect-projection-formula"
kind = "lemma"
title = "Perfect projection formula for reductions"
order = 1746
uses = ["def-weil-pbc-complete-coefficient-datum", "lemma-weil-pbc-projection-formula-base-change-naturality", "lemma-weil-pbc-projection-formula-identity-compactification", "lemma-weil-pbc-projection-formula-totalization", "lemma-weil-pbc-projection-formula-tower-compatibility"]
+++
For every $n$ there is a natural isomorphism

$$
(Rf_*K)\otimes^L_\Lambda\Lambda/I^n
\xrightarrow[\pi_n]{\sim}Rf_*K_n
$$

whose inverse is $\rho_n$. The families $(\pi_n)$ and $(\rho_n)$ commute
with the reduction tower, compatible coefficient endomorphisms, and base
change.

## Proof

Choose a strict-perfect package $F_n^\bullet\to P_n$. Signed totalization
gives inverse arrows

$$
(Rf_*K)\otimes^LF_n^\bullet
\mathrel{\substack{\xrightarrow{\ \pi_n\ }\\[-2pt]
\xleftarrow[\ \rho_n\ ]{}}}
Rf_*(K\otimes^LLf^*F_n^\bullet).
$$

Because $P_n$ is constant, $Lf^*P_n=P_n$, and the target is $Rf_*K_n$.
The identity-compactification lemma shows that this is also the open/proper
compactification composite for proper $f$. The totalization lemma gives
$\rho_n\pi_n=1$ and $\pi_n\rho_n=1$. Uniqueness of an inverse makes the map
independent of the strict-perfect package. Tower, operator, and base-change
compatibility are exactly the preceding two lemmas. This expands the
finite-projective argument located at Tag `0944`.
