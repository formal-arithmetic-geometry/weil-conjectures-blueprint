+++
kind = "proof"
of = "proposition-splitting-ind-etale-covers"
title = "Proof outline"
order = 57
uses = ["proposition-etale-implications", "lemma-stability", "proposition-w-local-components", "proposition-gleason-s-theorem"]
+++
We first replace $B$ by an ind-Zariski $B$-algebra, so
that its spectrum is w-local and its closed points lie exactly over the
closed points of $\operatorname{Spec}(R)$; such a refinement does not
change the local rings.
Let $\mathfrak q\subset B$ lie over a closed point $\mathfrak m$ of
$\operatorname{Spec}(R)$. Since $R_{\mathfrak m}$ is strictly henselian,
the ind-étale local homomorphism $R_{\mathfrak m}\to B_{\mathfrak q}$
is an isomorphism. Hence every component of $\operatorname{Spec}(B)$
maps isomorphically onto the component of $\operatorname{Spec}(R)$ below
it, and a retraction amounts to a continuous choice of one component above each component of
$\operatorname{Spec}(R)$. Such a choice exists because, by Proposition [proposition-gleason-s-theorem], the surjection
$\pi_0(\operatorname{Spec}(B))\to\pi_0(\operatorname{Spec}(R))$ of
profinite component spaces has a section.
Given such a section, we restrict $B$ to the corresponding closed set of components by a
filtered colimit of localizations at idempotents. The result is an
$R$-algebra isomorphic to $R$, and this gives the retraction. For details
see [Stacks, [097D](https://stacks.math.columbia.edu/tag/097D), [09AZ](https://stacks.math.columbia.edu/tag/09AZ), [0982](https://stacks.math.columbia.edu/tag/0982)].
