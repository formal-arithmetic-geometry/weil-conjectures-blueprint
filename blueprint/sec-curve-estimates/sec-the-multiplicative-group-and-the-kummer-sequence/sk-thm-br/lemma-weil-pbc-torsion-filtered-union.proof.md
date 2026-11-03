+++
kind  = "proof"
of    = "lemma-weil-pbc-torsion-filtered-union"
+++
For $k\in\mathbf N$ let $F[k!]=\ker(k!:F\to F)$, a subsheaf killed by
$k!$; since $k!\mid k'!$ for $k\le k'$ these form an increasing chain,
indexed by the filtered category $\mathbf N$. Filtered colimits of
sheaves of $\Lambda$-modules on $X_{\Et}$ [def-weil-pbc-etale-sheaves]
are exact, so the canonical map $\varinjlim_kF[k!]\to F$ is a
monomorphism. It is an epimorphism, as can be checked on geometric
stalks: geometric stalks commute with colimits and kernels, and an
element of a stalk killed by $n>0$ lies in the stalk of $F[k!]$ for
every $k\ge n$. Hence $F=\varinjlim_kF[k!]$.

In the second case let $N_k$ be the product of the positive integers
$d\le k$ invertible on $S$, and use the chain $F[N_k]$. Its colimit
maps monomorphically to $F$ as before. Every map $D_j\to F$ from the
first diagram factors through some $F[N_k]$: on geometric stalks the
image of $D_j$ is killed by $n_j$ and by orders invertible on $S$, hence
by the part of $n_j$ prime to the non-invertible primes, which divides
$N_{n_j}$. So the colimit map is also an epimorphism.
