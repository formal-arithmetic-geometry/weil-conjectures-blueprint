+++
kind = "proof"
of = "det-pe-wlocal-components"
+++
*1.* A closed subspace of a spectral space is spectral, so $T^c$ is spectral, and every
point of $T^c$ is closed. In a spectral space the constructible (patch) topology is compact
Hausdorff with a basis of clopen sets, it is finer than the given topology, and a subset
that is closed in the constructible topology and stable under specialization is closed
(Stacks, Topology, section on spectral spaces). In $T^c$ the specialization order is
trivial, so every patch-closed subset is closed: the topology of $T^c$ equals its patch
topology, which is profinite.

*2.* Every point $x$ specializes to some closed point, since $\overline{\{x\}}$ is a
nonempty quasi-compact closed subset; by Zorn's lemma and quasi-compactness it contains a
minimal nonempty closed subset, which is a single point since $T$ is sober and $T_0$; that
point is closed in $T$. By
hypothesis it is unique, so $r$ is well defined, and $r|_{T^c}=\mathrm{id}$. Continuity of
$r$ under the stated hypotheses (spectral, $T^c$ closed, unique closed specializations) is
Stacks, Tag 096A (see also Tags 0968, 0969).

Let $c\in T^c$ and $G_c=r^{-1}(c)$, the set of generalizations of $c$. For $x\in G_c$ the
closure of $\{x\}$ in the subspace $G_c$ is irreducible and contains $c$; so $G_c$ is a
union of connected subsets all containing $c$, hence connected. If $C$ is a connected
component of $T$, then $r(C)$ is a connected subset of the profinite, hence totally
disconnected, space $T^c$, so $r(C)=\{c\}$ for one $c$ and $C\subset G_c$; as $G_c$ is
connected and meets $C$, $C=G_c$. So the components are exactly the fibres of $r$, and each
contains exactly one closed point. The map $\pi_0(T)\to T^c$ induced by $r$ is continuous
(quotient topology) and inverse to $T^c\to T\to\pi_0(T)$, which is continuous; hence
$T^c\to\pi_0(T)$ is a homeomorphism.

*3.* Let $x\in T$ and let $C$ be its component, with unique closed point $c$. A closed
specialization $c'$ of $x$ lies in $\overline{\{x\}}$, which is connected and contains
$x$, so $c'\in C$ and $c'=c$. Existence of a closed specialization was shown in 2.

*4.* The primes contained in $\mathfrak m$ are the generalizations of $\mathfrak m$, i.e.
the image of $\operatorname{Spec}R_{\mathfrak m}$; by 2 this set is the component of
$\mathfrak m$.
