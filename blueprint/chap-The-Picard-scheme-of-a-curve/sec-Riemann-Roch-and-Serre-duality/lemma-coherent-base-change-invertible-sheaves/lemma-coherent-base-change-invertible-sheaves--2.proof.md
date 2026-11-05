+++
kind = "proof"
of = "lemma-coherent-base-change-invertible-sheaves--2"
order = 1530005
uses = ["lemma-acyclic-resolutions"]
+++
Restrict the cartesian square to $V$. Higher direct images commute with
this open restriction, by
`AlgebraicGeometry.Scheme.Modules.nonempty_higherDirectImage_iso_restrict`:
restriction is exact and takes injective modules to modules acyclic for
pushforward. Paste the restricted square with the original square, using
$\iota_Ua_V=a\iota_V$. The assumed comparison for $a_V$ identifies the
higher direct images of the resulting pullback with
$\mathcal H^q(a_V^*P^\bullet)$. The pullback-composition isomorphism
identifies its coefficient module with the restriction of $b^*\mathcal F$,
and composing these isomorphisms gives the result.
