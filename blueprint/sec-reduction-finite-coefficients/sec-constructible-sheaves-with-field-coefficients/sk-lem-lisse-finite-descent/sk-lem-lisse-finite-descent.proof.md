+++
kind = "proof"
of = "sk-lem-lisse-finite-descent"
uses = ["sk-prop-sfb-qlbar-colimit-x"]
+++
Since $X$ is quasi-compact, we may choose a finite covering by
quasi-compact affine pro-étale objects on which all the modules are
free; such refinements exist by [Stacks, Tag 0988](https://stacks.math.columbia.edu/tag/0988). Their pairwise
intersections are quasi-compact since $X$ is quasi-separated. On a quasi-compact object, taking sections
commutes with filtered colimits, because coverings admit finite
quasi-compact refinements and the sheaf condition involves only finite
limits [Stacks, Tag 0739](https://stacks.math.columbia.edu/tag/0739). By Lemma [sk-prop-sfb-qlbar-colimit-x] we have
$\QbarX=\varinjlim_EE_X$. Hence the finitely many transition matrices,
their inverses, and the matrices of the given morphisms have entries
in $E_X$ for a single finite $E$. Their cocycle and compatibility
identities already hold over $E_X$, since $E_X\to\QbarX$ is injective,
and descent of sheaves of modules gives the required lisse modules and
morphisms.
