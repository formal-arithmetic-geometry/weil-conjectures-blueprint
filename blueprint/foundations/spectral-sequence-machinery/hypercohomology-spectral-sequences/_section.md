+++
id = "hypercohomology-spectral-sequences"
kind = "section"
title = "Hypercohomology spectral sequences"
order = 1216
uses = ["def-sp-acyclic", "def-sp-convergence", "def-sp-exact-couple", "def-sp-grothendieck-abelian", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "lem-sp-edge-collapse", "lem-sp-kinjective-computes", "lem-sp-long-exact-of-triangle", "thm-sp-half-plane-convergence", "thm-sp-spectral-object-yields"]
+++
The two hypercohomology spectral sequences of a bounded-below complex. The
first comes from canonical truncation: the truncation triangles form an exact
couple [def-sp-truncation-couple], [lem-sp-truncation-couple-exact] whose
spectral sequence has $E_2^{p,q}=R^pv(\mathcal H^q K)$ and converges
unconditionally because it lives in a half plane
[thm-sp-truncation-e2]. The second comes from a Cartan--Eilenberg
resolution and has $E_1^{r,s}=R^rv(K^s)$ [thm-sp-if-e1]; collapsing it gives
the Leray acyclicity criterion [lem-sp-leray-acyclicity], which is how
acyclic resolutions are allowed to compute derived functors.
