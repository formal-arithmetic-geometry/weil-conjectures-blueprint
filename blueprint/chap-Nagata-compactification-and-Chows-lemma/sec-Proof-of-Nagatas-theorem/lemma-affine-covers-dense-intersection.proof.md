+++
kind = "proof"
of = "lemma-affine-covers-dense-intersection"
order = 1457
uses = ["lemma-schematic-closure-uniqueness"]
+++
The scheme $X$ has finitely many irreducible components.
By [Stacks, [01ZX](https://stacks.math.columbia.edu/tag/01ZX)], every point of $X$ has an affine open neighbourhood
that also contains all the generic points of those components, and
since $X$ is quasi-compact, finitely many such opens cover $X$. Their
total intersection still contains all generic points, so it is dense.
For the second assertion, note that each $U_r$ is affine of finite
type over $S$, so by [Stacks, [04II](https://stacks.math.columbia.edu/tag/04II)] we may embed it as a locally closed
subscheme of some $\mathbf A^{n_r}_S$. Its schematic closure in $\mathbf P^{n_r}_S$ is
proper, and by Lemma [lemma-schematic-closure-uniqueness] the scheme $U_r$ is open
in that closure.
