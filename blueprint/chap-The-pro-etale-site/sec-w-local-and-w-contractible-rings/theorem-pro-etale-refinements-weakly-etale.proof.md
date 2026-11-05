+++
kind = "proof"
of = "theorem-pro-etale-refinements-weakly-etale"
order = 63
uses = ["lemma-stability", "definition-w-local-w-strictly-local", "proposition-w-local-components"]
+++
Weakly étale and ind-étale maps differ only in
how local rings are glued. Namely, after strict localization of the base a
weakly étale map identifies local rings, that is, for every prime $\mathfrak q$ of $B$ lying over
$\mathfrak p\subset R$ the induced map of local rings $R_{\mathfrak p}\to B_{\mathfrak q}$ is an isomorphism.
Such a map becomes ind-Zariski after refinement.

Applying the construction of simultaneous strict localizations to the pair
$R\to B$ we obtain compatible ind-étale refinements $R\to C$
and $B\to D$, with both spectra w-local and with closed points of
$D$ mapping to closed points of $C$. The map $C\to D$ is still weakly
étale by Lemma [lemma-stability], and the local rings
of $C$ at closed points are strictly henselian. Olivier's rigidity
theorem says that a weakly étale local map out of a strictly
henselian local ring is an isomorphism; see [Stacks, [092Z](https://stacks.math.columbia.edu/tag/092Z)]. Applying it at
the closed points of $D$, which lie over closed points of $C$, we get
isomorphisms of local rings there. Every point of the w-local
$\operatorname{Spec}(D)$ is a generalization of a closed point, and its
local ring is a localization of the local ring at that closed point.
Hence $C\to D$ identifies all local rings. For a ring map that identifies
local rings there is a faithfully flat ind-Zariski refinement of the target
over which the map becomes ind-Zariski [Stacks, [097G](https://stacks.math.columbia.edu/tag/097G)]. Applied to $C\to D$,
this gives a faithfully flat ind-Zariski map $D\to D'$ such that
$C\to D'$ is ind-Zariski, and we take $B'=D'$.

The algebra $B'$ has the two required properties. The map $B\to B'$ is the
composite $B\to D\to D'$ of two faithfully flat ind-étale maps, and
$R\to B'$ is the composite $R\to C\to D'$ of an ind-étale and an
ind-Zariski map. Both composites are ind-étale by
Lemma [lemma-stability]. For details see [Stacks, [097Z](https://stacks.math.columbia.edu/tag/097Z)].
