+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-affine-cover"
uses = ["sk-lem-nagata-sketch-elimination", "sk-lem-nagata-sketch-closure"]
+++
For any point of $X$, the affine-neighbourhood lemma (Stacks 01ZX, in its
case of finitely many irreducible components) supplies an affine open
containing that point and all the generic points of the components.
Quasi-compactness selects finitely many such opens. Their total intersection
still contains all generic points and is therefore dense.

For the second assertion, $Y$ is quasi-affine and locally of finite type
over $S$, so the relative affine-space immersion lemma (Stacks 04II;
[lemma-nagata-zmt-open-immersion-affine-factorization], [lemma-nagata-quasi-affine-immersion-affine-space-exists]) embeds it over $S$ as a locally closed
subscheme of some $\mathbf A^{n}_S$. As $Y\to S$ is quasi-compact, so is the
resulting immersion $Y\to\mathbf P^{n}_S$. Its schematic closure in
$\mathbf P^{n}_S$ is proper over $S$, and [sk-lem-nagata-sketch-closure]
makes $Y$ an open in that closure. An affine $U_r$ is quasi-affine, its map
to $S$ is locally of finite type, and it is quasi-compact because $U_r$ is
quasi-compact and $S$ is quasi-separated.
