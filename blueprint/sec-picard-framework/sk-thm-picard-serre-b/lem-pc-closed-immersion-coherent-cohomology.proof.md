+++
kind  = "proof"
of    = "lem-pc-closed-immersion-coherent-cohomology"
+++
Over $V=\operatorname{Spec}(R)\subset Y$, write
$i^{-1}(V)=\operatorname{Spec}(R/I)$. The module of sections of
$\mathcal F$ there is finite over $R/I$, hence finite over $R$.
It computes $i_*\mathcal F|_V$ with the usual localization maps,
so [pqf-lem-coherent-ft-locnoeth] proves coherence.
Closed immersions are affine by this same description, and
[lem-pc-affine-morphism-hi] gives $R^qi_*\mathcal F=0$ for
$q>0$. The Leray spectral sequence [pqf-lem-leray] therefore
gives the asserted cohomology identifications.
Finally trivialize $\mathcal L$ on an open cover as allowed by
[def-sc-invertible-module]. On each member the tensor map
is the identity on $i_*\mathcal F$; these are the restrictions of
the natural map, and hence prove its isomorphism globally.
