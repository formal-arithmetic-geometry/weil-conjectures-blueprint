+++
id = "lem-weil-pbc-sheafification-exact"
kind = "lemma"
title = "Sheafification of abelian presheaves is exact; limits of abelian sheaves are sectionwise"
order = 1061
uses = ["def-weil-pbc-sheafification"]
lean = ["CategoryTheory.instPreservesFiniteLimitsFunctorOppositeSheafPresheafToSheaf"]
tags = ["mathlib", "stacks-00WJ"]
+++
Let $\mathcal C$ be a site, $\mathrm{PAb}(\mathcal C)$ the category of presheaves of abelian groups on $\mathcal C$ and $\Ab(\mathcal C)\subseteq\mathrm{PAb}(\mathcal C)$ the full subcategory of sheaves, with inclusion $\iota$ and sheafification $\mathcal F\mapsto\mathcal F^\#$, $\#:\mathrm{PAb}(\mathcal C)\to\Ab(\mathcal C)$, left adjoint to $\iota$ [def-weil-pbc-sheafification]. Then:

1. $\iota$ commutes with all limits, in particular with finite limits: the limit of a diagram of abelian sheaves is its limit as presheaves, computed sectionwise; e.g. the kernel of a morphism of abelian sheaves is the sectionwise kernel;
2. $\#$ commutes with finite limits, and (as a left adjoint) with all colimits; hence $\#$ is exact.
