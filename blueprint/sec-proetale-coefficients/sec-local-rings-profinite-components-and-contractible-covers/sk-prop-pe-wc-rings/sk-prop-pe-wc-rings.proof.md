+++
kind = "proof"
of = "sk-prop-pe-wc-rings"
title = "outline"
uses = ["sk-prop-pe-stonean"]
+++
The idea is that over each closed point an ind-étale cover of a
strictly henselian local ring splits, so that only the choice of a
component above each point remains, and the projectivity of extremally
disconnected spaces makes this choice continuously. First replace $B$ by an ind-Zariski $B$-algebra, so
that its spectrum is w-local and its closed points lie exactly over the
closed points of $\operatorname{Spec}(R)$. Here ind-Zariski means a
filtered colimit of local isomorphisms, and such a refinement does not
change the local rings.
Let $\mathfrak q\subset B$ lie over a closed point $\mathfrak m$ of
$\operatorname{Spec}(R)$. Since $R_{\mathfrak m}$ is strictly henselian,
the ind-étale local homomorphism $R_{\mathfrak m}\to B_{\mathfrak q}$
is an isomorphism. Hence every component of $\operatorname{Spec}(B)$
maps isomorphically onto the component of $\operatorname{Spec}(R)$ below
it, and it remains to choose one component above each component of
$\operatorname{Spec}(R)$. By Proposition [sk-prop-pe-stonean] the surjection
$\pi_0(\operatorname{Spec}(B))\to\pi_0(\operatorname{Spec}(R))$ of
profinite component spaces has a section.
Restriction to the corresponding closed set of components is realized by a
filtered colimit of localizations at idempotents. The result is an
$R$-algebra isomorphic to $R$, which gives the retraction. For details
see [Stacks, Tag 097D](https://stacks.math.columbia.edu/tag/097D), [Stacks, Tag 09AZ](https://stacks.math.columbia.edu/tag/09AZ), [Stacks, Tag 0982](https://stacks.math.columbia.edu/tag/0982).
