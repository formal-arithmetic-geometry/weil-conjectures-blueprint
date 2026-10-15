+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-affine-cover"
uses = ["sk-prop-nagata-sketch-zmt", "sk-lem-nagata-sketch-closure"]
+++
There are finitely many irreducible components of $X$. For any point of
$X$, the affine-neighbourhood lemma (Stacks 01ZX) supplies an affine open
containing that point and all the generic points of those components.
Quasi-compactness selects finitely many such opens. Their total intersection
still contains all generic points and is therefore dense.

Each $U_r$ is affine and its map to $S$ is of finite type. The relative
affine-space immersion lemma (Stacks 04II; [sk-prop-nagata-sketch-zmt])
embeds it as a locally closed subscheme of some $\mathbf A^{n_r}_S$. Its
schematic closure in $\mathbf P^{n_r}_S$ is proper, and
[sk-lem-nagata-sketch-closure] makes $U_r$ an open in that closure.
