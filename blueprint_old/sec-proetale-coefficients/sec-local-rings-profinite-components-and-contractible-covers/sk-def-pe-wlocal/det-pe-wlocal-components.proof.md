+++
kind = "proof"
of = "det-pe-wlocal-components"
+++
*1.* A closed subspace of a spectral space is spectral, so $T^c$ is spectral, and every
point of $T^c$ is closed, so $T^c$ is $T_1$; it is compact as a closed subset of the
quasi-compact space $T$. In a spectral space the constructible (patch) topology is compact
Hausdorff with a basis of clopen sets, it is finer than the given topology, and a subset
that is closed in the constructible topology and stable under specialization is closed
(Stacks, Topology, section on spectral spaces). In $T^c$ the specialization order is
trivial, so every patch-closed subset is closed: the topology of $T^c$ equals its patch
topology, which is profinite.

*2.* Every point $x$ specializes to some closed point, since $\overline{\{x\}}$ is a
nonempty quasi-compact closed subset; by Zorn's lemma and quasi-compactness it contains a
minimal nonempty closed subset, which is a single point since $T$ is sober and $T_0$. That
closed point lies in the connected component of $x$, as $\overline{\{x\}}$ is connected;
so $T^c\to\pi_0(T)$ is surjective. For injectivity let $c\neq c'$ in $T^c$. By 1 there is
a clopen $U_0\subset T^c$ with $c\in U_0$, $c'\notin U_0$. Let $U$ and $V$ be the sets of
generalizations of points of $U_0$ and of $T^c\setminus U_0$. In a w-local space the set of
generalizations of a closed subset of $T^c$ is closed ([Stacks, Tag 096A](https://stacks.math.columbia.edu/tag/096A)), so $U$ and $V$
are closed. They cover $T$ because every point has a closed specialization, and they are
disjoint because closed specializations are unique. So $U$ is clopen, contains $c$ and
not $c'$, and $c,c'$ lie in different components. The map $T^c\to\pi_0(T)$ is continuous,
bijective, from a compact space to the Hausdorff space $\pi_0(T)$ (connected components of
a compact space form a compact Hausdorff space), hence a homeomorphism.

*3.* For a generalization $x$ of $c$, the closure $\overline{\{x\}}$ is connected and
contains $c$, so $x$ lies in the component of $c$. Conversely, if $x$ lies in the component
of $c$, let $c'$ be a closed specialization of $x$; then $c'$ lies in the component of $x$,
which is that of $c$, so $c'=c$ by 2.

*4.* The primes contained in $\mathfrak m$ are the generalizations of $\mathfrak m$, i.e.
the image of $\operatorname{Spec}R_{\mathfrak m}$; by 3 this set is the component of
$\mathfrak m$.
