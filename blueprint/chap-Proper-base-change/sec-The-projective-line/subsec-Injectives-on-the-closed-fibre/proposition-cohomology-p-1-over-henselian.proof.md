+++
kind = "proof"
of = "proposition-cohomology-p-1-over-henselian"
order = 376
uses = ["theorem-comparison-over-henselian-pair-degree", "lemma-acyclicity-closed-fibre", "definition-compactification-refinement"]
+++
We treat sheaves killed by a prime first, where
Lemma [lemma-acyclicity-closed-fibre] applies, and then reach all torsion
sheaves by extensions, direct sums and filtered colimits.

Suppose first that $\ell F=0$ for a prime $\ell$.  Take an injective resolution
$F\to I^\bullet$ in sheaves of $\mathbf F_\ell$-modules on $\mathbf P^1_{R,\acute{e}t}$.
Since $i^*$ is exact, $F_0\to I_0^\bullet$ is again a resolution, and by
Lemma [lemma-acyclicity-closed-fibre] its terms are
$\Gamma(\mathbf P^1_\kappa,-)$-acyclic. Moreover, Theorem [theorem-comparison-over-henselian-pair-degree]
shows that the two complexes of sections agree term by term:

$$
\Gamma(\mathbf P^1_R,I^\bullet)\xrightarrow{\sim}
\Gamma(\mathbf P^1_\kappa,I_0^\bullet).
$$

The left complex computes $R\Gamma(\mathbf P^1_R,F)$, and the right computes
$R\Gamma(\mathbf P^1_\kappa,F_0)$. Hence the natural restriction map between them is a
quasi-isomorphism.

By the long exact cohomology sequences and the five lemma, the sheaves
for which the statement holds form a class closed under extensions. Since a
sheaf killed by $\ell^a$ has a finite filtration with quotients killed by
$\ell$, and a sheaf killed by an integer $n$ is the finite direct sum of
its primary parts, the class contains all sheaves of bounded torsion.
An arbitrary torsion $F$ is the colimit
$\varinjlim_n F[n]$, with positive integers ordered by divisibility, and the
comparison passes to this colimit, because the cohomology of the
quasi-compact quasi-separated schemes $\mathbf P^1_R$ and
$\mathbf P^1_\kappa$ commutes with filtered colimits [Stacks, [03Q5](https://stacks.math.columbia.edu/tag/03Q5)]. Finally, all
maps used are restriction maps, which gives naturality in $F$.
