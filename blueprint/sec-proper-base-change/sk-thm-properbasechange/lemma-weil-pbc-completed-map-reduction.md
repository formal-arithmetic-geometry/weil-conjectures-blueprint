+++
id = "lemma-weil-pbc-completed-map-reduction"
kind = "lemma"
title = "Finite reduction of the completed map"
order = 1347
uses = ["def-weil-pbc-completed-base-change-map", "def-weil-pbc-completed-frobenius-structures", "def-weil-pbc-completed-reduction-square", "lem-weil-pbc-finite-reduction-reconstruction", "lem-weil-pbc-rectangle-derived-limit", "lemma-weil-pbc-completed-frobenius-equivariance", "lemma-weil-pbc-completed-pullback-reduction", "lemma-weil-pbc-frobenius-tower-compatibility", "lemma-weil-pbc-level-map-derived-limit"]
+++
For every $n$, the diagram

$$
\begin{CD}
S\otimes^LP_n @>{\overline\xi_n}>> T\otimes^LP_n\\
@V{\alpha_n}V{\sim}V @VV{\delta_n}V{\sim}\\
B_n @>{v'_n}>> D_n
\end{CD}
$$

commutes. Hence reduction of
$\operatorname{Ex}^{\mathrm{comp}}_{\square,K}$ of
[def-weil-pbc-completed-base-change-map] modulo $I^n$, conjugated
by the displayed canonical reduction isomorphisms, is exactly the S8
transported finite-level exchange map $v'_n=\operatorname{Ex}_{\square,K_n}$.
The squares for $n+1\to n$ commute, and the assertion is natural for
compatible tower endomorphisms. Under a Frobenius-equivariant datum, use
$\Phi_{Y'}P_n=P_n$ to give the two reductions their induced Weil structures.
Then

$$
\begin{aligned}
\alpha_n(\Theta_S\otimes1)
&=\Theta_{B,n}\Phi_{Y'}(\alpha_n),\\
\delta_n(\Theta_T\otimes1)
&=\Theta_{D,n}\Phi_{Y'}(\delta_n),
\end{aligned}
$$

and the displayed reduction square is a square of Weil objects.
