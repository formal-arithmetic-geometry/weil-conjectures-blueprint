+++
id = "hypercohomology-spectral-sequences"
kind = "section"
title = "Hypercohomology spectral sequences"
order = 1139
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-grothendieck-abelian", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "lem-sp-long-exact-of-triangle", "thm-sp-half-plane-convergence", "thm-sp-spectral-object-yields"]
+++
The section opens with the definition the rest of the chapter had been using
without stating: $Rv$ on a bounded-below *complex*, by K-injective resolution
[def-sp-kinjective-bridge], well defined and compatible with the derived
functors of an object [lem-sp-kinjective-computes]. Everything after it —
the truncation couple, the shift rule and both spectral sequences — is about
$Rv$ of a complex, so nothing here is meaningful before it.

Then the two hypercohomology spectral sequences of a bounded-below complex. The
first comes from canonical truncation: the truncation triangles form an exact
couple [def-sp-truncation-couple], [lem-sp-truncation-couple-exact] whose
spectral sequence has $E_2^{p,q}=R^pv(\mathcal H^q K)$ and converges
unconditionally because it lives in a half plane
[thm-sp-truncation-e2]. The second comes from a Cartan--Eilenberg
resolution and has $E_1^{r,s}=R^rv(K^s)$ [thm-sp-if-e1]; collapsing it gives
the Leray acyclicity criterion [lemma-weil-pbc-leray-acyclicity], which is how
acyclic resolutions are allowed to compute derived functors.

The K-injective comparison [lem-sp-kinjective-computes] is filed under the
Grothendieck spectral sequence in the source, but it is about the K-injective
bridge of this section and nothing in the Grothendieck section uses it; it
stands here, directly after the definition it justifies.

Its proof and the proof of [thm-sp-if-e1] cited each other in the source — the
theorem took independence of the resolution from the lemma, and the lemma took
the agreement of its two routes from the theorem's Cartan--Eilenberg
resolution. The cause was the missing definition: with $Rv$ on complexes
undefined, each statement was the only thing that could pin down what the other
one meant. With [def-sp-kinjective-bridge] stating it, the lemma is proved from
K-injectivity alone and the theorem is proved from the lemma. The dependence
runs one way and the chapter has no circular proof left.
