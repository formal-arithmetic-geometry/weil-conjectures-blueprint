+++
kind  = "proof"
of    = "sk-lem-stratified-lattice"
+++
The idea is to find a lattice after an étale surjective base change and then push it down by
the trace. The first step uses that the lattices in $E^r$ form a discrete set on which
$\GL_r(E)$ acts continuously, so that the sheaf of lattices in $L$ is an étale $X$-scheme.
The second step needs the base change to be finite étale, which holds on the strata of a
finite stratification.

The rank of $L$ is a locally constant function on $|X|$: on a trivializing covering the
subsets of constant rank are open and closed and saturated, and they descend by fpqc descent
of open subsets, so we may assume that $L$ has constant rank $r$. Details:
[det-lem-stratified-lattice-rank].

*The sheaf of lattices is an étale $X$-scheme.* Consider the sheaf on $X_{\mathrm{proét}}$
whose sections over $U$ are the lisse $\cO_{E,U}$-submodules $M\subset L|_U$ with
$M[1/\ell]=L|_U$. We show that it is represented by a separated surjective étale $X$-scheme.
On an affine pro-étale object $V$ where $L$ is free of rank $r$, this sheaf is the constant
sheaf on the set $\GL_r(E)/\GL_r(\cO_E)$ of lattices in $E^r$. This set is discrete because
$\GL_r(\cO_E)$ is an open subgroup of $\GL_r(E)$. A change of basis on $V\times_XV$ is a
continuous function to $\GL_r(E)$, and since the stabilizer of a lattice is open, its action
on each fixed lattice is locally constant. Hence the induced map from the disjoint union of
copies of $V\times_XV$ indexed by the lattices in $E^r$ to itself is a morphism of schemes:
on each component, the preimages of the target components are open and closed and form a
disjoint open cover. The cocycle of the transition matrices therefore gives a descent datum
of schemes for these disjoint unions of copies of $V$.

For affine $V=\Spec B$, the disjoint union of copies of $V$ indexed by a set $I$ is
quasi-affine: it is the union, inside $\Spec\prod_IB$, of the principal open subsets defined
by the coordinate idempotents. Descent of quasi-affine schemes along fpqc coverings is
effective by \stacks{0APK}. Taking a finite affine trivializing covering of each affine open
of $X$ and gluing, we obtain a scheme representing the sheaf of lattices. It is separated and
étale over $X$ by \stacks{02KU} and \stacks{02VN}, and it is surjective because every free
module has a lattice. The universal lattice exists on it by descent of module sheaves.
Details: [det-lem-stratified-lattice-scheme].

*Pushing down by the trace.* Choose finitely many quasi-compact affine opens of this scheme
whose images cover $X$, and let $p\colon V\to X$ be their disjoint union. Then $p$ is
quasi-compact, separated, surjective and étale, and the universal lattice gives a lattice
$M_0\subset p^*L$. By \stacks{07RY} and \stacks{07RZ}, $X$ has a finite stratification by
locally closed subschemes over each of which $p$ is finite étale and surjective. On such a
stratum $S$ let $\Tr\colon p_*p^*L\to L$, a morphism in $\Mod(S_{\mathrm{proét}},E)$, be the
trace of the finite étale map $p$ over $S$, and define $L_0\subset L|_S$ as the image of the
composite
$$
p_*M_0\longrightarrow p_*p^*L\xrightarrow{\ \Tr\ }L .
$$
To see that $L_0$ is a lisse lattice, split the finite étale cover locally on $S$ into $d$
copies of $S$. Then $p_*M_0$ is a direct sum of $d$ lattices $M_1,\dots,M_d$ in $L$, the trace
is their sum, and $L_0=M_1+\cdots+M_d$. Trivialize $L$ further pro-étale locally. Each $M_k$ is
then a locally constant function to the discrete set of lattices in $E^r$, so after a common
refinement all $M_k$ are constant lattices $\Lambda_k\subset E^r$. Then $L_0$ is the constant
sheaf attached to $\Lambda_1+\cdots+\Lambda_d$, which is a finite free $\cO_E$-lattice
spanning $E^r$. Hence $L_0$ is lisse and $L_0[1/\ell]=L|_S$. Details:
[det-lem-stratified-lattice-trace].
