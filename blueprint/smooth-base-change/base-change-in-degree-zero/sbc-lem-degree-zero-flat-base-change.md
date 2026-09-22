+++
id = "sbc-lem-degree-zero-flat-base-change"
kind = "lemma"
title = "Degree-zero flat base change"
order = 5124
lean = ["AlgebraicGeometry.baseChange_pushforward_of_flat_geometricallyReduced"]
uses = ["sbc-def-base-change-square", "def-sbc-normal-dominant-galois"]
+++
Consider a base-change square [sbc-def-base-change-square] where $f$ is flat
and locally of finite presentation with geometrically reduced
[def-sbc-normal-dominant-galois] fibres (in particular, $f$ may be smooth).
Then
$$
f^{-1}g_*\mathcal F=h_*e^{-1}\mathcal F
$$
for any sheaf $\mathcal F$ on $T_{\Et}$.

(*Stacks Project, Étale Cohomology, Section 59.87 (Base change for
pushforward), [Tag 0EYS](https://stacks.math.columbia.edu/tag/0EYS) = Lemma
59.87.2; the proof combines Lemma 59.87.1, [Tag
0EZX](https://stacks.math.columbia.edu/tag/0EZX), with More on Morphisms,
Lemma 37.46.3, [Tag 0EY5](https://stacks.math.columbia.edu/tag/0EY5): the
connected components of the fibres correspond under the base change, and
direct image is computed by the equalizer of the section descriptions.*)

## Proof

The direct image is computed by the equalizer description of sections along
the fibres; for a flat morphism of finite presentation with geometrically
reduced fibres, the (reduced) connected components of the fibres are the
geometric points, and they correspond under base change, so for $V\to T$
étale the sections of both sides over $V$ are the same systems of sections
on the fibres of $V\times_TY\to V$. This identifies $f^{-1}g_*\mathcal F$
and $h_*e^{-1}\mathcal F$ as sheaves, which is the displayed equality.

Unresolved dependencies: def:weil-pbc-direct-image
