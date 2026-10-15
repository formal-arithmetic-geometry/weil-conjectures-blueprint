+++
kind = "proof"
of = "sk-prop-pbc-p1-henselian"
uses = ["sk-lem-pbc-p1-injective-fibre", "sk-thm-pbc-henselian-h0"]
+++
Write $X=\mathbf P^1_A$ and $X_0=\mathbf P^1_k$ as in
[sk-lem-pbc-p1-injective-fibre]. Suppose first that $rF=0$ for a prime $r$.
Take an injective resolution $F\to I^\bullet$ in sheaves of
$\mathbf F_r$-modules on $X_{\Et}$. Since $i^{-1}$ is exact,
$F_0\to I_0^\bullet$ remains a resolution; [sk-lem-pbc-p1-injective-fibre]
makes it a resolution by $\Gamma(X_0,-)$-acyclic sheaves.
[sk-thm-pbc-henselian-h0] identifies the two complexes of sections term by
term:

$$
\Gamma(X,I^\bullet)\xrightarrow{\ \sim\ }\Gamma(X_0,I_0^\bullet).
$$

The left complex computes $R\Gamma(X,F)$, and the right computes
$R\Gamma(X_0,F_0)$. Thus their natural restriction map is a
quasi-isomorphism.

The class of sheaves for which this holds is closed under extensions, by the
natural long exact cohomology sequences. A sheaf killed by $r^a$ has a finite
filtration with quotients killed by $r$; a sheaf killed by an integer $n$ is
the finite direct sum of its primary parts. This gives the result for sheaves
of bounded torsion. Finally, $F=\varinjlim_nF[n]$, with positive integers
ordered by divisibility. Both $X$ and $X_0$ are quasi-compact and
quasi-separated, so Stacks Project, Tag 03Q5 passes the comparison to this
filtered colimit. All maps used are restriction maps, which also proves
naturality in $F$.
