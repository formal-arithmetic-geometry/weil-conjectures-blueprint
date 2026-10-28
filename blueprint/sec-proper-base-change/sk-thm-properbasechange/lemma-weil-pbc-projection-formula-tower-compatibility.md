+++
id = "lemma-weil-pbc-projection-formula-tower-compatibility"
kind = "lemma"
title = "Projection formulas form a coefficient tower"
order = 2084
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.properProjectionMorphism", "AlgebraicGeometry.ProEtale.CondensedRing.properProjectionMorphism_natural_right"]
uses = ["def-weil-pbc-projection-formula-map"]
+++
Let $\Lambda$ be a commutative condensed ring, $f:X\to Y$ a morphism and
$K\in D(X_{\Proet},\Lambda)$. The projection-formula map $\pi_{f,K,P}$ of
[def-weil-pbc-projection-formula-map] is natural in $P$: for every morphism
$h:P\to P'$ in $D(Y_{\Proet},\Lambda)$,

$$
Rf_*(1_K\otimes Lf^*h)\circ\pi_{f,K,P}=\pi_{f,K,P'}\circ(1_{Rf_*K}\otimes h).
$$

In particular, for $\Lambda=\mathcal O_E$, $P_n=(\mathcal O_E/\pi_E^n)_Y$ and
the quotient maps $q_n:P_{n+1}\to P_n$, writing $\pi_n=\pi_{f,K,P_n}$, the
square

$$
\begin{CD}
(Rf_*K)\otimes^LP_{n+1} @>{\pi_{n+1}}>>
Rf_*(K\otimes^LLf^*P_{n+1})\\
@V{1\otimes q_n}VV @VV{Rf_*(1\otimes Lf^*q_n)}V\\
(Rf_*K)\otimes^LP_n @>{\pi_n}>> Rf_*(K\otimes^LLf^*P_n)
\end{CD}
$$

commutes; whenever $\pi_n$ and $\pi_{n+1}$ are isomorphisms, the square with
their inverses as horizontal arrows and the same vertical arrows commutes as
well.
