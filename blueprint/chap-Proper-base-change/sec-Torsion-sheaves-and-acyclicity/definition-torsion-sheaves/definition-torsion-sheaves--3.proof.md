+++
kind = "proof"
of = "definition-torsion-sheaves--3"
order = 340005
uses = ["definition-torsion-sheaves", "definition-torsion-sheaves--1", "definition-torsion-sheaves--2"]
+++
For $n\mid m$, multiplication by $m$ vanishes on $F[n]$, giving the
inclusion $F[n]\to F[m]$. The identity and composition laws follow by
cancelling the kernel inclusions. The index category is filtered:
$1$ is an index and $nm$ is an upper bound for $n$ and $m$.

If its canonical map to $F$ is an isomorphism, preservation of colimits
by geometric stalks shows that every germ comes from some $F[n]$.
Additivity and the kernel equation show that this germ is killed by
$n$, proving condition 3.

Locally torsion sections give torsion germs: represent a germ by a
section and lift the point to a member of a covering on which that
section has finite order. Conversely, for a section over $U$, consider
the sieve of arrows on which its restriction has finite order. A
torsion germ is killed by a positive integer, and this equality is
witnessed on a smaller pointed étale neighbourhood. Conservativity of
the geometric points makes this sieve covering. Algebraic closures of
the residue fields already give a conservative family, so condition 3
suffices; the same argument gives the version with separably closed
geometric points.

Assume condition 2. Write $\varphi:\varinjlim_nF[n]\to F$ for the
canonical map. Exactness of filtered colimits of abelian sheaves makes
$\varphi$ a monomorphism, since every $F[n]\to F$ is a monomorphism.
Every section of $F$ locally lifts to some $F[n]$, by the kernel
description in [definition-torsion-sheaves--2], and hence locally lifts
to the colimit. Thus $\varphi$ is an epimorphism as well, and is an
isomorphism. This proves condition 1.

For module sheaves, geometric stalks commute with forgetting the
$\Lambda$-action, giving the asserted equivalence with local torsion of
the underlying abelian sheaf. To construct the filtered diagram, take
$J=\mathbb N$ with its usual order and $D_k=F[k!]$. Divisibility of
factorials gives the transition inclusions. Exactness of filtered
colimits again makes $t:\varinjlim_kF[k!]\to F$ a monomorphism. If two
maps out of $F$ agree after composition with $t$, they agree on every
$F[k!]$. A germ killed by $m>0$ is killed by $m!$, so exactness of the
geometric stalk functor lifts it to the stalk of $F[m!]$. The two maps
therefore agree on all geometric stalks, and conservativity makes them
equal. Thus $t$ is also an epimorphism and hence an isomorphism. Finally,
the kernel equation, followed by cancellation of the inclusion, gives
$k!\,\id_{F[k!]}=0$.
