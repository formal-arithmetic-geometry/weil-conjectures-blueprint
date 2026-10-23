+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-stage-killing"
uses  = ["lemma-weil-pbc-etale-cohomology-continuity"]
+++
By the continuity of etale cohomology along cofiltered limits of
quasi-compact quasi-separated schemes with affine transition maps
[lemma-weil-pbc-etale-cohomology-continuity], the pullback maps induce an
isomorphism

$$
 \varinjlim_jH^q(D_j,\pi_j^{-1}G)\xrightarrow{\sim}H^q(X,G|_X).
$$

The element of the colimit represented by $\pi_{j_0}^*c$ maps to the pullback
of $c$ to $X$, which is zero; hence it is zero in the filtered colimit, so
there is $j\to j_0$ with $\pi_j^*c=0$ (the pullbacks of $c$ along the
$\pi_j$ are compatible with the transition maps).
