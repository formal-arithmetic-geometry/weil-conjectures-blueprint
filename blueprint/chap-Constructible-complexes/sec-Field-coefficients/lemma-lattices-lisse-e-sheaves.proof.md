+++
kind = "proof"
of = "lemma-lattices-lisse-e-sheaves"
order = 261
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "theorem-existence-contractible-covers", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "proposition-locally-constant-sheaves-finite-presentation", "proposition-sp-unique-adjoint"]
+++
Where $L$ is free of rank $r$, a lattice is the same as a lattice in $E^r$,
so the sheaf of lattices is locally the constant sheaf on the discrete set
$\GL_r(E)/\GL_r(\mathcal O_E)$. The representing scheme is obtained by
descending the corresponding disjoint unions of copies of the
trivializing objects.

The rank of $L$ is a locally constant function on $|X|$. Indeed, on a
trivializing covering the subsets of constant rank are open, closed
and saturated, and they descend by fpqc descent of open subsets. So
$X$ is the disjoint union of the open and closed subsets on which the rank
is constant. Since the sheaf of lattices restricts to the sheaf of lattices
on each of them, we may assume that $L$ has constant rank $r$.

We now construct the representing scheme.
On a pro-étale affine $V$ where $L$ is free of rank $r$, the
sheaf of lattices is the constant sheaf on the set

$$
\GL_r(E)/\GL_r(\mathcal O_E)
$$

of lattices in $E^r$, which is discrete because $\GL_r(\mathcal O_E)$
is an open subgroup of $\GL_r(E)$. To glue these constant sheaves, recall from
Lemma [lemma-comparison-completed-coefficients] that on an affine object, sections
of $E_X$ are continuous functions to $E$, with bounded denominators by
quasi-compactness. A change of basis on $V\times_XV$ is therefore a
continuous function to $\GL_r(E)$. Since the stabilizer of a lattice
is open, the image of each fixed lattice under this function is locally
constant on $V\times_XV$. Now consider the disjoint union of
copies of $V\times_XV$ indexed by the lattices in $E^r$. On each component, the
preimages of the target components are then open and closed and form a disjoint open
cover, so the induced map from this disjoint union to itself is a
morphism of schemes. In this way the cocycle of the transition matrices defines a descent datum of
schemes for these disjoint unions of copies of $V$.

For affine $V=\operatorname{Spec}B$, the disjoint union of copies of $V$
indexed by a set $I$ is ind-quasi-affine, since its finite subunions are
affine open subschemes and together they cover it. Since descent along fpqc coverings is
effective for ind-quasi-affine morphisms [Stacks, [0APK](https://stacks.math.columbia.edu/tag/0APK)], the descent datum above is effective. Taking a finite
affine trivializing covering of each affine open of $X$ and gluing, we
therefore obtain a scheme representing the sheaf of lattices. This scheme is separated and
étale over $X$ by [Stacks, [02KU](https://stacks.math.columbia.edu/tag/02KU), [02VN](https://stacks.math.columbia.edu/tag/02VN)], and it is surjective because
every free module has a lattice. By descent of sheaves of modules, this
scheme carries a universal lattice.
