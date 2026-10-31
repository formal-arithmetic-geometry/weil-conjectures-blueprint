+++
kind = "proof"
of = "sk-prop-pbc-p1-henselian"
uses = ["sk-lem-pbc-p1-injective-fibre", "sk-thm-pbc-henselian-h0"]
+++
Suppose first that $\ell F=0$ for a prime $\ell$. Take an injective resolution
$F\to I^\bullet$ in sheaves of $\mathbf F_\ell$-modules on $\mathbf P^1_{R,\acute{e}t}$.
Since $i^*$ is exact, $F_0\to I_0^\bullet$ is again a resolution, and by
Lemma [sk-lem-pbc-p1-injective-fibre] it is a resolution by
$\Gamma(\mathbf P^1_\kappa,-)$-acyclic sheaves. By Theorem [sk-thm-pbc-henselian-h0],
the two complexes of sections agree term by term:

$$
\Gamma(\mathbf P^1_R,I^\bullet)\xrightarrow{\sim}
\Gamma(\mathbf P^1_\kappa,I_0^\bullet).
$$

The left complex computes $R\Gamma(\mathbf P^1_R,F)$, and the right computes
$R\Gamma(\mathbf P^1_\kappa,F_0)$, so the natural restriction map between them is a
quasi-isomorphism.

In general, the class of sheaves for which the statement holds is closed
under extensions, by the long exact cohomology sequences. A sheaf killed by
$\ell^a$ has a finite filtration with quotients killed by $\ell$, and a sheaf
killed by an integer $n$ is the finite direct sum of its primary parts.
This proves the result for sheaves of bounded torsion. Finally,
$F=\varinjlim_n F[n]$, with positive integers ordered by divisibility.
Since $\mathbf P^1_R$ and $\mathbf P^1_\kappa$ are quasi-compact and quasi-separated,
their cohomology commutes with filtered colimits [Stacks, Tag 03Q5](https://stacks.math.columbia.edu/tag/03Q5), and hence
the comparison passes to the colimit. Since all maps
used are restriction maps, this also proves naturality in $F$.
