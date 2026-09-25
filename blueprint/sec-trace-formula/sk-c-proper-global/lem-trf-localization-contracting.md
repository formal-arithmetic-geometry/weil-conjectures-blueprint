+++
id = "lem-trf-localization-contracting"
kind = "lemma"
title = "Localization for a contracting correspondence"
order = 2512
uses = ["lem-trf-contracting-trace-stalk", "lem-trf-local-term-locality", "lem-trf-localization-normal-cone", "thm-trf-contracting-local-term"]
+++
Suppose that after the normal-cone reduction of
[lem-trf-localization-normal-cone] the correspondence is
contracting at every point of its fixed scheme, i.e. its two legs
agree modulo the square of the maximal ideal at each fixed point, so
that the fixed scheme is finite etale over $s$ and its points are
isolated fixed points. Then the localization identity of
[thm-trf-fixed-point-localization] holds.

## Proof

For a contracting correspondence the trace class is concentrated on
the fixed points: by the locality of the trace class
[lem-trf-local-term-locality] the restriction of
$\operatorname{Tr}_c(u)$ to an open-and-closed fixed component
depends only on the stalk data, and the normal-cone reduction
[lem-trf-contracting-trace-stalk] identifies the trace map
restricted to that component with the stalk evaluation, whose value is
the categorical trace of the induced endomorphism of the stalk. This
is the content of the local-term computation for contracting
correspondences, of which the Frobenius case is
[thm-trf-contracting-local-term]; summing over the finitely many
fixed components, and comparing with the trace of the global operator
computed from the same stalk data, gives the asserted identity.
