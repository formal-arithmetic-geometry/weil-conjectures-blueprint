+++
kind = "proof"
of = "sk-lem-lattice-atlas"
uses = ["sk-prop-sfb-qlbar-colimit-x"]
+++
The rank of $L$ is a locally constant function on $|X|$. Indeed, on a
trivializing covering the subsets of constant rank are open, closed
and saturated, and they descend by fpqc descent of open subsets. Since
$X$ is the disjoint union of the open and closed subsets on which the rank
is constant, and the sheaf of lattices restricts to the sheaf of lattices
on each of them, we may assume that $L$ has constant rank $r$.

Consider the
sheaf on $X_{\mathrm{pro}\acute{e}t}$ whose sections over $U$ are the lisse
$\mathcal O_{E,U}$-submodules $M\subset L|_U$ with $M[1/\ell]=L|_U$. We
show that it is represented by a separated surjective étale $X$-scheme.
On an affine pro-étale object $V$ where $L$ is free of rank $r$, this
sheaf is the constant sheaf on the set

$$
\GL_r(E)/\GL_r(\mathcal O_E)
$$

of lattices in $E^r$. This set is discrete because $\GL_r(\mathcal O_E)$
is an open subgroup of $\GL_r(E)$. Recall from
Lemma [sk-prop-sfb-qlbar-colimit-x] that on an affine object, sections
of $E_X$ are continuous functions to $E$, with bounded denominators by
quasi-compactness. Hence a change of basis on $V\times_XV$ is a
continuous function to $\GL_r(E)$. Since the stabilizer of a lattice
is open, the action of this function on each fixed lattice is locally
constant. It follows that the induced map from the disjoint union of
copies of $V\times_XV$ indexed by the lattices in $E^r$ to itself is a
morphism of schemes. Indeed, on each component the preimages of the
target components are open and closed and form a disjoint open cover.
Thus the cocycle of the transition matrices defines a descent datum of
schemes for these disjoint unions of copies of $V$.

For affine $V=\operatorname{Spec}B$, the disjoint union of copies of $V$
indexed by a set $I$ is ind-quasi-affine, since its finite subunions are
affine open subschemes and together they cover it. Descent along fpqc coverings is
effective for ind-quasi-affine morphisms [Stacks, Tag 0APK](https://stacks.math.columbia.edu/tag/0APK). Taking a finite
affine trivializing covering of each affine open of $X$ and gluing, we
obtain a scheme representing the sheaf of lattices. It is separated and
étale over $X$ by [Stacks, Tag 02KU](https://stacks.math.columbia.edu/tag/02KU), [Stacks, Tag 02VN](https://stacks.math.columbia.edu/tag/02VN), and it is surjective because
every free module has a lattice. By descent of sheaves of modules, this
scheme carries a universal lattice.
