+++
id = "lem-sf-orientation-product"
kind = "lemma"
title = "The orientation is multiplicative"
order = 3705
uses = ["def-sf-orientation", "lem-sf-kunneth-coherence", "thm-sf-dualizing-product"]
+++
In the setting of [def-sf-orientation], let $f:X\to Y$ and
$g:X'\to Y'$ be smooth separated finite-type morphisms of pure relative
dimensions $d$ and $d'$ carrying orientations $\eta_f,\eta_g$ of the datum,
and form $f\times_Sg:X\times_SX'\to Y\times_SY'$ over a common base $S$.
Then $\eta_f\otimes\eta_g$ is an orientation for $f\times_Sg$: the class of
morphisms carrying an orientation is stable under products, compatibly with
the base-change and composition coherences of the datum.

## Proof

The product is smooth of pure relative dimension $d+d'$, and by
[thm-sf-dualizing-product] the two sides of
$L(f\times_Sg)^*\Lambda(d+d')[2(d+d')]\cong R(f\times_Sg)^!\Lambda$ are the
tensor products of the corresponding objects for $f$ and for $g$: the
pullback side by the Künneth identification of the external product of
constant sheaves, the exceptional side by the composition law applied to the
two projections. Under these identifications $\eta_f\otimes\eta_g$ is an
isomorphism on each factor, hence an isomorphism, and it is natural because
$\eta_f$ and $\eta_g$ are; the compatibilities with base change and
composition are those of [lem-sf-kunneth-coherence] together with the
corresponding coherences of the two given orientations.
