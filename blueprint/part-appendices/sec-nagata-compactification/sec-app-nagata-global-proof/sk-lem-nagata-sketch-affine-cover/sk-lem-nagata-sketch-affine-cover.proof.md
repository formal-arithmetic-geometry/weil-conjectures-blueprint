+++
kind = "proof"
of = "sk-lem-nagata-sketch-affine-cover"
uses = ["sk-lem-nagata-sketch-elimination", "sk-lem-nagata-sketch-closure"]
+++
The scheme $X$ has finitely many irreducible components.
By [Stacks, Tag 01ZX](https://stacks.math.columbia.edu/tag/01ZX), every point of $X$ has an affine open neighbourhood
that also contains all the generic points of those components. Since
$X$ is quasi-compact, finitely many such opens cover $X$. Their total
intersection still contains all generic points and is therefore dense.
Each $U_r$ is affine of finite type over $S$. By
[Stacks, Tag 04II](https://stacks.math.columbia.edu/tag/04II) we may embed $U_r$ as a locally closed subscheme of some
$\mathbf A^{n_r}_S$. Its schematic closure in $\mathbf P^{n_r}_S$ is
proper, and by Lemma [sk-lem-nagata-sketch-closure] the scheme $U_r$ is open
in that closure.
