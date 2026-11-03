+++
kind = "proof"
of = "sk-cor-pe-finite-tor-comparison"
uses = ["lem-exc-constant-inverse-image-flat", "lem-exc-comparison-tor-interval", "det-pe-finite-tor-comparison-noetherian", "sk-prop-pe-comparison-morphism"]
+++
The functor $\nu_X^*$ is exact (Proposition [sk-prop-pe-comparison-morphism]),
and since $\nu_X^*\Lambda=\Lambda_X$ it is symmetric monoidal on sheaves
of modules. The pullback of a flat sheaf of modules is flat
[Stacks, Tag 05VD](https://stacks.math.columbia.edu/tag/05VD). An étale complex of Tor amplitude in $[a,b]$ is
represented by a complex of flat sheaves in degrees $[a,b]$, and its
pullback is a complex of flat pro-étale sheaves in the same degrees.
Hence it has Tor amplitude in $[a,b]$ against every pro-étale module,
not only against pulled-back ones. Conversely, let $K$ be an étale complex. Its
Tor amplitude can be read off from $K\otimes^{\mathbf L}_\Lambda M$ for
arbitrary étale sheaves of modules $M$. The inverse image of this complex is
$\nu_X^*K\otimes^{\mathbf L}_{\Lambda_X}\nu_X^*M$, and since $\nu_X^*$
is exact and fully faithful, it detects vanishing of cohomology. Hence a
Tor bound on $\nu_X^*K$ implies the same bound on $K$.
