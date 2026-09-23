+++
id = "hypercohomology-spectral-sequences"
kind = "section"
title = "Hypercohomology spectral sequences"
order = 1227
uses = ["def-sp-acyclic", "def-sp-convergence", "def-sp-exact-couple", "def-sp-grothendieck-abelian", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "lem-sp-edge-collapse", "lem-sp-long-exact-of-triangle", "thm-sp-half-plane-convergence", "thm-sp-spectral-object-yields"]
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

The K-injective comparison [lem-sp-kinjective-computes] closes the section. The
source files it under the Grothendieck spectral sequence, but it is about the
K-injective bridge [def-sp-kinjective-bridge] and the truncation couple
[def-sp-truncation-couple] of this section, and filing it there made the two
sections cite each other in both directions.

Its proof and the proof of [thm-sp-if-e1] cite each other in the source: the
theorem's resolution-independence clause appeals to the K-injective comparison,
and the comparison appeals to the Cartan--Eilenberg resolution of the theorem.
That circularity is genuine and is not repaired here. It is the only one in the
blueprint, and it would be broken by splitting the resolution-independence
clause off from the theorem, which the main construction does not need.
