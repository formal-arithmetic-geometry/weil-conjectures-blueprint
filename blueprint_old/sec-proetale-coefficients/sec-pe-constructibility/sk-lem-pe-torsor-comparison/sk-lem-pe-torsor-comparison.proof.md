+++
kind = "proof"
of = "sk-lem-pe-torsor-comparison"
uses = ["sk-thm-pe-indetale-refinement", "sk-prop-pe-comparison-morphism"]
+++
A torsor is described by a cocycle on a single
pro-étale affine cover, and since sections of a classical sheaf on a
limit come from a finite stage, the cocycle already lives on an étale
cover.
Write the group as $\nu_X^*G_0$. We may work on an affine open of $X$.
Using Theorem [sk-thm-pe-indetale-refinement] and finite affine
refinements, we refine a trivializing covering to a single faithfully
flat ind-étale affine $U\to X$, and we write $U=\varprojlim_iU_i$ with
$U_i$ affine étale over $X$. A trivialization over $U$ determines a
transition element in $\nu_X^*G_0(U\times_XU)$. By continuity for affine
limits it descends to $G_0(U_i\times_XU_i)$ for some $i$, and the cocycle
identity on the triple product holds after enlarging $i$. Since
$U\to X$ is surjective, each $U_i\to X$ is an étale covering. Gluing the
trivial torsor along this cocycle, we get an étale torsor whose
pullback is isomorphic to the given torsor. Hence the given torsor is
classical by Theorem [sk-thm-pe-classical-sheaves], and it is trivialized by
the étale covering $U_i\to X$. See [Stacks, Tag 099X](https://stacks.math.columbia.edu/tag/099X).
