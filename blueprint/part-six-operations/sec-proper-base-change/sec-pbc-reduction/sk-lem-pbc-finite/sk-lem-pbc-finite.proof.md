+++
kind = "proof"
of = "sk-lem-pbc-finite"
+++
After base change to the strict henselization of $W$ at $\bar w$, the finite
scheme $V$ becomes a finite disjoint union of strictly henselian local schemes.
On each such local scheme, the sections of an étale sheaf are its stalk at
the closed geometric point. Indeed, every étale neighbourhood of that
point admits a section, so a germ extends to a global section, and two
sections with the same germ agree after pulling back along such a section. In
particular, taking sections is exact on abelian sheaves. Combining this with
the description of stalks of direct images via strict localizations
[Stacks, Tag 03QP](https://stacks.math.columbia.edu/tag/03QP), we obtain the displayed formula.
Since geometric stalks are conservative and finite products of abelian groups
are exact, $u_*$ is exact.

In a cartesian square over $W'\to W$, a geometric point of $W'$ and
its image in $W$ have the same geometric fibre, and the underived
base change map is the identity on the corresponding factors of the displayed
formula, so it is an isomorphism. Since both
direct images in the square are exact, their derived functors and
the base change map are computed term by term. The same argument applies to
sheaves of modules.
