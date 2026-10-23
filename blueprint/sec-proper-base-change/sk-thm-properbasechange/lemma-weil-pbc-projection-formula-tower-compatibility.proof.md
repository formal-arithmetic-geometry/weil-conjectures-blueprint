+++
kind  = "proof"
of    = "lemma-weil-pbc-projection-formula-tower-compatibility"
+++
Under the adjunction $Lf^*\dashv Rf_*$, both composites
$(Rf_*K)\otimes^LP\to Rf_*(K\otimes^LLf^*P')$ correspond to

$$
Lf^*(Rf_*K\otimes^LP)\cong Lf^*Rf_*K\otimes^LLf^*P
\xrightarrow{\epsilon_K\otimes1}K\otimes^LLf^*P
\xrightarrow{1\otimes Lf^*h}K\otimes^LLf^*P',
$$

by naturality of the monoidal comparison of $Lf^*$ and of adjunction in its
arguments. Hence the two composites are equal. For $h=q_n$ this is the
square. If the horizontal arrows are isomorphisms, composing the equality
$Rf_*(1\otimes Lf^*q_n)\,\pi_{n+1}=\pi_n\,(1\otimes q_n)$ with
$\pi_n^{-1}$ on the left and $\pi_{n+1}^{-1}$ on the right gives the square
of inverses.
