+++
id = "sk-cor-pe-sections"
kind = "corollary"
title = "A conservative family preserving all module colimits"
order = 1519
uses = ["sk-thm-pe-weakly-contractible-basis", "sk-cor-pe-wc-sections", "sk-def-pe-weak-contractible"]
tags = ["sketch"]
+++
Let $X$ be an arbitrary scheme and $\mathcal R$ any sheaf of rings on $X_{\mathrm{proét}}$
(for instance the pullback of a condensed ring). Evaluation on all affine weakly
contractible objects [sk-def-pe-weak-contractible] detects exactness of complexes and
isomorphisms of $\mathcal R$-module sheaves. For each such object $W$, evaluation preserves
all limits and all colimits of $\mathcal R$-modules.

The quasi-compactness used here is quasi-compactness as an object of the site: coverings
admit finite refinements. Affine objects of $X_{\mathrm{proét}}$ have this property. Over a
quasi-compact, quasi-separated object, the quasi-compact, quasi-separated subsite with
finite covers is a coherent site. In topos terminology an object $P$ is coherent if it is
quasi-compact and $V\times_PV$ is quasi-compact for every quasi-compact object $V$ mapping
to $P$. Together with the affine refinements, this provides the local coherent projective
objects required for $\Sh(X_{\mathrm{proét}})$ to be a *locally weakly contractible* topos
in the sense of the companion pro-étale blueprint.
