+++
kind  = "proof"
of    = "lem-trf-open-ctf"
+++
Exactness in [def-weil-extension-by-zero] gives
$\mathcal H^r(j_!K)=j_!\mathcal H^r(K)$, so the range does not grow.
Take a common finite locally closed stratification of $U$
witnessing constructibility of the finitely many nonzero
$\mathcal H^r(K)$ in [def-weil-finite-torsion-constructibility].
Each stratum is locally closed in $Y$, and adding the closed
complement $Y\setminus U$ gives a finite stratification of $Y$.
The restrictions of the extended cohomology sheaves are the same
finite locally constant sheaves on these strata and the zero sheaf
on the complement. This proves constructibility.

If the Tor amplitude in [def-weil-finite-tor-amplitude] is
$[a,b]$, apply [lem-trf-open-tensor] with an arbitrary sheaf
$M$ of $A$-modules on $Y$, in degree zero. Its restriction
$j^*M$ is in degree zero, so $K\otimes_A^Lj^*M$ has no
cohomology outside $[a,b]$. Exact extension by zero preserves
that vanishing, giving the same Tor bound for $j_!K$.
