+++
kind  = "proof"
of    = "lem-weil-pbc-prime-factor-devissage"
+++
The displayed sequence is the kernel--image sequence for multiplication by
$r$ in the abelian category $\mathcal C$ (for etale sheaves, kernels and images
are computed as in [def-weil-pbc-etale-sheaves]). The claims about the orders
follow from $r\cdot F[r]=0$ and $(n/r)\cdot rF=0$, the latter because
$(n/r)\cdot r=n$ kills $F$ and $F\to rF$ is an epimorphism. For the last
assertion, induct on $n$: if $n=1$ then $F=0$ is killed by any prime; if $n>1$,
choose a prime $r\mid n$; then $F[r]$ is killed by the prime $r$ and $rF$ is
killed by $n/r<n$, so $P$ holds for both by induction, hence for $F$ by
stability under extensions.
