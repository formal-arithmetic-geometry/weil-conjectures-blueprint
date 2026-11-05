+++
kind = "proof"
of = "lemma-triviality-fibres--2"
order = 1475005
uses = ["lemma-triviality-fibres--1", "theorem-chow-s-lemma-projective-form"]
+++
Put $\mathcal A=\mathcal M\otimes\mathcal N^{-1}$ and
$\mathcal B=\mathcal N\otimes\mathcal M^{-1}$. These are invertible
and $\mathcal A\otimes\mathcal B\simeq\mathcal O_X$.
Tensoring with $\mathcal N_t$ shows that
$\mathcal M_t\simeq\mathcal N_t$ if and only if $\mathcal A_t$ is
trivial. By [lemma-triviality-fibres--1], this is equivalent to

$$
h^0(X_t,\mathcal A_t)>0\quad\text{and}\quad h^0(X_t,\mathcal B_t)>0.
$$

An invertible sheaf is of finite presentation and, since $f$ is flat,
is flat over $T$. The upper semicontinuity theorem
`AlgebraicGeometry.Scheme.Modules.upperSemicontinuous_hFiber`
therefore applies to both sheaves. Its proof computes fibre cohomology
locally by a bounded complex of finite free modules; the finiteness
input ultimately uses Chow's lemma [theorem-chow-s-lemma-projective-form].
For either sheaf $\mathcal F$, the locus
$\{t\in T\mid h^0(X_t,\mathcal F_t)<1\}$ is open. The required set
is the intersection of the complements of these two open loci, hence
is closed.
