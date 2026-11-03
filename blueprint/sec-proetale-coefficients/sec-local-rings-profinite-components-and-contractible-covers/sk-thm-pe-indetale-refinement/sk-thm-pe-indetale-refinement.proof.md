+++
kind = "proof"
of = "sk-thm-pe-indetale-refinement"
+++
Weakly étale and ind-étale maps differ only in
how local rings are glued: after strict localization of the base a
weakly étale map identifies local rings, and such a map becomes
ind-Zariski after refinement.
Applying the construction of simultaneous strict localizations to the pair
$R\to B$ we obtain compatible ind-étale refinements $R\to C$
and $B\to D$, with both spectra w-local and with closed points of
$D$ mapping to closed points of $C$. The map $C\to D$ is still weakly
étale by Lemma [sk-lem-pe-weakly-etale-stability], and the local rings
of $C$ at closed points are strictly henselian. Olivier's rigidity
theorem says that a weakly étale local map out of a strictly
henselian local ring is an isomorphism; see [Stacks, Tag 092Z](https://stacks.math.columbia.edu/tag/092Z). Applying it at
the closed points of $D$, which lie over closed points of $C$, we get
isomorphisms of local rings there. Every point of the w-local
$\operatorname{Spec}(D)$ is a generalization of a closed point, and its
local ring is a localization of the local ring at that closed point.
Hence $C\to D$ identifies all local rings. By the ind-Zariski refinement theorem for
maps identifying local rings there is a faithfully flat ind-Zariski map
$D\to D'$ such that $C\to D'$ is ind-Zariski, and we take $B'=D'$. For
details see [Stacks, Tag 097Z](https://stacks.math.columbia.edu/tag/097Z).
