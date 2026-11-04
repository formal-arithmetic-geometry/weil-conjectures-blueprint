+++
kind = "proof"
of = "lemma-lattices-after-finite-stratification"
order = 291
+++
Let $Y\to X$ be the étale $X$-scheme representing lattices in $L$
(Lemma [lemma-lattices-lisse-e-sheaves]), with its universal lattice.

*Pushing down by the trace.* Choose finitely many quasi-compact
affine opens of this scheme whose images cover $X$, and let
$p:V\to X$ be their disjoint union. Then $p$ is quasi-compact, separated,
surjective and étale, and the universal lattice gives a lattice
$M_0\subset p^*L$. By [Stacks, [07RY](https://stacks.math.columbia.edu/tag/07RY), [07RZ](https://stacks.math.columbia.edu/tag/07RZ)], $X$ has a finite
stratification by locally closed subschemes over each of which $p$ is
finite étale and surjective. On such a stratum $S$, let
$\operatorname{Tr}:p_*p^*L\to L$ be the trace of the finite étale map $p$
over $S$, and define $L_0\subset L|_S$
as the image of the composite

$$
p_*M_0\longrightarrow p_*p^*L\xrightarrow{\operatorname{Tr}}L.
$$

To see that $L_0$ is a lattice, we split the finite étale cover
locally on $S$ into $d$ copies of $S$. Then $p_*M_0$ is a direct sum of
$d$ lattices $M_1,\dots,M_d$ in $L$, and the trace is their sum. Thus
$L_0=M_1+\cdots+M_d$. If we further trivialize $L$ pro-étale locally,
each $M_k$ becomes a locally constant function to the discrete set of lattices
in $E^r$. After a common refinement each $M_k$ is the constant sheaf
attached to a lattice $N_k\subset E^r$. Then $L_0$ is the constant sheaf
attached to $N_1+\cdots+N_d$, which is a finite free $\mathcal O_E$-lattice
spanning $E^r$. Hence $L_0$ is lisse and $L_0[1/\ell]=L|_S$.
