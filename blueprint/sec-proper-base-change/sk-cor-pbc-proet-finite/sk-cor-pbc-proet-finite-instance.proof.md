+++
kind = "proof"
of = "det-pbc-proet-finite-instance"
+++
*(1)* Multiplication by $N$ is zero on $A$, hence on every $A$-module, hence
on every sheaf of $A$-modules on either site, and so on every cohomology sheaf
$\mathcal H^q(K)$, $\mathcal H^q(L)$. A sheaf killed by $N$ has every
geometric stalk killed by $N$, so it is torsion in the sense of the
underlying abelian sheaves.

*(2)* By (1) the hypotheses of the torsion theorem (classical, torsion
underlying cohomology) hold for $K$, so the exchange is an isomorphism.
Concretely, with the witness $(L,\alpha)$, the étale exchange for $L$ is an
isomorphism by étale proper base change with finite coefficients, and the
transport along $\nu^*$ (the direct-image and inverse-image comparisons, which
respect units and counits) identifies it with the pro-étale exchange for
$\nu_X^*L$; conjugating by $\alpha$ gives the exchange for $K$. This is
exactly the construction of [thm-weil-pbc-finite-level-proetale], and the
result does not depend on the witness: for two witnesses $(L,\alpha)$,
$(L',\alpha')$ the isomorphism $\alpha'^{-1}\alpha:\nu_X^*L\simeq\nu_X^*L'$
comes from a unique isomorphism $L\simeq L'$, because $\nu_X^*$ is fully
faithful on $D^+$ for finite coefficients [thm-weil-pbc-site-comparison], and
exchange is natural with respect to it.
