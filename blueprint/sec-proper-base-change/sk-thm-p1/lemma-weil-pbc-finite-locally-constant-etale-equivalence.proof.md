+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-locally-constant-etale-equivalence"
+++
(1) $h_P$ is a sheaf since the etale topology is subcanonical. Etale locally on
$T$ a finite etale $P$ is a finite disjoint union of copies of the base, so
$h_P$ is locally the constant sheaf on a finite set.

(2) Given $E$, choose an etale cover $U\to T$ trivializing it with finite
fibre $S$. The descent isomorphism on $U\times_TU$ is a permutation of $S$
satisfying the cocycle equation, hence descends the disjoint union
$\coprod_{s\in S}U$ to a finite etale scheme $P$ (descent of affine morphisms
along etale covers), and $h_P\cong E$ because both become
$\coprod_{s\in S}U$ after the same cover.

(3) A torsor $Q$ under $\underline M$ is locally isomorphic to $\underline M$,
so it is a finite locally constant sheaf of sets and $Q\cong h_P$ for a finite
etale $P\to T$ by (2). By the Yoneda lemma the action
$\underline M\times Q\to Q$ is an action of $M$ on $P$ by $T$-automorphisms.
The map $\coprod_{m\in M}P\to P\times_TP$ induces on functors of points the
map $\underline M\times Q\to Q\times Q$, $(m,x)\mapsto(mx,x)$, which is an
isomorphism because the action is simply transitive; hence it is an
isomorphism. Finally $P\to T$ is surjective because $Q$ has sections etale
locally.
