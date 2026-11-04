+++
kind = "proof"
of = "lemma-descent-lisse-qbar-sheaves-finite"
order = 266
+++
The data are described by finitely many matrices with entries in
$\QbarX$ over finitely many quasi-compact objects, and each entry already
lies in some $E_X$. We make this precise.

Since $X$ is quasi-compact, we may choose a finite covering by
quasi-compact pro-étale affines on which all the modules are
free; such refinements exist by [Stacks, [0988](https://stacks.math.columbia.edu/tag/0988)]. Their pairwise
intersections are quasi-compact since $X$ is quasi-separated. On a quasi-compact object, taking sections
commutes with filtered colimits, because coverings admit finite
quasi-compact refinements and the sheaf condition involves only finite
limits [Stacks, [0739](https://stacks.math.columbia.edu/tag/0739)]. By Lemma [lemma-comparison-completed-coefficients] we have
$\QbarX=\varinjlim_EE_X$. Hence the finitely many transition matrices,
their inverses, and the matrices of the given morphisms have entries
in $E_X$ for a single finite $E$. Their cocycle and compatibility
identities already hold over $E_X$, since $E_X\to\QbarX$ is injective.
Descent of sheaves of modules now gives the required lisse modules and
morphisms.
